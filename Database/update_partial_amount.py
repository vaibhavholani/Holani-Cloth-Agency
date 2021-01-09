from __future__ import annotations
from Database import db_connector, retrieve_partial_payment


def add_partial_amount(supplier_id: int, party_id: int, amount: int) -> None:
    """
    Add partial amount between a supplier and party
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    partial_amount = int(retrieve_partial_payment.get_partial_payment(supplier_id, party_id))
    amount += partial_amount

    query = "UPDATE supplier_party_account SET partial_amount = {} WHERE supplier_id = {} AND party_id = {}" \
        .format(amount, supplier_id, party_id)

    cursor.execute(query)
    db.commit()
    db.disconnect()


def use_partial_amount(supplier_id: int, party_id: int, amount: int) -> None:
    """
    Use partial amount between a supplier and party
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    partial_amount = int(retrieve_partial_payment.get_partial_payment(supplier_id, party_id))
    amount = partial_amount - amount
    if amount < 0:
        amount = 0
    query = "UPDATE supplier_party_account SET partial_amount = {} WHERE supplier_id = {} AND party_id = {}" \
        .format(amount, supplier_id, party_id)

    cursor.execute(query)
    db.commit()
    db.disconnect()
