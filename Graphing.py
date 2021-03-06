import matplotlib.pyplot as plt 
import numpy as np

class Plotting():
    def plot_life_expectancy_popdensity_correlation(self, data):
        colors = ["black","green","blue", "red","yellow"]
        for n in range(len(data)):
            xpoints = np.array(data[n][0])
            ypoints = np.array(data[n][1])
            plt.scatter(xpoints, ypoints,color = colors[n], s = 8)

        plt.text(76,26000,"Macao")
        plt.text(72,22000,"Monaco")
        plt.text(71,6300,"Hong Kong")
        plt.text(72,5200,"Singapore")
        plt.text(72,3800,"Gibraltar")
        plt.xlabel("life expectancy")
        plt.ylabel("pop/km^2")
        plt.legend(["america","europe","asia","oceania","africa"], loc="upper left")

    def plot_offical_languages_popsize_spoken(self, data):
        labels = data[0]
        total_pop = data[1]
        language = data[2]

        x = np.arange(len(labels))  # the label locations
        width = 0.5  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x, language, width, label='Speakers')
        rects2 = ax.bar(x + width, total_pop, width, label='Total population of country')
        
        ax.set_ylabel('Population')
        ax.set_title('Speakers of official languages of countries')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)

        plt.setp(ax.get_xticklabels(), rotation=15, ha='right')

        fig.tight_layout
    
    def plot_averages(self, avg_pop_city, avg_pop_country):
        np_avg = np.array([avg_pop_city, avg_pop_country])
        plt.bar(["Avg pop city","Avg pop country"],np_avg, color = 'y')
        plt.text(0,np_avg[0],np_avg[0],ha='center',fontsize=8)
        plt.text(1,np_avg[1],np_avg[1],ha='center',fontsize=8)
        plt.xticks(fontsize=8)

    def plot_medians(self, med_pop_city, med_pop_country):
        np_med = np.array([med_pop_city, med_pop_country])
        plt.bar(["Median pop city","Median pop country"],np_med, color = 'g')
        plt.text(2,np_med[0],np_med[0],ha='center',fontsize=8)
        plt.text(3,np_med[1],np_med[1],ha='center',fontsize=8)
        plt.xticks(fontsize=8)

    def show_graph(self):
        plt.show()