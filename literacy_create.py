import sqlite3
import csv

# Creating the database
connection = sqlite3.connect('literacy.db')
drop = 'DROP TABLE IF EXISTS literacy_rates'
lit_table = 'CREATE TABLE literacy_rates (id integer primary key, Region TEXT, Country TEXT, Year integer, Age integer, Gender TEXT, Literacy_rate float)'


#setting up connection
cursor = connection.cursor()
cursor.execute(drop)
cursor.execute(lit_table)

connection.commit()



insert_query = 'INSERT INTO literacy_rates(id, Region, Country, Year, Age, Gender, Literacy_rate) VALUES (?,?,?,?,?,?,?)'

 