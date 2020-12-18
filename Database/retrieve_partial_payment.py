from __future__ import annotations
from Database import db_connector


db = db_connector.connect()
cursor = db.cursor()


def get_partial_payment(supplier_id: int, party_id: int) -> int:
    """
    Returns the partial payment without bill between the party and supplier.
    """

    query = "select id from supplier_party_account supplier_id = '{}' AND party_id = '{}'".format(
        supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0:
        return 0
    return int(data[0][0])