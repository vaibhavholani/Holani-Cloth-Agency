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


