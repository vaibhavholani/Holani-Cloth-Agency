from __future__ import annotations
from typing import List, Tuple
import datetime
from Entities import RegisterEntry
from Database import db_connector, retrieve_indivijual, retrieve_gr


def get_register_entry_id(supplier_id: int, party_id: int, bill_number: int) -> int:
    """
    Returns primary key id of the register entry
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from register_entry where bill_number = '{}' AND supplier_id = '{}' AND party_id = '{}' " \
            "order by " \
            "register_date DESC". \
        format(bill_number, supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def check_unique_bill_number(supplier_id: int, party_id: int, bill_number: int, date: str) -> bool:
    """
    Check if the bill number if unique
    """
    db = db_connector.connect()
    cursor = db.cursor()

    date = datetime.datetime.strptime(date, "%d/%m/%Y")

    query = "select id, register_date from register_entry where " \
            "bill_number = '{}' AND supplier_id = '{}' AND party_id = '{}'". \
        format(bill_number, supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()

    if len(data) == 0:
        return True

    if (date - data[0][1]).days >= 2:
        return True

    return False


def get_pending_bill_numbers(supplier_id: int, party_id: int) -> List[int]:
    """
    Returns a list of all pending bill numbers between party and supplier.
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select bill_number from register_entry where supplier_id = '{}' AND party_id = '{}' AND status != '{}'".\
        format(supplier_id, party_id, "F")
    cursor.execute(query)
    data = cursor.fetchall()
    data_r = [int(x[0]) for x in data]
    db.disconnect()
    return data_r


def get_register_entry(supplier_id: int, party_id: int, bill_number: int) -> RegisterEntry:
    """
    Return the register entry associated with given bill number
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    # Getting names
    supplier_name = retrieve_indivijual.get_supplier_name_by_id(supplier_id)
    party_name = retrieve_indivijual.get_party_name_by_id(party_id)

    # Getting data from the database for each bill number
    query = "select DATE_FORMAT(register_date, '%d/%m/%Y'), amount, partial_amount, status, d_amount, d_percent, gr_amount " \
            "from register_entry where " \
            "bill_number = '{}' AND supplier_id = '{}' AND party_id = '{}'". \
        format(bill_number, supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()

    r_list = []
    for entries in data:
        # make register entries
        reference = entries

        # Setting variables
        amount = int(reference[1])
        date = str(reference[0])
        part_amount = int(reference[2])
        status = reference[3]
        d_amount = int(reference[4])
        d_percent = int(reference[5])
        gr_amount = int(reference[6])

        # creating register entry
        re_curr = RegisterEntry.RegisterEntry(bill_number, amount, supplier_name, party_name, date)
        re_curr.part_payment = part_amount
        re_curr.status = status
        re_curr.d_amount = d_amount
        re_curr.d_percent = d_percent
        re_curr.gr_amount = gr_amount
        r_list.append(re_curr)

    db.disconnect()

    return r_list


def get_register_entry_bill_numbers(supplier_id: int, party_id: int, bill_number: List[int]) -> List[RegisterEntry]:
    """
    Returns register_entries with the given bill_number(s)
    """

    re_by_bill = []

    for bill_num in bill_number:

        re_curr = get_register_entry(supplier_id, party_id, bill_num)
        # adding it to the list
        re_by_bill = re_by_bill + re_curr

    return re_by_bill


def get_khata_data_by_date(supplier_id: int, party_id: int, start_date: str, end_date: str) -> List[Tuple]:
    """
    Returns a list of all bill_number's amount and date between the given dates
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    data = []

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    query = "select register_entry.bill_number, DATE_FORMAT(register_entry.register_date, '%d/%m/%Y'), " \
            "register_entry.amount, register_entry.status " \
            "from register_entry " \
            "where party_id = '{}' AND supplier_id = '{}' AND " \
            "register_date >= '{}' AND register_date <= '{}';"\
        .format(party_id, supplier_id, start_date, end_date)

    cursor.execute(query)
    bills_data = cursor.fetchall()

    if len(bills_data) == 0:
        return bills_data

    for bills in bills_data:
        query_2 = "select memo_entry.memo_number, memo_bills.amount,DATE_FORMAT(memo_entry.register_date, '%d/%m/%Y'), " \
                  "memo_bills.type, memo_entry.amount " \
                  "from memo_entry JOIN memo_bills on (memo_entry.id = memo_bills.memo_id) " \
                  "where memo_bills.bill_number = '{}' AND memo_entry.supplier_id = '{}' " \
                  "AND memo_entry.party_id = '{}'; " \
            .format(bills[0], supplier_id, party_id)
        cursor.execute(query_2)
        memo_data = cursor.fetchall()

        for nums in range(len(memo_data)):
            if nums == 0:
                data_tuple = bills + memo_data[nums]
            else:
                data_tuple = (" ", " ", " ", " ") + memo_data[nums]

            data.append(data_tuple)

        if len(memo_data) == 0:
            data_tuple = bills + ("-", "-", "-", "-")
            data.append(data_tuple)

    db.disconnect()
    return data


def get_supplier_register_data(supplier_id: int, party_id: int, start_date: str, end_date: str) -> List[Tuple]:
    """
        Returns a list of all bill_number's amount and date
        """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    query = "select bill_number, amount, " \
            "CASE WHEN status='F' THEN '0'" \
            "ELSE (amount - (partial_amount)-(gr_amount)) END AS pending_amount," \
            "DATE_FORMAT(register_date, '%d/%m/%Y'), status from " \
            "register_entry JOIN party ON party.id = register_entry.party_id " \
            "where supplier_id = '{}' AND party_id = '{}' AND " \
            "register_date >= '{}' AND register_date <= '{}'". \
        format(supplier_id, party_id, start_date, end_date)

    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data


def get_payment_list_data(supplier_id: int, party_id: int, start_date: str, end_date: str) -> List[Tuple]:
    """
    Get all the pending bills info
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    query = "select bill_number, amount, " \
            "(amount - (partial_amount)-gr_amount)," \
            "DATE_FORMAT(register_date, '%d/%m/%Y'), " \
            "DATEDIFF(NOW(),register_date), " \
            "status from " \
            "register_entry JOIN supplier ON supplier.id = register_entry.supplier_id " \
            "where supplier_id = '{}' AND party_id = '{}' AND " \
            "register_date >= '{}' AND register_date <= '{}' AND status != 'F'". \
        format(supplier_id, party_id, start_date, end_date)

    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data


def get_payment_list_summary_data(supplier_id: int, party_id: int, start_date: str, end_date: str) -> List[Tuple]:
    """
    Get summarised data for all payment lists summary
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    # Find amount less than 40 days
    query1 = "select SUM(amount), SUM(amount) - SUM(partial_amount) - SUM(gr_amount)" \
             "from register_entry where party_id = '{}' AND supplier_id = '{}'" \
             " AND status != 'F' AND DATEDIFF(NOW(), register_date) < 40 AND register_date >= '{}' " \
             "AND register_date <= '{}';".format(party_id, supplier_id, start_date, end_date)

    # Find amount between 40 and 70 days
    query2 = "select SUM(amount), SUM(amount) - SUM(partial_amount) - SUM(gr_amount) " \
             "from register_entry where party_id = '{}' AND supplier_id = '{}' " \
             "AND status != 'F' AND DATEDIFF(NOW(), register_date) BETWEEN 40 AND 70 AND register_date >= '{}' AND " \
             "register_date <= '{}';".format(party_id, supplier_id, start_date, end_date)

    # Find amount more than 70 days
    query3 = "select SUM(amount), SUM(amount) - SUM(partial_amount) - SUM(gr_amount) " \
             "from register_entry where party_id = '{}' AND supplier_id = '{}' " \
             "AND status != 'F' AND 70 < DATEDIFF(NOW(), register_date) AND register_date >= '{}' " \
             "AND register_date <= '{}';".format(party_id, supplier_id, start_date, end_date)

    cursor.execute(query1)
    data1 = cursor.fetchall()
    if data1[0][0] is None:
        data1 = [("-", "-", "-")]

    cursor.execute(query2)
    data2 = cursor.fetchall()

    if data2[0][0] is None:
        data2 = [("-", "-","-")]

    cursor.execute(query3)
    data3 = cursor.fetchall()

    if data3[0][0] is None:
        data1 = [("-", "-", "-")]

    data = data1 + data2 + data3
    db.disconnect()
    return data


def grand_total_work(supplier_id: int, party_id: int, start_date: str, end_date: str) -> int:
    """
    Get the grand total for each porty for the selected suppliers
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    query = "select SUM(amount) from register_entry where " \
            "party_id = '{}' AND supplier_id = '{}' AND " \
            "register_date >= '{}' AND register_date <= '{}';".format(party_id, supplier_id, start_date, end_date)

    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()

    if data[0][0] is None:
        return 0
    return data[0][0]


def grand_total_gr(supplier_id: int, party_id: int, start_date: str, end_date: str) -> int:
    """
    Get the GR between supplier and party
    """
    r_val = retrieve_gr.get_gr_between_dates(supplier_id, party_id, start_date, end_date)
    if r_val == -1:
        return 0


def legacy_no_memo(curr_pld: Tuple) -> List[Tuple]:
    """
    Returns legacy payment bill with no memos
    """
    if curr_pld[4] < 40:
        bill_tuple = [("-", "-", "-","-", "-", "-", curr_pld[2], curr_pld[0], curr_pld[3])]
    elif 40 <= curr_pld[4] <= 70:
        bill_tuple = [("-", "-", "-", "-", "-", curr_pld[2], "-", curr_pld[0], curr_pld[3])]
    else:
        bill_tuple = [("-", "-", "-", "-", curr_pld[2], "-", "-", curr_pld[0], curr_pld[3])]

    return bill_tuple


def legacy_one_memo(curr_pld: Tuple, curr_memo: Tuple) -> List[Tuple]:
    """
    Returns legacy payment bill with one memo
    """
    if curr_pld[4] < 40:
        bill_tuple = [(curr_memo[0], curr_memo[1], curr_memo[2], curr_memo[3], "-", "-", curr_pld[2], curr_pld[0], curr_pld[3])]
    elif 40 <= curr_pld[4] <= 70:
        bill_tuple = [(curr_memo[0], curr_memo[1], curr_memo[2], curr_memo[3], "-", curr_pld[2], "-", curr_pld[0], curr_pld[3])]
    else:
        bill_tuple = [(curr_memo[0], curr_memo[1], curr_memo[2], curr_memo[3], curr_pld[2], "-", "-", curr_pld[0], curr_pld[3])]

    return bill_tuple


def legacy_multiple_memo(curr_memo: Tuple) -> List[Tuple]:
    """
    Returns legacy payment bill with multiple memos
    """
    bill_tuple = [(curr_memo[0], curr_memo[1], curr_memo[2], curr_memo[3], "-", "-", "-", "-", "-")]
    return bill_tuple


def legacy_payment_list(supplier_id: int, party_id: int, start_date: str, end_date: str):
    """
    Get the legacy payment list
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    p_l_d = get_payment_list_data(supplier_id, party_id, start_date, end_date)

    bills_data = [data[0] for data in p_l_d]
    print(type(bills_data[0]))

    memo_data = []
    for bills in bills_data:
        query_2 = "select memo_entry.memo_number, memo_bills.amount, memo_bills.type, " \
                  "DATE_FORMAT(memo_entry.register_date, '%d/%m/%Y') " \
                  "from memo_entry JOIN memo_bills on (memo_entry.id = memo_bills.memo_id) " \
                  "where memo_bills.bill_number = '{}' AND memo_entry.supplier_id = '{}' " \
                  "AND memo_entry.party_id = '{}'; " \
            .format(bills, supplier_id, party_id, start_date, end_date)
        cursor.execute(query_2)
        add_memo_data = cursor.fetchall()
        memo_data.append(add_memo_data)

    legacy_data = []
    for entry in range(len(bills_data)):

        curr_pld = p_l_d[entry]
        curr_memo = memo_data[entry]
        bill_tuples = []
        if len(curr_memo) == 0:
            bill_tuples.extend(legacy_no_memo(curr_pld))
        elif len(curr_memo) == 1:
            bill_tuples.extend(legacy_one_memo(curr_pld, curr_memo[0]))
        else:
            # Add the first entry and fill the rest with spaces
            bill_tuples.extend(legacy_one_memo(curr_pld, curr_memo[0]))
            # Make functions to make execution easier?
            for memos in curr_memo[1:]:
                bill_tuples.extend(legacy_multiple_memo(memos))

        legacy_data.extend(bill_tuples)

    return legacy_data




