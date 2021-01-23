from __future__ import annotations
from typing import List
from Database import db_connector
from Indivijuval import Supplier, Party, Bank, Transporter


def supplier_exist(supplier_name: str) -> bool:
    """
    Checks if the supplier exists in the database
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from supplier where name = '{}'".format(supplier_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    if len(data) == 0:
        return False
    return True


def party_exist(party_name: str) -> bool:
    """
    Checks if the supplier exists in the database
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from party where name = '{}'".format(party_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    if len(data) == 0:
        return False
    return True


def get_all_party_names() -> List[str]:
    """
    Get all party names returned in a List
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from party"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    db.disconnect()
    return r_list


def get_all_bank_names() -> List[str]:
    """
    Get all bank names returned in a List
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from bank"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    db.disconnect()
    return r_list


def get_all_party_id() -> List[int]:
    """
    Get all party ids returned in a List
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from party"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    db.disconnect()
    return r_list


def get_all_supplier_id() -> List[int]:
    """
    Get all supplier ids returned in a List
    """

    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from supplier"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    db.disconnect()
    return r_list


def get_party_name_by_id(party_id: int) -> str:
    """
    Get party name by ID
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()
    print(party_id)
    query = "select name from party where id = '{}';".format(party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_party_id_by_name(party_name: str) -> int:
    """
    Get party ID by name
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()
    use_name = ""
    for chars in party_name:
        if chars in ["'", '"']:
            use_name = use_name + "%"
        else:
            use_name = use_name + chars
    query = "select id from party where name LIKE '{}';".format(use_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_party_address_by_name(party_name: str) -> str:
    """
    Get the party address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    use_name = ""
    for chars in party_name:
        if chars in ["'", '"']:
            use_name = use_name + "%"
        else:
            use_name = use_name + chars
    query = "select address from party where name LIKE '{}';".format(use_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_party_address_by_id(party_id: int) -> str:
    """
    Get the party address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from party where name = '{}';".format(party_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_all_supplier_names() -> List[str]:
    """
    Get all supplier names returned in a List
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from supplier"
    cursor.execute(query)
    data = cursor.fetchall()
    r_list = [x[0] for x in data]
    db.disconnect()
    return r_list


def get_supplier_name_by_id(supplier_id: int) -> str:
    """
    Get supplier name by ID
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from supplier where id = '{}';".format(supplier_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_supplier_id_by_name(supplier_name: str) -> int:
    """
    Get supplier ID by name
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()
    use_name = ""
    for chars in supplier_name:
        if chars in ["'", '"']:
            use_name = use_name + "%"
        else:
            use_name = use_name+chars

    query = "select id from supplier where name LIKE '{}'".format(str(use_name))
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_supplier_address_by_name(supplier_name: str) -> str:
    """
    Get the supplier address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from supplier where name = '{}';".format(supplier_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_supplier_address_by_id(supplier_id: int) -> str:
    """
    Get the supplier address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from supplier where name = '{}';".format(supplier_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_bank_name_by_id(bank_id: int) -> str:
    """
    Get bank name by ID
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from bank where id = '{}';".format(bank_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_bank_id_by_name(bank_name: str) -> int:
    """
    Get bank ID by name
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from bank where name = '{}';".format(bank_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_bank_address_by_name(bank_name: str) -> str:
    """
    Get the bank address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from bank where name = '{}';".format(bank_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_bank_address_by_id(bank_id: int) -> str:
    """
    Get the bank address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from bank where name = '{}';".format(bank_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_transport_name_by_id(transport_id: int) -> str:
    """
    Get transport name by ID
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select name from transport where id = '{}';".format(transport_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_transport_id_by_name(transport_name: str) -> int:
    """
    Get transport ID by name
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select id from transport where name = '{}';".format(transport_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_transport_address_by_name(transport_name: str) -> str:
    """
    Get the transport address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from transport where name = '{}';".format(transport_name)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_transport_address_by_id(transport_id: int) -> str:
    """
    Get the transport address
    """
    # Open a new connection
    db = db_connector.connect()
    cursor = db.cursor()

    query = "select address from transport where name = '{}';".format(transport_id)
    cursor.execute(query)
    data = cursor.fetchall()
    db.disconnect()
    return data[0][0]


def get_party_ids_by_list(party_names: List[str]) -> List[int]:
    """
    Get the id of selected parties by thier names
    """

    id_list = []

    for names in party_names:
        id_list.append(get_party_id_by_name(names))

    return id_list


def get_supplier_ids_by_list(supplier_names: List[str]) -> List[int]:
    """
    Get the id of selected supplier by thier names
    """

    id_list = []

    for names in supplier_names:
        id_list.append(get_supplier_id_by_name(names))

    return id_list
