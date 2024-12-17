# need to pip install mysql-connector-python

import mysql.connector

def connect_to_db():
    """
    Connect to OpenEMR MySQL database.
    """
    try:
        conn = mysql.connector.connect(
            host="your_db_host", # probably localhost
            user="your_db_user",
            password="your_db_pass",
            database="openemr" # OpenEMR database name
        )
        print("Connected to database.")
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to database: {e}")
        raise
