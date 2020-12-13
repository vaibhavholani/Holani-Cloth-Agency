"""
==== Description ====
This class is used to represent a memo entry.

"""

from __future__ import annotations
from typing import List
import datetime
from Database import Lists
from Entities import RegisterEntry


class MemoEntry:

    """
    A class that represents a memo entry

    ===Attributes===

    amount: the amount for which the party has received an order
    date: the date

    """
    memo_number: int
    supplier_name: str
    party_name: str
    amount: int
    date: datetime
    selected_bills: List

    def __init__(self, memo_number: int, amount: int, party: str, supplier: str,
                 date: str, selected_bills: List[RegisterEntry], mode: str) -> None:

        self.memo_number = memo_number
        self.supplier_name = supplier
        self.party_name = party
        self.amount = amount
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.mode = mode
        self.selected_bills = Lists.re_bill_numbers(self.supplier_name, self.party_name, selected_bills)

    def unique_memo_check(self):
        pass

    def full_payment(self):

        for bills in self.selected_bills:
            bills.status = "F"
            bills.payment_date.append(self.date)

    def partial_payment_bill(self):

        for bills in self.selected_bills:
            bills.status = "P"
            bills.part_payment = self.amount
            bills.payment_date.append(self.date)

    def partial_payment_random(self):

        Lists.insert_partial_data(self.supplier_name, self.party_name, self.amount)

    def goods_return(self):

        for bills in self.selected_bills:
            bills.status = "P"
            bills.gr_amount = self.amount
            bills.amount = bills.amount - self.amount
            bills.gr_date.append(self.date)


def call_full(memo_number: int, supplier: str, party: str, amount: int,
              date: str,
              selected_bills: List[RegisterEntry]) -> None:

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Full")
    memo.full_payment()


def call_partial_bill(memo_number: int, supplier: str, party: str, amount: int,
                      date: str,
                      selected_bills: List[RegisterEntry]) -> None:

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Part Bill")
    memo.partial_payment_bill()


def call_partial_random(memo_number: int, supplier: str, party: str,
                        amount: int, date: str,
                        selected_bills: List[RegisterEntry]) -> None:
    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Part Random")
    memo.partial_payment_random()


def call_gr(memo_number: int, supplier: str, party: str, amount: int, date: str,
            selected_bills: List[RegisterEntry]) -> None:

    memo = MemoEntry(memo_number, amount, party, supplier, date, selected_bills, "Good Return")
    memo.goods_return()
