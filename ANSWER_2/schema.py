# Alex Canizales - schema.py

import sqlite3
import os


DIRNAME = os.path.dirname(__file__)
DBFILE  = "database.db"


def schema(dbpath=os.path.join(DIRNAME, DBFILE)):
    
    CREATESQL_STUDENTS = """CREATE TABLE students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(255),
        last_name VARCHAR(255) NOT NULL,
        gpa FLOAT,
        campus_id INTEGER,
        FOREIGN KEY ("campus_id") REFERENCES campus(id));"""

    CREATESQL_CAMPUS = """CREATE TABLE campus(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city VARCHAR(64) NOT NULL,
        state VARCHAR(64));"""

    DROPSQL_STUDENTS = "DROP TABLE IF EXISTS students;"
    DROPSQL_CAMPUS = "DROP TABLE IF EXISTS campus;"

    with sqlite3.connect(dbpath) as connection:
        cursor = connection.cursor()
        cursor.execute(DROPSQL_STUDENTS)
        cursor.execute(DROPSQL_CAMPUS)
        cursor.execute(CREATESQL_STUDENTS)
        cursor.execute(CREATESQL_CAMPUS)


if __name__ == "__main__":
    schema()