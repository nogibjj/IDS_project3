import sqlite3
import csv
import fastapi
from fastapi import FastAPI
import uvicorn
import pandas as pd
import json

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



app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the literacy rates dataset"}

#print(f"BELOW ARE ALL THE DISTINCT COUNTRIES IN THE DATASET:")
query1 = """SELECT DISTINCT country FROM literacy_rates;"""

countries = []
for i in cursor.execute(query1):
    countries.append(i)


#convert list to string
countries = str(countries)
#remove brackets
countries = countries.replace("[","")
countries = countries.replace("]","")
# #remove quotes
countries = countries.replace("'","")



@app.get("/distinct_countries")
async def root():
    return {"All distinct countries": countries}


query2 = """SELECT DISTINCT country FROM literacy_rates WHERE country LIKE 'A%' LIMIT 10;"""

A_countries = []

for i in cursor.execute(query2):
    A_countries.append(i)

#convert list to string
A_countries = str(A_countries)
#remove brackets
A_countries = A_countries.replace("[","")
A_countries = A_countries.replace("]","")
# #remove quotes
A_countries = A_countries.replace("'","")



@app.get("/countries_starting_with_A")
async def root():
    return {"Countries starting with A": A_countries}

query3 = """SELECT DISTINCT country, literacy_rate FROM literacy_rates ORDER BY literacy_rate DESC LIMIT 10;"""

topten = []

for i in cursor.execute(query3):
    topten.append(i)

#convert list to string
topten = str(topten)
#remove brackets
topten = topten.replace("[","")
topten = topten.replace("]","")
# #remove quotes
topten = topten.replace("'","")


@app.get("/top10")
async def top10():
    return {"Top 10 countries with highest literacy rates": topten} 

query4 = """SELECT DISTINCT country, literacy_rate FROM literacy_rates ORDER BY literacy_rate ASC LIMIT 10;"""


bottomten = []

for i in cursor.execute(query4):
    bottomten.append(i)


#convert list to string
bottomten = str(bottomten)
#remove brackets
bottomten = bottomten.replace("[","")
bottomten = bottomten.replace("]","")
# #remove quotes
bottomten = bottomten.replace("'","")

@app.get("/bottom10")
async def bottom10():

    return {" 10 countries with the lowest literacy rates": bottomten}

query5 = """SELECT DISTINCT country, literacy_rate FROM literacy_rates WHERE age = '15-24' ORDER BY literacy_rate DESC LIMIT 10;"""

#query5 = """SELECT DISTINCT country, literacy_rate FROM literacy_rates WHERE age = '15-24' ORDER BY literacy_rate ASC LIMIT 10;"""

top10_15_24 = []

for i in cursor.execute(query5):
    top10_15_24.append(i)

top10_15_24 = str(top10_15_24)
#remove brackets
top10_15_24 = top10_15_24.replace("[","")
top10_15_24 = top10_15_24.replace("]","")
# #remove quotes
top10_15_24 = top10_15_24.replace("'","")

@app.get("/age_15_24")
async def age15_24():

    return {" Top 10 countries with the highest literacy rates for age 15 -24": top10_15_24}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")