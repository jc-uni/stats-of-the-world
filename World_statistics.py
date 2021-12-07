import mysql.connector

def connect():
    i = 0
    connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
    print(connection)

    mycursor = connection.cursor()
    queries()
    

def queries():
    query = "SELECT * FROM city"
    mycursor.execute(query)

    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def main():
    print("Hello world")
    connect()
    

if __name__ == "__main__":
    main()