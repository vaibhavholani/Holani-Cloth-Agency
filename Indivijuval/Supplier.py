"""
=== Class Description ===
The file is supposed to represent a Supplier

"""
from __future__ import annotations


class Supplier:
    """
    The class represents a supplier.

    name : The name  of the Supplier
    short_name: The short name of the Supplier
    address: The address of the supplier.

    """

    def __init__(self, name: str, short_name: str, address: str) -> None:

        self.name = name
        self.short_name = short_name
        self.address = address


def create_supplier(name: str, short_name: str, address: str) -> Supplier:
    """
    Create and return a Supplier

    :param name: The name  of the Supplier
    :param short_name: The short name of the Supplier
    :param address: The address of the supplier.
    :return: Supplier
    """
    return Supplier(name, short_name, address)

