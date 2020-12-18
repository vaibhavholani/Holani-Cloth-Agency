from __future__ import annotations
from typing import List
from Database import db_connector
from Indivijuval import Supplier, Party, Bank, Transporter

db = db_connector.connect()
cursor = db.cursor()


def supplier_exist(supplier_name: str) -> bool:
    """
    Checks if the supplier exists in the database
    """
    query = "select name from supplier where name = '{}'".format(supplier_name)
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    return True


def party_exist(party_name: str) -> bool:
    """
    Checks if the supplier exists in the database
    """
    query = "select name from party where name = '{}'".format(party_name)
    cursor.execute(query)
    data = cursor.fetchall()
    if len(data) == 0:
        return False
    return True


def get_all_party_names() -> List[str]:
    """
    Get all party names returned in a List
    """
    query = "select name from party"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    return r_list


def get_party_name_by_id(party_id: int) -> str:
    """
    Get party name by ID
    """
    query = "select name from party where id = '{}';".format(party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_party_id_by_name(party_name: str) -> int:
    """
    Get party ID by name
    """
    query = "select id from party where name = '{}';".format(party_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_party_address_by_name(party_name: str) -> str:
    """
    Get the party address
    """
    query = "select address from party where name = '{}';".format(party_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_party_address_by_id(party_id: int) -> str:
    """
    Get the party address
    """
    query = "select address from party where name = '{}';".format(party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_all_supplier_names() -> List[str]:
    """
    Get all supplier names returned in a List
    """
    query = "select name from supplier"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    return r_list


def get_supplier_name_by_id(supplier_id: int) -> str:
    """
    Get supplier name by ID
    """
    query = "select name from supplier where id = '{}';".format(supplier_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_supplier_id_by_name(supplier_name: str) -> int:
    """
    Get supplier ID by name
    """
    query = "select id from supplier where name = '{}'".format(str(supplier_name))
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_supplier_address_by_name(supplier_name: str) -> str:
    """
    Get the supplier address
    """
    query = "select address from supplier where name = '{}';".format(supplier_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_supplier_address_by_id(supplier_id: int) -> str:
    """
    Get the supplier address
    """
    query = "select address from supplier where name = '{}';".format(supplier_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_bank_name_by_id(bank_id: int) -> str:
    """
    Get bank name by ID
    """
    query = "select name from bank where id = '{}';".format(bank_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_bank_id_by_name(bank_name: str) -> int:
    """
    Get bank ID by name
    """
    query = "select id from bank where name = '{}';".format(bank_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_bank_address_by_name(bank_name: str) -> str:
    """
    Get the bank address
    """
    query = "select address from bank where name = '{}';".format(bank_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_bank_address_by_id(bank_id: int) -> str:
    """
    Get the bank address
    """
    query = "select address from bank where name = '{}';".format(bank_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_transport_name_by_id(transport_id: int) -> str:
    """
    Get transport name by ID
    """
    query = "select name from transport where id = '{}';".format(transport_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_transport_id_by_name(transport_name: str) -> int:
    """
    Get transport ID by name
    """
    query = "select id from transport where name = '{}';".format(transport_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_transport_address_by_name(transport_name: str) -> str:
    """
    Get the transport address
    """
    query = "select address from transport where name = '{}';".format(transport_name)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]


def get_transport_address_by_id(transport_id: int) -> str:
    """
    Get the transport address
    """
    query = "select address from transport where name = '{}';".format(transport_id)
    cursor.execute(query)
    data = cursor.fetchall()
    return data[0][0]
