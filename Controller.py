from Graphing import Plotting
from Reformatting import Reformat
from QueriesSQL import Queries
from Connector import Connect

Reform = Reformat()
Plots = Plotting()
AllQueries = Queries()
Connection = Connect()

class Control():

        #Correlation between average life expectancy & population density of a country
    def find_life_expectancy_popdensity_correlation(self):
        data = []
        for i in range(len(AllQueries.life_expectancy_popdensity_correlation_query)):
            fetched = Connection.fetch_data(AllQueries.life_expectancy_popdensity_correlation_query[i])
            reformatted_fetched = Reform.life_expectancy_popdensity_correlation(fetched)
            data.append(reformatted_fetched)
        Plots.plot_life_expectancy_popdensity_correlation(data)
        Plots.show_graph();

        #Speakers of official languages in the countries of the world
    def find_offical_languages_popsize_spoken(self):
        fetched = Connection.fetch_data(AllQueries.offical_languages_popsize_spoken_query)
        final_result = Reform.offical_languages_popsize_spoken(fetched)
        Plots.plot_offical_languages_popsize_spoken(final_result)
        Plots.show_graph()

    def find_median_average_pop_city_country(self):

        #Average population of cities & countries
        fetched_city_pop = Connection.fetch_data(AllQueries.avg_city_pop_query)
        final_result_avg_city_pop = Reform.average_value(fetched_city_pop)

        fetched_country_pop = Connection.fetch_data(AllQueries.avg_country_pop_query)
        final_result_avg_country_pop = Reform.average_value(fetched_country_pop)

        Plots.plot_averages(final_result_avg_city_pop,final_result_avg_country_pop)

        #Median population of cities & countries
        fetched_city_pop_med = Connection.fetch_data(AllQueries.median_city_pop_query)
        final_result_med_city_pop = Reform.median_value(fetched_city_pop_med)
    
        fetched_country_pop_med = Connection.fetch_data(AllQueries.median_country_pop_query)
        final_result_med_country_pop = Reform.median_value(fetched_country_pop_med)

        Plots.plot_medians(final_result_med_city_pop, final_result_med_country_pop)

        Plots.show_graph()

    