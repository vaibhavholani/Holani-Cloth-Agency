from __future__ import annotations
from Entities import MemoEntry
from Database import db_connector, retrieve_indivijual
import datetime


def check_new_memo(memo_number: int, memo_date: str, supplier_name: str, party_name: str) -> bool:
    """
    Check if the memo already exists.
    """
    # Open a new connection
    db, cursor = db_connector.cursor()
    date = datetime.datetime.strptime(memo_date, "%d/%m/%Y")

    supplier_id = retrieve_indivijual.get_supplier_id_by_name(supplier_name)
    party_id = retrieve_indivijual.get_party_id_by_name(party_name)

    query = "select register_date, supplier_id, party_id from memo_entry where memo_number = '{}' order by 1 DESC".format(
             memo_number)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()

    if len(data) == 0:
        return True
    if (date - data[0][0]).days >= 30:
        return True
    if int(data[0][1]) == supplier_id and int(data[0][2]) == party_id and (date - data[0][0]).days == 0:
        return True
    return False


def check_add_memo(memo_number: int, memo_date: str) -> bool:
    """
    Check if the memo already exists.
    """
    # Open a new connection
    db, cursor = db_connector.cursor()
    date = datetime.datetime.strptime(memo_date, "%d/%m/%Y")

    query = "select register_date from memo_entry where memo_number = '{}' order by 1 DESC".format(
             memo_number)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    if len(data) == 0:
        return True
    if (date - data[0][0]).days >= 365:
        return True
    return False


def get_id_by_memo_number(memo_number, supplier_id, party_id) -> int:
    """
    Get the memo_id using memo_number, supplier_id and party_id
    """
    # Open a new connection
    db, cursor = db_connector.cursor()

    query = "select id from memo_entry where memo_number = {} AND supplier_id = {} AND party_id = {} " \
            "order by register_date DESC;".format(
             memo_number, supplier_id, party_id)

    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return int(data[0][0])
