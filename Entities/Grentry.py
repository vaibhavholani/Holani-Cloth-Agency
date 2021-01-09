"""
==== Description ====
This class is used to represent a register entry. A register entry is made when
the bill for an order is received.

"""

from __future__ import annotations
from Database import retrieve_indivijual, insert_gr
from typing import List
import datetime


class GrEntry:

    """
    A class that represents a register entry


    ===Attributes===

    bill_number: a unique number that links a RegisterEntry to a MemoEntry
    amount: the amount for which the party has received an order
    date: the date when the bill is received
    supplier: the full name of the supplier
    party: the full name of the party

    """

    def __init__(self, amount: int, supplier: str, party: str,
                 start_date: str, end_date: str) -> None:

        self.amount = amount
        self.party_name = party
        self.supplier_name = supplier
        self.supplier_id = int(retrieve_indivijual.get_supplier_id_by_name(self.supplier_name))
        self.party_id = int(retrieve_indivijual.get_party_id_by_name(self.party_name))
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
        self.end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")


def call(amount: int, supplier: str, party: str, start_date: str, end_date: str) -> GrEntry:
    entry = GrEntry(amount, supplier, party, start_date, end_date)
    # Call the add function here
    insert_gr.settle_gr(entry)
    return entry








