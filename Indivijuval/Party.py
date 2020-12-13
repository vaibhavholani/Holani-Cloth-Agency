"""
=== Class Description ===
The file is supposed to represent a Party

"""
from __future__ import annotations


class Party:
    """
    The class represents a Party.

    name : The name  of the Party
    short_name: The short name of the Party
    address: The address of the Party.

    """

    def __init__(self, name: str, short_name: str, address: str):
        self.name = name
        self.short_name = short_name
        self.address = address


def create_party(name: str, short_name: str, address: str) -> Party:

    return Party(name, short_name, address)
