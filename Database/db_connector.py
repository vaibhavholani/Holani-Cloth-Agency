from __future__ import annotations
from typing import Tuple, List
import mysql.connector


def connect():
    """
    Provides a reference to the database and its cursor
    """
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hema9350544808",
        database="holani_cloth_agency")

    return mydb


def cursor() -> Tuple:
    """
    return the cursor and db connection
    """
    database = connect()
    # db_connection = database.connect()
    db_cursor = database.cursor()
    query = "set time_zone = '-07:00';"
    db_cursor.execute(query)
    database.commit()
    return database, db_cursor


def update() -> None:
    """
    Set the new timestamp
    """
    # Open a new connection
    local_db, local_cursor = cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    local_cursor.execute(query)
    local_timestamp = (local_cursor.fetchall())[0][0]

    # UPDATE it with the new one
    query = "UPDATE last_update SET updated_at = CURRENT_TIMESTAMP where updated_at = " \
            "CAST('{}' AS DATETIME);".format(local_timestamp)
    local_cursor.execute(query)

    local_db.commit()


def add_stack(query: str) -> None:
    """
    add a non-insert query into the database
    """
    # Open a new connection
    local_db, local_cursor = cursor()

    sql = '''INSERT INTO stack (query) VALUES (%s)'''
    val = (query,)
    local_cursor.execute(sql, val)
    local_db.commit()
    local_db.disconnect()
    update()


def add_stack_val(query: str, val: Tuple) -> None:
    """
    add an insert query to the stack
    """
    # Open a new connection
    local_db, local_cursor = cursor()

    sql = "INSERT INTO stack (query, val) VALUES (%s, %s)"
    value = (query, str(val))
    local_cursor.execute(sql, value)
    local_db.commit()
    local_db.disconnect()
    update()


def add_stack_val_multiple(query: str, val: List[Tuple]) -> None:
    """
    add insert query with multiple values
    """
    # Open a new connection
    local_db, local_cursor = cursor()

    sql = "INSERT INTO stack (query, val) VALUES (%s, %s)"
    value = (query, str(val))
    local_cursor.execute(sql, value)
    local_db.commit()
    local_db.disconnect()
    update()

