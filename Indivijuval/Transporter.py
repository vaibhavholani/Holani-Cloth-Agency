"""
=== Class Description ===
The file is supposed to represent a Transporter

"""
from __future__ import annotations


class Transporter:
    """
    The class represents a Transporter.

    name : The name  of the Transporter
    address: The address of the Transporter.

    """

    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address


def create_transporter(name: str, address: str) -> Bank:
    return Transporter(name, address)
