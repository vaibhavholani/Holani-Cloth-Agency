from __future__ import annotations
from typing import List
from Entities import RegisterEntry
from Database import db_connector, retrieve_indivijual


db = db_connector.connect()
cursor = db.cursor()


def get_pending_bill_numbers(supplier_id: int, party_id: int) -> List[int]:
    """
    Returns a list of all pending bill numbers between party and supplier.
    """
    query = "select bill_number from register_entry where supplier_id = '{}' AND party_id = '{}' AND status != '{}'".\
        format(supplier_id, party_id, "F")
    cursor.execute(query)
    data = cursor.fetchall()
    data_r = [int(x[0]) for x in data]
    return data_r


def get_register_entry(supplier_id: int, party_id: int, bill_number: int) -> RegisterEntry:
    """
    Return the register entry associated with given bill number
    """

    # Getting names
    supplier_name = retrieve_indivijual.get_supplier_name_by_id(supplier_id)
    party_name = retrieve_indivijual.get_party_name_by_id(party_id)

    # Getting data from the database for each bill number
    query = "select DATE_FORMAT(register_date, '%d/%m/%Y'), amount, partial_amount, gr_amount, status " \
            "from register_entry where " \
            "bill_number = '{}' AND supplier_id = '{}' AND party_id = '{}'". \
        format(bill_number, supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()

    # make register entries
    print(data)
    reference = data[0]

    # Setting variables
    amount = int(reference[1])
    date = str(reference[0])
    part_amount = int(reference[2])
    gr_amount = int(reference[3])
    status = reference[4]

    # creating register entry
    re_curr = RegisterEntry.RegisterEntry(bill_number, amount, supplier_name, party_name, date)
    re_curr.part_payment = part_amount
    re_curr.gr_amount = gr_amount
    re_curr.status = status

    return re_curr


def get_register_entry_bill_numbers(supplier_id: int, party_id: int, bill_number: List[int]) -> List[RegisterEntry]:
    """
    Returns register_entries with the given bill_number(s)
    """
    re_by_bill = []

    for bill_num in bill_number:

        re_curr = get_register_entry(supplier_id, party_id, bill_num)
        # adding it to the list
        re_by_bill.append(re_curr)

    return re_by_bill







