import mysql.connector
from Analysis import Statistics

connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
print(connection)
cursor = connection.cursor()

Stats = Statistics()

cursor.execute(Stats.median_country_pop_query)
fetched_data = cursor.fetchall()
calculated_result = Stats.median_country_pop(fetched_data)
for x in calculated_result:
    print(x)
    

def main():
    print("Hello world")
    #connect()
    

if __name__ == "__main__":
    main()