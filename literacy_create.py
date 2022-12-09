import sqlite3
import csv

# Creating the database
connection = sqlite3.connect('literacy.db')
drop = 'DROP TABLE IF EXISTS literacy_rates'
lit_table = 'CREATE TABLE literacy_rates (id integer primary key, Region VAR, Country VAR, Year VAR, Age VAR, Gender VAR, Literacy_rate VAR)'


#setting up connection
cursor = connection.cursor()
cursor.execute(drop)
cursor.execute(lit_table)

#connection.commit()

insert_query = 'INSERT INTO literacy_rates(id, Region, Country, Year, Age, Gender, Literacy_rate) VALUES (?,?,?,?,?,?,?)'


##open the csv file
file = open('/workspaces/IDS_project3/Literacyrates.csv')

##read the contents of the csv file
contents = csv.reader(file)

##skip the header
next(contents)

##create a list of tuples

seq_of_parameters = []

for row in contents:
    seq_of_parameters.append(row)

#print(seq_of_parameters)

for i in seq_of_parameters:
    cursor.execute(insert_query,i)

connection.commit()


##Query 1

print(f"BELOW ARE ALL THE DISTINCT COUNTRIES IN THE DATASET:")
query1 = """SELECT Distinct country FROM literacy_rates;"""

for i in cursor.execute(query1):
    print(i)

print(f"Countries that start with the letter A:")
query2 = """SELECT Distinct country FROM literacy_rates WHERE country LIKE 'A%' LIMIT 10;"""

for i in cursor.execute(query2):
    print(i)


#select top 10 countries with highest literacy rate

print(f"Top 10 Countries with highest literacy rate:")
query3 = """SELECT distinct country, literacy_rate FROM literacy_rates ORDER BY literacy_rate DESC LIMIT 10;"""

for i in cursor.execute(query3):
    print(i)


#select top 10 countries with lowest literacy rate
print(f"Top 10 Countries with lowest literacy rate:")
query4 = """SELECT country, literacy_rate FROM literacy_rates ORDER BY literacy_rate ASC LIMIT 10;"""

for i in cursor.execute(query4):
    print(i)


#select top 10 countries with highest literacy rate for 15-24 year olds

print(f"Top 10 Countries with highest literacy rate for 15- 24 year olds:")
query5 = """SELECT Distinct country, literacy_rate FROM literacy_rates WHERE age = '15-24' ORDER BY literacy_rate DESC LIMIT 10;"""

for i in cursor.execute(query5):
    print(i)