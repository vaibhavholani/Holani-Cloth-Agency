from __future__ import annotations
from Database import db_connector
from Indivijuval import Supplier, Party, Bank, Transporter

db = db_connector.connect()
cursor = db.cursor()


def insert_supplier(supplier: Supplier) -> None:
    sql = "INSERT INTO supplier (name, address) VALUES (%s, %s)"
    val = (supplier.name, supplier.address)

    cursor.execute(sql, val)
    db.commit()


def insert_party(party: Party) -> None:
    sql = "INSERT INTO party (name, address) VALUES (%s, %s)"
    val = (party.name, party.address)

    cursor.execute(sql, val)
    db.commit()


def insert_bank(bank: Bank) -> None:
    sql = "INSERT INTO bank (name, address) VALUES (%s, %s)"
    val = (bank.name, bank.address)

    cursor.execute(sql, val)
    db.commit()


def insert_transporter(transporter: Transporter) -> None:
    sql = "INSERT INTO Transport (name, address) VALUES (%s, %s)"
    val = (transporter.name, transporter.address)

    cursor.execute(sql, val)
    db.commit()
