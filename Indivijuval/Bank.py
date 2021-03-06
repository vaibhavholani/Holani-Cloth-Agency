"""
=== Class Description ===
The file is supposed to represent a Bank

"""
from __future__ import annotations


class Bank:
    """
    The class represents a Bank.

    name : The name  of the Bank
    address: The address of the Bank.

    """

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


def create_bank(name: str, address: str) -> Bank:
    return Bank(name, address)
