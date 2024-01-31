import sqlite3
from sqlite3 import Error

def try_connection(): 
    """ create a database connection to a SQLite database """
    conn = None
    isConnection = False
    try:
        conn = sqlite3.connect("backend/bin/test.db")
        isConnection = True
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return isConnection

file = "backend/bin/studentDB.db"
if try_connection(file):
    print("succeed")

def connect(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection established...")
    except Error as e:
        print(e)
    return conn

def disconnect(conn):
    try:
        conn.close()
    except Error as e:
        print(e)
    









