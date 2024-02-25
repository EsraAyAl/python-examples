# sqlite3 is built-in to python, no pip needed!
import sqlite3
#created database called employee_db
db = sqlite3.connect('employee_db')
print('Connection Established!')

# Created Cursor Object because establish with database, cursor object allows me to execute my commands, no cursor no commands
cursor = db.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS employee(id INTEGER UNIQUE NOT NULL,
                                first_name TEXT NOT NULL,
                                last_name TEXT,
                                contact_number TEXT);
    '''
)

db.commit()
print("Table Created!")

cursor.execute(
    '''
        INSERT INTO employee VALUES (10, 'John', 'Python', '000 000 0000');
    '''
)

db.commit()
print('Entry Added!')
cursor.execute(
    '''
        SELECT * FROM employee;
    '''
)
data = cursor.fetchone()
print(data)
for row in cursor:
    print(f"{row}\n")