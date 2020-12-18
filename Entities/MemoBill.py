"""
==== Description ====
This class is used to represent a bill in a memo_entry.

"""

from __future__ import annotations
from typing import List
import datetime
from Database import insert_memo_entry
from Entities import RegisterEntry


class MemoBill:

    """Create a bill for a memo."""

    def __init__(self, memo_id: int, memo_number: int, amount: int, memo_type: str) -> None:

        self.memo_id = memo_id
        self.memo_number = memo_number
        self.amount = amount
        self.type = memo_type


def call(memo_id: int, memo_number: int, amount: int, memo_type: str) -> None:
    """
    Create a memo bill and insert it into the database.
    """
    bill = MemoBill(memo_id, memo_number, amount, memo_type)
    insert_memo_entry.insert_memo_bills(bill)

