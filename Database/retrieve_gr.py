from __future__ import annotations
from Database import db_connector
import datetime


def get_gr(supplier_id: int, party_id: int) -> int:
    """
    Returns the gr_amount without bill between the party and supplier.
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select gr_amount from supplier_party_account where supplier_id = '{}' AND party_id = '{}'".format(
        supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()

    db.disconnect()

    if len(data) == 0:
        return 0
    return int(data[0][0])


def get_usable_gr(supplier_id: int, party_id: int) -> int:
    """
    Gets the usable gr_amount
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select SUM(settle_amount) from gr_settle where supplier_id = '{}' AND party_id = '{}'".format(
        supplier_id, party_id)
    cursor.execute(query)
    data = cursor.fetchall()

    db.disconnect()

    if data[0][0] is None:
        return get_gr(supplier_id, party_id)
    else:
        return get_gr(supplier_id, party_id) - int(data[0][0])


def get_gr_between_dates(supplier_id: int, party_id: int, start_date: str, end_date: str) -> int:
    """
    Get the gr_between dates used to settle the account
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    start_date = str(datetime.datetime.strptime(start_date, "%d/%m/%Y"))
    end_date = str(datetime.datetime.strptime(end_date, "%d/%m/%Y"))

    query = "select SUM(settle_amount) from gr_settle where " \
            "party_id = '{}' AND supplier_id = '{}' AND " \
            "start_date >= '{}' AND end_date <= '{}';".format(party_id, supplier_id, start_date, end_date)

    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    if data[0][0] is None or len(data) == 0:
        return -1
    return data[0][0]
