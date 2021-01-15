from __future__ import annotations
from Entities import RegisterEntry
from Database import db_connector, retrieve_register_entry


def update_register_entry_data(entry: RegisterEntry) -> None:
    """
    Update changes made to the register entry by a memo_entry
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    entry_id = retrieve_register_entry.get_register_entry_id(entry.supplier_id, entry.party_id, entry.bill_number)

    query = "UPDATE register_entry SET partial_amount = '{}', status = '{}', " \
            "d_amount = '{}', d_percent = '{}' WHERE id = {}"\
        .format(entry.part_payment, entry.status, entry.d_amount, entry.d_percent, entry_id)

    cursor.execute(query)
    db.commit()
    db.disconnect()
    db_connector.update()
