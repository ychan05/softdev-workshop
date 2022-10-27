#Luigi (he/they):: Yat Long Chan, Brian Wang
#SoftDev pd 8
#K18: (Python+SQLite)3 Colllab: A Mare Widge Made in Hebben :: Using python to populate a SQLite3 database from a csv file
#2022-10-26
#time spent: 0.8 hours


import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
db.execute("DROP TABLE if exists students")
db.execute("DROP TABLE if exists courses;")


#def courses_to_db():
with open("courses.csv", "r") as f:
    reader = csv.DictReader(f)
    c.execute("CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);")
    for row in reader:
        c.execute(f'INSERT INTO courses VALUES("{row.get("code")}", {row.get("mark")}, {row.get("id")});')

#def students_to_db():
with open("students.csv", "r") as f :
    reader = csv.DictReader(f)

    c.execute("CREATE TABLE students(name TEXT, age INTEGER, id INTEGER);")
    for row in reader:
        c.execute(f'INSERT INTO students VALUES("{row.get("name")}", {row.get("age")}, {row.get("id")});')

#working fetch for all the tables
#c.execute("SELECT * FROM courses;")
#print(c.fetchall())
#c.execute("SELECT * FROM students;")
#print(c.fetchall())


#slightly more formatted prints!!
print("COURSES: \n")
for entry in c.execute("SELECT * FROM courses;"):
    print(entry)

print("\n\nSTUDENTS: \n")
for entry in c.execute("SELECT * FROM students;"):
    print(entry)


#command = "CREATE TABLE talos"          # test SQL stmt in sqlite3 shell, save as string
#c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


