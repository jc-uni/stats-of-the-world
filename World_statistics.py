import mysql.connector
from Graph import Plotting
from Analysis import Statistics

connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
print(connection)
cursor = connection.cursor()


def main():
    Stats = Statistics()
    Plots = Plotting()

    #Average population of cities & countries
    cursor.execute(Stats.avg_city_pop_query)
    fetched_city_pop = cursor.fetchall()
    final_result_avg_city_pop = Stats.avg_city_pop(fetched_city_pop)

    cursor.execute(Stats.avg_country_pop_query)
    fetched_country_pop = cursor.fetchall()
    final_result_avg_country_pop = Stats.avg_country_pop(fetched_country_pop)

    Plots.plot_averages(final_result_avg_city_pop,final_result_avg_country_pop)
    
    #Median population of cities & countries
    cursor.execute(Stats.median_city_pop_query)
    fetched_city_pop_med = cursor.fetchall()
    final_result_med_city_pop = Stats.median_city_pop(fetched_city_pop_med)

    cursor.execute(Stats.median_country_pop_query)
    fetched_country_pop_med = cursor.fetchall()
    final_result_med_country_pop = Stats.median_country_pop(fetched_country_pop_med)

    Plots.plot_medians(final_result_med_city_pop, final_result_med_country_pop)
    
    #Show average & median population of cities & countries
    Plots.show_graph()
    

if __name__ == "__main__":
    main()