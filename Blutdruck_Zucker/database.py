import sqlite3


def connect():
    return sqlite3.connect("data_blood.db") # take care of working directory !


def store_data(connection, date, time, sys, dia, pulse, weight, sugar):
     with connection:
        connection.execute("INSERT INTO logfile (date, time, sys, dia, pulse, weight, sugar) VALUES (?, ?, ?, ?, ?, ?, ?)", (date, time, sys, dia, pulse, weight, sugar))
          # arguments(query, tuple of values)


