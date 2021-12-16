class Control():
    import mysql.connector
    from Graphing import Plotting
    from Reformatting import Statistics
    from QueriesSQL import Queries

    Stats = Statistics()
    Plots = Plotting()
    AllQueries = Queries()

    connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
    print(connection)
    cursor = connection.cursor()

    def find_offical_languages_popsize_spoken(self):
        #Speakers of official languages in the countries of the world
        fetched = fetch_data(AllQueries.offical_languages_popsize_spoken_query)
        final_result = Stats.offical_languages_popsize_spoken(fetched)
        Plots.plot_offical_languages_popsize_spoken(final_result)
        Plots.show_graph()

    def find_median_average_pop_city_country(self):
        find_average_pop_country_city()
        find_median_pop_country_city()
        Plots.show_graph()

    def find_average_pop_country_city():
        #Average population of cities & countries
        fetched_city_pop = fetch_data(AllQueries.avg_city_pop_query)
        final_result_avg_city_pop = Stats.average_value(fetched_city_pop)

        fetched_country_pop = fetch_data(AllQueries.avg_country_pop_query)
        final_result_avg_country_pop = Stats.average_value(fetched_country_pop)

        Plots.plot_averages(final_result_avg_city_pop,final_result_avg_country_pop)

    def find_median_pop_country_city():
        #Median population of cities & countries
        fetched_city_pop_med = fetch_data(AllQueries.median_city_pop_query)
        final_result_med_city_pop = Stats.median_value(fetched_city_pop_med)
    
        fetched_country_pop_med = fetch_data(AllQueries.median_country_pop_query)
        final_result_med_country_pop = Stats.median_value(fetched_country_pop_med)

        Plots.plot_medians(final_result_med_city_pop, final_result_med_country_pop)

    def fetch_data(sql_query):
        cursor.execute(sql_query)
        fetched_data = cursor.fetchall()
        return fetched_data