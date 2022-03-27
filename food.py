from flask import Flask
#request, Response, make_response, jsonify
import psycopg2

app = Flask(__name__)

queryTest = """CREATE TABLE test2(
           test INTEGER
);"""

#database connect
username = "chantal"
host = "free-tier14.aws-us-east-1.cockroachlabs.cloud"
port = "26257"
database = "lucid-satyr-874.defaultdb"
password = "cqtHqk2r1sGnhc12g7khBg"



@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape")
def scrape():
    return "<p>Scrape</p>"

@app.route("/display")
def display():
    #display whatever is in the foodTable
    return "<p>display</p>"


@app.route("/insert")
def insert():
    #get data from pduff
    #get JSON
    return "<p>Hello, World!</p>"

@app.route("/dbsend")
def insertdb():
    
    try:
        connection = psycopg2.connect(user=username, password=password, host=host, port=port, dbname=database)
        cursor = connection.cursor()

        cursor.execute(queryTest)
        return 'OK', 200

    except (Exception, psycopg2.Error) as error :
        if(connection):
            print("Failed to insert record into mobile table", error)

    finally:
        #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
