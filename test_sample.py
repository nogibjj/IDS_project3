import sqlite3
import os
from faker import Faker

connection = sqlite3.connect('test_sample.db')
drop_table = 'DROP TABLE IF EXISTS people'
table = 'CREATE TABLE people (id integer primary key, name TEXT, surname TEXT)'

cursor = connection.cursor()
cursor.execute(drop_table)
cursor.execute(table)

#cursor.execute(table)

connection.commit()
#generating random fake names

fake = Faker()
names = [fake.name().split() for i in range(100)]
names = [name for name in names if len(name) == 2]

connection = sqlite3.connect('test_sample.db')

cursor = connection.cursor()

insert_query = 'INSERT INTO people(name,surname) VALUES (?,?)'

for name in names:
    cursor.execute(insert_query, name)

    connection.commit()


select_query = 'SELECT * from people LIMIT 6'
for i in cursor.execute(select_query):
    print(i)


