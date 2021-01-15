from __future__ import annotations
from Database import db_connector, retrieve_gr


def add_gr_amount(supplier_id: int, party_id: int, amount: int) -> None:
    """
    Add partial amount between a supplier and party
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    gr_amount = int(retrieve_gr.get_gr(supplier_id, party_id))
    amount += gr_amount

    query = "UPDATE supplier_party_account SET gr_amount = {} WHERE supplier_id = {} AND party_id = {}" \
        .format(amount, supplier_id, party_id)

    cursor.execute(query)
    db.commit()
    db.disconnect()
    db_connector.update()
