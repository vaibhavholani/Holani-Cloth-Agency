
from Database import online_db_connector
from Database import db_connector


def upload_individual() -> None:
    """
    Add all the suppliers and party to the online database
    """

    individual_list = ["supplier", "party", "bank", "Transport"]

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    for individual in individual_list:

        # Getting new data
        query = "select id, name, address from {} where last_update > CAST('{}' AS DATETIME)".format(individual,
                                                                                                    timestamp)
        local_cursor.execute(query)
        new_data = local_cursor.fetchall()

        sql = "INSERT INTO {} (id, name, address) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE " \
              "name = VALUES(name), address =VALUES(address)".format(individual)
        online_cursor.executemany(sql, new_data)

        online_db.commit()

    local_db.disconnect()
    online_db.disconnect()


def upload_register_entry() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select id, supplier_id, party_id, register_date, amount, " \
            "partial_amount, bill_number, status, d_amount," \
            " d_percent, gr_amount from register_entry where last_update > CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO register_entry (id, supplier_id, party_id, register_date, amount, " \
          "partial_amount, bill_number, status, " \
          "d_amount, d_percent, gr_amount) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" \
          "ON DUPLICATE KEY UPDATE status=VALUES(status), partial_amount=VALUES(partial_amount)," \
          " d_amount=VALUES(d_amount), d_percent=VALUES(d_percent), gr_amount=VALUES(gr_amount)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def upload_memo_entry() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select id, memo_number, supplier_id, party_id, register_date" \
            " from memo_entry where last_update > CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO memo_entry (id, memo_number, supplier_id, party_id, register_date)" \
          "VALUES (%s, %s, %s, %s, %s)" \
          "ON DUPLICATE KEY UPDATE memo_number=VALUES(memo_number), register_date=VALUES(register_date)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def upload_memo_payments() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select id, memo_id, bank_id, cheque_number from memo_payments where last_update > CAST('{}' AS DATETIME)" \
        .format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO memo_payments (id, memo_id, bank_id, cheque_number)" \
          "VALUES (%s, %s, %s, %s)" \
          "ON DUPLICATE KEY UPDATE memo_id=VALUES(memo_id), bank_id=VALUES(bank_id), " \
          "cheque_number=VALUES(cheque_number)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def upload_memo_bills() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select id, memo_id, bill_number, type, amount from memo_bills where last_update > " \
            "CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO memo_bills (id, memo_id, bill_number, type, amount)" \
          "VALUES (%s, %s, %s, %s, %s)" \
          "ON DUPLICATE KEY UPDATE memo_id=VALUES(memo_id), bill_number=VALUES(bill_number), type=VALUES(type), " \
          "amount=VALUES(amount)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def upload_gr_settle() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select supplier_id, party_id, start_date, end_date, settle_amount from gr_settle where last_update > " \
            "CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO gr_settle (supplier_id, party_id, start_date, end_date, settle_amount)" \
          "VALUES (%s, %s, %s, %s, %s)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def upload_account() -> None:
    """
    Add all the new and updated register entries to the online database
    """

    # Open a new connection
    local_db, local_cursor = db_connector.cursor()

    online_db = online_db_connector.connect()
    online_cursor = online_db.cursor()

    # get the last update timestamp
    query = "select updated_at from last_update"
    online_cursor.execute(query)
    timestamp = (online_cursor.fetchall())[0][0]

    # Getting new data
    query = "select supplier_id, party_id, partial_amount, gr_amount from supplier_party_account " \
            "where last_update > CAST('{}' AS DATETIME)".format(timestamp)
    local_cursor.execute(query)
    new_data = local_cursor.fetchall()

    sql = "INSERT INTO supplier_party_account (supplier_id, party_id, partial_amount, gr_amount)" \
          "VALUES (%s, %s, %s, %s)"
    online_cursor.executemany(sql, new_data)

    online_db.commit()
    local_db.disconnect()
    online_db.disconnect()


def update() -> None:
    """
    Update all and the put the new updated timestamp
    """
    upload_individual()
    upload_register_entry()
    upload_memo_entry()
    upload_memo_payments()
    upload_memo_bills()
    upload_gr_settle()
    upload_account()
    online_db_connector.update()


