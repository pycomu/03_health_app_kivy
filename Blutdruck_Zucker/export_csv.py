import sqlite3
import csv

try:
    # Connect to database.
    connect = sqlite3.connect("./Blutdruck_Zucker/data_blood.db")
    print("Database connection established.")

except sqlite3.DatabaseError as e:

    # Confirm unsuccessful connection and quit.
    print("Database connection unsuccessful.")
    quit()

# Cursor to execute query.
cursor = connect.cursor()

# SQL to select data from the person table.
sqlSelect = "SELECT date, time, sys, dia, pulse, weight, sugar FROM logfile"

try:

    # Execute query.
    cursor.execute(sqlSelect)

    # Fetch the data returned.
    results = cursor.fetchall()

    # Extract the table headers.
    headers = [i[0] for i in cursor.description]

    # Open CSV file for writing.
    # csvFile = csv.writer(open("./Blutdruck_Zucker/data_blood.csv", 'w', newline=''),
    #                         delimiter=',', lineterminator='\r\n',
    #                         quoting=csv.QUOTE_ALL, escapechar='\\')

    csvFile = csv.writer(open("./Blutdruck_Zucker/data_blood.csv", 'w', newline=''),
                            delimiter=',', lineterminator='\r\n', escapechar='\\')                        

    # Add the headers and data to the CSV file.
    csvFile.writerow(headers)
    csvFile.writerows(results)

    # Message stating export successful.
    print("Data export successful.")

except sqlite3.DatabaseError as e:

    # Message stating export unsuccessful.
    print("Data export unsuccessful.")
    quit()

finally:

    # Close database connection.
    connect.close()