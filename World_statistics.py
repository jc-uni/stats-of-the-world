import mysql.connector

def connect():
    i = 0
    connection = mysql.connector.connect(host = "localhost", user = "root", password = "MySQLPassword", database = "world")
    print(connection)

    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM city")

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

#def query():

def main():
    print("Hello world")
    connect()

if __name__ == "__main__":
    main()