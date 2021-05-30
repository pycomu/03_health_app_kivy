import sqlite3


def connect():
    return sqlite3.connect("./kivy/template/health_app.db") # take care of working directory !


def read_pin_account(connection):
    with connection:
        return connection.execute("SELECT account_pin FROM account").fetchone() # read out account_pin


# def store_account(connection, account_name, account_pin, account_email):
#      with connection:
#         connection.execute("INSERT INTO account (account_name, account_pin, account_email) VALUES (?, ?, ?)", (account_name, account_pin, account_email))           # arguments(query, tuple of values)
        




