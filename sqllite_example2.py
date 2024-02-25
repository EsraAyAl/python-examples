#Python's SQLite module
#It is easy to create and manipulate databases with Python. To allow us to use SQLite with Python, 
# the Python Standard Library includes a module called "sqlite3". To use the SQLite3 module, we need to 
# add an import statement to our Python script:

import sqlite3

# Creates or opens a file called student_db with a SQLite3 DB

db = sqlite3.connect('student_db')

# Sanity check, because I'm paranoid.
print('Connection Established!')

#Creating & deleting tables. To make any changes to the database, we need a cursor object.
cursor = db.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, name TEXT,
                grade INTEGER)
''')

db.commit()

# Sanity check
print('Table Created!')

#Inserting into the Database. To insert data, we use the cursor again to execute a SQL statement. 
# When using data stored in Python variables to insert data into a database table, use the "?" placeholder. 
# It is not secure to use string operations or concatenation to make your queries. In this example, we are going to 
# insert two students into the database; their information is stored in Python variables.

id1 = 1001
name1 = 'Jimbo'
grade1 = 78

id2 = 1002
name2 = 'John'
grade2 = 80

# insert first student
cursor.execute('''
    INSERT INTO student(id, name, grade)
                VALUES(?,?,?)
''', (id1,name1,grade1))

print('First user added!')

cursor.execute('''
    INSERT INTO student(id, name, grade)
                VALUES(?,?,?)
''', (id2,name2,grade2))

print('Second user added!')

db.commit()

#In the example below, the values of the Python variables are passed inside a tuple (you could also use a dictionary):
#It is up to us. We can add dictionary or like up code to add values.
id3 = 1003
name3 = 'Johnny'
grade3 = 68

cursor.execute('''
    INSERT INTO student(id, name, grade)
                VALUES(:id, :name, :grade)
''', {'id':id3, 'name':name3, 'grade':grade3})

print('Third user added!')

db.commit()

#If you need to insert several users, use executemany and a list with the tuples:
students_ = [(1004, name1, grade1),(1005, name2, grade2),(1006, name3, grade3)]

cursor.executemany('''
    INSERT INTO student(id, name, grade)
                    VALUES(?,?,?)
''', students_)

print('Multiple users added')

db.commit()

#If you need to get the id of the row you just inserted, use lastrowid:
find_id = cursor.lastrowid
print(f'Last row id : {find_id}')

#Use rollback to roll back any change to the database since the last call to commit: like ctrl z
cursor.execute('''
    UPDATE student SET grade=? WHERE id=?
''', (65, 1002))

db.rollback()

#To retrieve data, execute a SELECT SQL statement against the cursor object and then use fetchone() to retrieve a single row or 
# fetchall() to retrieve all the rows.
id_ = 1003

cursor.execute('''
    SELECT name, grade FROM student WHERE id=?
''', (id_,))

student = cursor.fetchone()
print(student)

#The cursor object works as an iterator, invoking fetchall() automatically
cursor.execute('''SELECT name, grade FROM student''')

for row in cursor:
    # row[0] returns the name column values and row[1] returns the grade column values
    print(f'name : {row[0]} grade : {row[1]}')


#Updating or deleting data is practically the same as inserting data:
grade = 100
id_ = 1001

# update student id 1001
cursor.execute('''
    UPDATE student SET grade=? WHERE id=?
''', (grade,id_))

# Delete student id 1002
id_2 = 1002

cursor.execute('''DELETE FROM student WHERE id=?''', (id_2,))

db.commit()

#When we are done working with the DB, we need to close the connection:
db.close()

