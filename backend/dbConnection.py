import sqlite3
from sqlite3 import Error

file = "backend/bin/studentDB.db"

def try_connection(): 
    """ create a database connection to a SQLite database """
    conn = None
    isConnection = False
    try:
        conn = sqlite3.connect(file)
        isConnection = True
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
    return isConnection

if try_connection():
    print("test succeed")

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
        print("Connection closed.")
    except Error as e:
        print(e)

def request(conn, query: str):
    try:
        c = conn.cursor()
        return c.execute(query)
    except Error as e:
        pass
    
    return None;









