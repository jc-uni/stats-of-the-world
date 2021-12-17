import mysql.connector

connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
print(connection)
cursor = connection.cursor()

class Connect():
    def fetch_data(self, sql_query):
        cursor.execute(sql_query)
        fetched_data = cursor.fetchall()
        return fetched_data