from __future__ import annotations
from typing import List, Tuple
from Database import db_connector, online_db_connector


def query_execute(data: List[Tuple], db_cursor):
    """
    execute all queries with the given cursor
    """
    for queries in data:
        if queries[1] == " ":
            db_cursor.execute(queries[0])
        elif queries[1][0] == "(":
            tuple_string = queries[1]
            tuple_string = tuple_string[1:-1]
            val = tupify(tuple_string)
            db_cursor.execute(queries[0], val)
        else:
            execute_multiple(queries[0], queries[1], db_cursor)

        sql = "INSERT INTO stack(query, val) VALUES (%s, %s)"
        db_cursor.execute(sql, (queries[0], queries[1]))


def tupify(tuple_string: str) -> Tuple:
    """
    converts "'a','b'" or "[('a', 'b')]" in the correct tuple format
    """
    tuple_string = tuple_string.replace("'", "")
    tuple_string = tuple_string.replace("(", "")
    tuple_string = tuple_string.replace(")", "")
    tuple_list = tuple_string.split(",")
    tuple_list_final = [x.strip() for x in tuple_list]
    val = tuple(tuple_list_final)
    return val


def execute_multiple(query: str, val: str, db_cursor) -> None:
    """
    execute the queries with multiple insert
    """
    tuple_list = (val[1:-1]).split("),")
    val = []
    for tups in tuple_list:
        val.append(tupify(tups))

    db_cursor.executemany(query, val)


def update_online() -> None:
    """
    take the queries from the offline stack and execute it to make changes into the online database
    """

    local_database, local_cursor = db_connector.cursor()
    online_database, online_cursor = online_db_connector.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    query = "select query, val from stack where updated_at >= CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    data = local_cursor.fetchall()

    query_execute(data, online_cursor)

    online_database.commit()
    online_db_connector.update()


def download_online() -> None:
    """
    take the queries from the offline stack and execute it to make changes into the online database
    """

    local_database, local_cursor = db_connector.cursor()
    online_database, online_cursor = online_db_connector.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    local_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    query = "select query, val from stack where updated_at >= CAST('{}' AS DATETIME)".format(timestamp)
    online_cursor.execute(query)
    data = online_cursor.fetchall()

    query_execute(data, local_cursor)

    local_database.commit()
    db_connector.update()
