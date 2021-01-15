from __future__ import annotations
from Database import db_connector
from Entities import MemoEntry


def insert_partial_payment(entry: MemoEntry) -> None:
    """
    Inserts partial payment between the account of supplier and party.
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    sql = "INSERT INTO supplier_party_account (supplier_id, party_id, partial_amount) " \
          "VALUES (%s, %s, %s)"
    val = (entry.supplier_id, entry.party_id, entry.amount)

    cursor.execute(sql, val)
    db.commit()
    db.disconnect()
    db_connector.update()
