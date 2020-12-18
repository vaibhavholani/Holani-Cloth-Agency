from __future__ import annotations
from Entities import MemoEntry
from Database import db_connector


def check_new_memo(memo: MemoEntry) -> bool:
    """
    Check if the memo already exists.
    """
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from memo_entry where memo_number = '{}' AND supplier_id = '{}' AND party_id = '{}'".format(
        memo.memo_number, memo.supplier_id, memo.party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    if len(data) == 0:
        print(True)
        return True
    return False


def get_id_by_memo_number(memo_number, supplier_id, party_id) -> int:
    """
    Get the memo_id using memo_number, supplier_id and party_id
    """
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from memo_entry where memo_number = {} AND supplier_id = {} AND party_id = {};".format(
        memo_number, supplier_id, party_id)

    print(query)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    print(data)
    return int(data[0][0])
