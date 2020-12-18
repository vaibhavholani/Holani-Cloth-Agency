from __future__ import annotations
from Database import db_connector
from Database import retrieve_indivijual, retrieve_memo_entry
from Entities import MemoEntry, MemoBill


def insert_memo_entry(entry: MemoEntry) -> None:

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(entry.supplier_name))
    party_id = int(retrieve_indivijual.get_party_id_by_name(entry.party_name))

    sql = "INSERT INTO memo_entry (supplier_id, party_id, register_date, memo_number) " \
          "VALUES (%s, %s, %s, %s)"
    val = (supplier_id, party_id, str(entry.date), entry.memo_number)

    cursor.execute(sql, val)
    db.commit()
    db.disconnect()


def insert_memo_bills(entry: MemoBill) -> None:
    """
    Insert all the bills attached to the same memo number.
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    sql = "INSERT INTO memo_bills (memo_id, bill_number, type, amount) " \
          "VALUES (%s, %s, %s, %s)"
    val = (entry.memo_id, entry.memo_number, entry.type, entry.amount)

    cursor.execute(sql, val)
    db.commit()
    db.disconnect()

