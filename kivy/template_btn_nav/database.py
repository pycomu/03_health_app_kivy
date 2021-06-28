import sqlite3

dbfile_path_name = "./health_app.db" # take care of working directory !

def connect():
    try:
        connect = sqlite3.connect(dbfile_path_name) # Connect to database.
        print("Database connection established.")

    except sqlite3.DatabaseError as e:
        print("Database connection unsuccessful.") # Confirm unsuccessful connection and quit.
        quit()
  
    return connect


def read_pin_account(connection):
    with connection:
        return connection.execute("SELECT account_pin FROM account").fetchone() # read out account_pin


def store_account(connection, account_name, account_pin, account_email):
     with connection:
        connection.execute("INSERT INTO account (account_name, account_pin, account_email) VALUES (?, ?, ?)", (account_name, account_pin, account_email))           # arguments(query, tuple of values)

def store_child_info(connection, child_first_name, child_last_name, child_bday, child_gender):
     with connection:
        connection.execute("INSERT INTO child (child_first_name, child_last_name, child_bday, child_gender) VALUES (?, ?, ?, ?)", (child_first_name, child_last_name, child_bday, child_gender))       

