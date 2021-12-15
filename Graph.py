import matplotlib.pyplot as plt 
import numpy as np

class Plotting():
    def plot_offical_languages_popsize_spoken(self):
        labels = ['G1', 'G2', 'G3', 'G4', 'G5']
        men_means = [20, 34, 30, 35, 27]
        women_means = [25, 32, 34, 20, 25]
        unspecified_means = [5, 62, 24, 50, 15]

        x = np.arange(len(labels))  # the label locations
        width = 0.15  # the width of the bars

        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width/3, men_means, width, label='Men')
        rects2 = ax.bar(x + width/3, women_means, width, label='Women')
        rects3 = ax.bar(x- width/3, unspecified_means, width, label='unspecified')

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Scores')
        ax.set_title('Scores by group and gender')
        ax.set_xticks(x, labels)
        ax.legend()

        ax.bar_label(rects1, padding=3)
        ax.bar_label(rects2, padding=3)
        ax.bar_label(rects3, padding=3)

        fig.tight_layout()
    
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