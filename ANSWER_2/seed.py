# Alex Canizales - seed.py

# QUESTION: Write a SQL SELECT statement to get the last names of all students
# in New York with a GPA over 3.0. Do not select based on an integer foreign key, 
# use a join and select by the city name.
#
# ANSWER: SELECT last_name 
#           FROM students 
#           JOIN campus 
#           ON students.campus_id=campus.id
#           WHERE students.gpa > 3.0 AND campus.city="New York";


import sqlite3
import os
from schema import schema


DIRNAME = os.path.dirname(__file__)
DBFILE  = "database.db"
DBPATH  = os.path.join(DIRNAME, DBFILE)


def insert_students(first_name, last_name, gpa, campus_id):
    """ inserts a new row into the database students table and sets id """
    with sqlite3.connect(DBPATH) as connection: 
        cursor = connection.cursor()
        INSERTSQL = """INSERT INTO students(first_name, last_name, gpa, campus_id) 
                    VALUES (:first_name, :last_name, :gpa, :campus_id);"""
        values = {
            "first_name": first_name,
            "last_name": last_name,
            "gpa": gpa,
            "campus_id": campus_id
            }
        try: 
            cursor.execute(INSERTSQL, values)
            id = cursor.lastrowid      
        except sqlite3.IntegrityError:
            raise ValueError("is not set or an id for this student already exists")


def insert_campus(city, state):
    """ inserts a new row into the database campus table and sets id """
    with sqlite3.connect(DBPATH) as connection: 
        cursor = connection.cursor()
        INSERTSQL = """INSERT INTO campus(city, state) 
                    VALUES (:city, :state);"""
        values = {
            "city": city,
            "state": state
            }
        try: 
            cursor.execute(INSERTSQL, values)
            id = cursor.lastrowid      
        except sqlite3.IntegrityError:
            raise ValueError("is not set or an id for this campus already exists")


def average_gpa(city, state):
    """ return average gpa from students table for the given database"""
    with sqlite3.connect(DBPATH) as connection:
        SELECTSQL = """SELECT gpa 
                        FROM students 
                        JOIN campus
                        ON students.campus_id=campus.id
                        WHERE campus.city=:city AND campus.state=:state;"""
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        values = {
            "city": city,
            "state": state
            }
        cursor.execute(SELECTSQL, values)
        list_gpas = cursor.fetchall()
        all_gpas = []
        for gpa in list_gpas:
            all_gpas.append((gpa[0]))
        avg_gpa = sum(all_gpas)/len(all_gpas)
        return avg_gpa

# SELECT last_name 
#    FROM students 
#    JOIN campus 
#    ON students.campus_id=campus.id
#    WHERE students.gpa > 3.0 AND campus.city="New York";

schema()

insert_campus("New York", "NY")
insert_campus("Houston", "TX")

insert_students("Lockett", "Walker", 3.1, 1)
insert_students("Coleman", "Casey", 2.7, 1)
insert_students("Kilome", "Franklyn", 3.8, 1)
insert_students("Santiago", "Hecton", 2.9, 1)

insert_students("Valdez", "Framber", 3.9, 2)
insert_students("Peacock", "Brad", 2.8, 2)
insert_students("Guduan", "Reymin", 3.5, 2)
insert_students("Cole", "Gerrit", 3.0, 2)

ny_gpa = average_gpa("New York", "NY")
print("New York campus GPA:", ny_gpa)
houston_gpa = average_gpa("Houston", "TX")
print("Houston campus GPA:", houston_gpa)