from __future__ import annotations
from Database import db_connector
from Database import retrieve_indivijual, retrieve_memo_entry
from Entities import MemoEntry, MemoBill


def insert_memo_entry(entry: MemoEntry) -> None:

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    sql = "INSERT INTO memo_entry (supplier_id, party_id, register_date, memo_number) " \
          "VALUES (%s, %s, %s, %s)"
    val = (entry.supplier_id, entry.party_id, str(entry.date), entry.memo_number)

    cursor.execute(sql, val)
    db.commit()

    db.disconnect()


def insert_memo_payemts(entry: MemoEntry) -> None:
    """
    Add the memo paymentns for the given memo_entry
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    memo_id = retrieve_memo_entry.get_id_by_memo_number(entry.memo_number, entry.supplier_id, entry.party_id)

    payment_list = [(memo_id, retrieve_indivijual.get_bank_id_by_name(e[0]), int(e[1])) for e in entry.payment_info]

    sql = "INSERT INTO memo_payments (memo_id, bank_id, cheque_number) " \
          "VALUES (%s, %s, %s)"

    cursor.executemany(sql, payment_list)
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
