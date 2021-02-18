from __future__ import annotations
from typing import Tuple
import mysql.connector


def connect():
    """
    Provides a reference to the online database
    """
    mydb = mysql.connector.connect(
        host="162.241.224.140",
        user="iobxgumy_vaibhav",
        password="Hema9350544808",
        database="iobxgumy_holani_cloth_agency")

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


def execute_stack(query: str) -> None:
    """
    execute a query on the online database
    """
    # Online Database
    online_db = connect()
    online_cursor = online_db.cursor()
    online_cursor.execute(query)


def update() -> None:
    """
    Set the new timestamp
    """
    online_database, online_cursor = cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    local_timestamp = (online_cursor.fetchall())[0][0]

    # UPDATE it with the new one
    query = "UPDATE last_update SET updated_at = CURRENT_TIMESTAMP where updated_at = " \
            "CAST('{}' AS DATETIME);".format(local_timestamp)
    online_cursor.execute(query)
    online_database.commit()
