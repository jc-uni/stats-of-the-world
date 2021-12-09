import mysql.connector
from Graph import Plotting
from Analysis import Statistics

connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
print(connection)
cursor = connection.cursor()


def main():
    Stats = Statistics()
    Plots = Plotting()

    cursor.execute(Stats.median_city_pop_query)
    fetched_city_pop = cursor.fetchall()

    cursor.execute(Stats.median_country_pop_query)
    fetched_country_pop = cursor.fetchall()

    Plots.plot_averages(fetched_city_pop,fetched_country_pop)

    cursor.execute(Stats.avg_city_pop_query)
    fetched_city_pop_avg = cursor.fetchall()

    cursor.execute(Stats.avg_country_pop_query)
    fetched_country_pop_avg = cursor.fetchall()

    Plots.plot_medians(fetched_city_pop_avg, fetched_country_pop_avg)

    Plots.show_graph()
    

if __name__ == "__main__":
    main()