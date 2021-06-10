import sqlite3


def connect():
    return sqlite3.connect("./health_app.db") # take care of working directory !


def read_pin_account(connection):
    with connection:
        return connection.execute("SELECT account_pin FROM account").fetchone() # read out account_pin


def store_account(connection, account_name, account_pin, account_email):
     with connection:
        connection.execute("INSERT INTO account (account_name, account_pin, account_email) VALUES (?, ?, ?)", (account_name, account_pin, account_email))           # arguments(query, tuple of values)

def store_child_info(connection, child_first_name, child_last_name, child_bday, child_gender):
     with connection:
        connection.execute("INSERT INTO child (child_first_name, child_last_name, child_bday, child_gender) VALUES (?, ?, ?, ?)", (child_first_name, child_last_name, child_bday, child_gender))       

