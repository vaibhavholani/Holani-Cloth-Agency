from __future__ import annotations
from Entities import RegisterEntry, MemoEntry
from typing import List, Optional

data_store = [[[]]]

memo_store = [[[]]]

partial_data_store = [[[0]]]


supplier_names = ["saitax"]

party_names = ["samunder"]


def retrieve_data(supplier_name: str, party_name: str)-> List[RegisterEntry]:
    """
    Returns a list of all Register Entries between a supplier and a party.

    """

    supplier_index = supplier_names.index(supplier_name)
    party_index = party_names.index(party_name)

    return memo_store[supplier_index][party_index]


def retrieve_memo_data(supplier_name: str, party_name: str)-> List[RegisterEntry]:
    """
    Returns a list of all Memo Entries between a supplier and a party.

    """

    supplier_index = supplier_names.index(supplier_name)
    party_index = party_names.index(party_name)

    return memo_store[supplier_index][party_index]


def retrieve_partial_data(supplier_name: str, party_name: str)-> List[RegisterEntry]:
    """
    Returns a list of all Partial Entries between a supplier and a party without
    a bill number.
    """

    supplier_index = supplier_names.index(supplier_name)
    party_index = party_names.index(party_name)

    return partial_data_store[supplier_index][party_index]


def insert_data(entry: RegisterEntry)-> None:
    """
    Inserts Register Entries into the database.

    :param entry:
    :return:
    """

    supplier = entry.supplier_name
    party = entry.party_name
    all_entries = retrieve_data(supplier, party)
    all_entries.append(entry)


def insert_memo_data(entry: MemoEntry) -> None:
    """
        Inserts Memo Entries into the database.

    :param entry:
    :return:
    """
    supplier = entry.supplier_name
    party = entry.party_name
    all_entries = retrieve_memo_data(supplier, party)
    all_entries.append(entry)


def insert_partial_data(supplier_name: str, party_name: str, amount: int):
    """
    Inserts Partial Entries into the database.

    """
    all_entries = retrieve_partial_data(supplier_name, party_name)
    if len(all_entries) == 0:
        all_entries.append(amount)
    else:
        all_entries[0] += amount


def use_partial_amount(supplier_name: str, party_name: str, amount: int):
    """
        Uses the partial amount between two parties
    """
    all_entries = retrieve_partial_data(supplier_name, party_name)
    if len(all_entries) != 0:
        all_entries[0] -= amount


def bill_number_list(supplier_name: str, party_name: str) -> List[int]:
    """
    Returns a list of all Register Entries' bill numbers between a supplier and a party.

    """
    all_entries = retrieve_data(supplier_name, party_name)

    return [re.bill_number for re in all_entries]


def re_bill_numbers(supplier_name: str, party_name: str, billnumbers: List[int])\
        -> List[Optional]:
    """
     Returns a list of all Register Entries with  bill numbers in input list
     between a supplier and a party.

    :param supplier_name:
    :param party_name:
    :param billnumbers:
    :return:
    """

    all_entries = retrieve_data(supplier_name, party_name)
    return [re for re in all_entries if re.bill_number in billnumbers]










