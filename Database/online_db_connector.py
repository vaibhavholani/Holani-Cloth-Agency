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