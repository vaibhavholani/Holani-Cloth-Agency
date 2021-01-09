from __future__ import annotations
from Database import db_connector
from Entities import MemoEntry, Grentry


def insert_gr(entry: MemoEntry) -> None:
    """
    Inserts gr amount between the account of supplier and party.
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    sql = "INSERT INTO supplier_party_account (supplier_id, party_id, gr_amount) " \
          "VALUES (%s, %s, %s)"
    val = (entry.supplier_id, entry.party_id, entry.amount)

    cursor.execute(sql, val)
    db.commit()

    sql = "INSERT INTO gr_entry (supplier_id, party_id, register_date, amount) " \
          "VALUES (%s, %s, %s, %s)"
    val = (entry.supplier_id, entry.party_id, entry.date, entry.amount)

    cursor.execute(sql, val)
    db.commit()

    db.disconnect()


def settle_gr(entry: Grentry) -> None:
    """
    Use the the pending gr amount to settle the account between a party and supplier
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    sql = "INSERT INTO gr_settle (supplier_id, party_id, settle_amount, start_date, end_date) " \
          "VALUES (%s, %s, %s, %s, %s)"
    val = (entry.supplier_id, entry.party_id, entry.amount, entry.start_date, entry.end_date)

    cursor.execute(sql, val)
    db.commit()

    db.disconnect()
