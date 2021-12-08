import matplotlib.pyplot as plt 
import numpy as np
import mysql.connector

from Analysis import Statistics

class Plotting():

    def __init__(self):
        fetching_and_plotting()

        #fetched_data = cursor.fetchall()

        #calculated_result = Stats.median_city_pop(fetched_data)
        #for x in calculated_result:
            #print(x)


    def show_graph(self):
        plt.show()
    
    def plot_averages(self, avg_pop_city, avg_pop_country):
        np_avg = np.array([avg_pop_city, avg_pop_country])
        plt.bar(["AVG POP CITY","AVG POP COUNTRY"],np_avg)

    def plot_medians(self, med_pop_city, med_pop_country):
        np_avg = np.array([med_pop_city, med_pop_country])
        plt.bar(["MEDIAN POP CITY","MEDIAN POP COUNTRY"],np_avg)
        
    def fetching_and_plotting():
        connection = mysql.connector.connect(host = "localhost", user = "read_only_user", password = "123", database = "world")
        print(connection)
        cursor = connection.cursor()

        Stats = Statistics()

        cursor.execute(Stats.median_city_pop_query)
        fetched_city_pop = cursor.fetchall()

        cursor.execute(Stats.median_country_pop_query)
        fetched_country_pop = cursor.fetchall()

        plot_averages(fetched_city_pop,fetched_country_pop)

        cursor.execute(Stats.avg_city_pop_query)
        fetched_city_pop_avg = cursor.fetchall()

        cursor.execute(Stats.avg_country_pop_query)
        fetched_country_pop_avg = cursor.fetchall()

        plot_medians(fetched_city_pop_avg, fetched_country_pop_avg)