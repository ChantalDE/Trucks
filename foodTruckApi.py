import logging
import datetime

from flask import Flask, jsonify, request, Response, make_response, jsonify
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

@app.route("/getallfoodtrucks", methods=['POST', 'GET'])
def getAllFoodTrucks():
    trucks = []
    connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
    cursor = connection.cursor()
    cursor.execute("SELECT name, address, opentime, closetime, foodtags, rating FROM foodtruckusers;")
    rows = cursor.fetchall()
    connection.commit()
    logging.debug("Status message: %s", cursor.statusmessage)




    trucksD = {}
    for i, row in enumerate(rows, start = 1):
        Trucks = {
                "Trucks" + str(i):{
                    "name": row[0],
                    "address": row[1],
                    "opentime": row[2],
                    "closetime": row[3],
                    "foodtags": row[4],
                    "rating": row[5]
                }
         }
        trucksD.update(Trucks)
            
    return json.dumps(trucksD, indent=4, sort_keys=True, default=str), 200




@app.route("/updateusertable", methods=['POST', 'GET'])
def updateUserTable():
    print("function call")    

    x = request.get_data()
    data = json.loads(x)
    print(data)
    name = data["name"]
    street = data["street"]
    city = data["city"]
    state = data["state"]
    zipcode = data["zip"]
    opentime = data["open"] 
    closetime = data["close"]
    foodtags = "spicy, hot, nice"
    rating = 9.5
    address = "hazelaarlaan 31"

    try:
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
        cursor = connection.cursor()
        
        query = ("INSERT INTO foodtruckusers(name,address, opentime, closetime, foodtags, rating) VALUES (%s, %s, %s, %s, %s, %s)")
        insertStuff = (name, address, opentime, closetime, foodtags, rating)
        cursor.execute(query, insertStuff)

        queryAddress = ("INSERT INTO foodtruckaddress(name, streetname, city, zipcode) VALUES (%s, %s, %s, %s)")
        insertAddress = (name, street, city, zipcode)
        cursor.execute(queryAddress, insertAddress)
        connection.commit()
        print("Successfully added to db")
        return 'OK', 200

    except (Exception, psycopg2.Error) as error:
        if(connection):
            print("Failed to insert record into mobile table", error)
            return 'Not OK', 400

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
            return 'OK', 200

    logging.debug("Status message: %s", cursor.statusmessage)
    return 'OK', 200 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
