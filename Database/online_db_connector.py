from __future__ import annotations
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


def update() -> None:
    """
    Set the new timestamp
    """
    # Local Database
    online_db = connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    local_timestamp = (online_cursor.fetchall())[0][0]

    # UPDATE it with the new one
    query = "UPDATE last_update SET updated_at = CURRENT_TIMESTAMP where updated_at = " \
            "CAST('{}' AS DATETIME);".format(local_timestamp)
    online_cursor.execute(query)
    online_db.commit()
