from __future__ import annotations
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


def update() -> None:
    """
    Set the new timestamp
    """
    # Local Database
    local_db = connect()
    local_cursor = local_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    local_cursor.execute(query)
    local_timestamp = (local_cursor.fetchall())[0][0]

    # UPDATE it with the new one
    query = "UPDATE last_update SET updated_at = CURRENT_TIMESTAMP where updated_at = " \
            "CAST('{}' AS DATETIME);".format(local_timestamp)
    local_cursor.execute(query)

    local_db.commit()
