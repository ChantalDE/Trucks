import logging

from flask import Flask, jsonify
#request, Response, make_response, jsonify
import json
import psycopg2

app = Flask(__name__)

"""--Get All foodTruckUsers
SELECT TOP 20 *
FROM foodTruckUsers;

--Get All foodTruckAddresses
SELECT TOP 20 *
FROM foodTruckAddress;

--Get All Food Trucks with FoodTruckAddresses
SELECT ftu.Name AS Name
	 , ftu.Address AS Address
	 , ftu.OpenTime AS OpenTime
	 , ftu.CloseTime AS CloseTime
	 , ftu.FoodTags AS FoodTags
	 , ftu.Rating AS Rating
FROM foodTruckUsers AS ftu
	INNER JOIN foodTruckAddress AS fta ON fta.Name = ftu.Name;

--Create foodTruckUsers
CREATE TABLE foodTruckUsers
(
	Name VARCHAR(70),
	Address VARCHAR(135),
	OpenTime TIMESTAMP,
	CloseTime TIMESTAMP,
	FoodTags, VARCHAR(200),
	Rating, DECIMAL
);

--CREATE foodTruckAddress
CREATE TABLE foodTruckAddress
(
	Name VARCHAR(70) PRIMARY KEY,
	StreetName VARCHAR(70),
	City VARCHAR(25),
	ZipCode INT
);

--INSERT into foodTruckUsers table
INSERT INTO foodTruckUsers(Name, Address, OpenTime, CloseTime, FoodTags, Rating)
VALUES ('%s', '%s', '%s', '%s', '%s', '%f');

--INSERT INTO foodTruckAddress table
INSERT INTO foodTruckAddress(Name, StreetName, City, ZipCode)
VALUES ('%s', '%s', '%s', '%d');

"""

class FoodTruck:
    def __init__(self, name, address, opentime, closetime, foodtags, rating):
        self.name = name
        self.address = address
        self.opentime = opentime
        self.closetime = closetime
        self.foodtags = foodtags
        self.rating = rating
        def printTruck(self):
            print("The name is %s", self.name)

queryTest = """CREATE TABLE test2(
           test INTEGER
);"""
userCreateTable = """CREATE TABLE foodTruckUsers
(
	Name VARCHAR(70),
	Address VARCHAR(135),
	OpenTime TIME,
	CloseTime TIME,
	FoodTags VARCHAR(200),
	Rating DECIMAL
);"""
addressCreateTable = """CREATE TABLE foodTruckAddress
(
	Name VARCHAR(70) PRIMARY KEY,
	StreetName VARCHAR(70),
	City VARCHAR(25),
	ZipCode INT
);"""

userUserCreateTable = """CREATE TABLE userUser
(
    Username VARCHAR(20),
    Password VARCHAR(20)
);"""

#database connect
username = "jahlil"
host = "free-tier14.aws-us-east-1.cockroachlabs.cloud"
port = "26257"
database = "lucid-satyr-874.defaultdb"
password = "FwtR7uwfJKJseHruFfDW4g"



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape")
def scrape():
    return "<p>Scrape</p>"

@app.route("/display")
def display():
    #display whatever is in the foodTable
    connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
    cursor = connection.cursor()
    cursor.execute("SELECT name, address, opentime, closetime, foodtags, rating FROM foodtruckusers;")
    rows = cursor.fetchall()
    connection.commit()
    logging.debug("Status message: %s", cursor.statusmessage)
    return json.dumps(rows, indent=4, sort_keys=True, default=str), 200

@app.route("/getallfoodtrucks")
def getAllFoodTrucks():
    trucks = []
    connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
    cursor = connection.cursor()
    cursor.execute("SELECT name, address, opentime, closetime, foodtags, rating FROM foodtruckusers;")
    rows = cursor.fetchall()
    connection.commit()
    logging.debug("Status message: %s", cursor.statusmessage)

    for row in rows:
        temp = FoodTruck(row[0], row[1], row[2], row[3], row[4], row[5])
        trucks.append(temp)
    #trucks[0].printTruck()
    return json.dumps(trucks[0].name, indent=4, sort_keys=True, default=str), 200

@app.route("/insert")
def insert():
    #get data from pduff
    #get JSON
    return "<p>Hello, World!</p>"

@app.route("/updateusertable")
def updateUserTable(name, address, opentime, closetime, foodtags, rating):
    #get data from scraping?
    connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO foodTruckUsers(Name, Address, OpenTime, CloseTime, Foodtags, Rating) VALUES (%s, %s, %s, %s, %s, %s);", (name, address, opentime, closetime, foodtags, rating))
    connection.commit()
    logging.debug("Status message: %s", cursor.statusmessage)
    return "Data inserted"


@app.route("/dbsend")
def insertdb():
    
    try:
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
        cursor = connection.cursor()

        #cursor.execute(queryTest)

        #Insert the User table
        #cursor.execute(userCreateTable)

        #Insert the Address table
        cursor.execute(userCreateTable)
        connection.commit()
        return 'OK', 200

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return 'Not OK', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
