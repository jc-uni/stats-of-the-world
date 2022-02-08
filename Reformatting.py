class Reformat():
    def life_expectancy_popdensity_correlation(self, data):
        labels = []
        life_expectancy = []
        pop_density = []

        for i in range(len(data)):
            labels.append(data[i][0])
            life_expectancy.append(data[i][1])
            pop_density.append(data[i][2])

        return labels, life_expectancy, pop_density

    def offical_languages_popsize_spoken(self, data):
        name_list = []
        total_pop_list = []
        pop_list = []

        for i in range(len(data)):
            name_list.append(data[i][0] +", " +data[i][2])
            total_pop_list.append(data[i][1])
            pop_list.append(data[i][3])

        return name_list, total_pop_list, pop_list

    def average_value(self, data):
        return round(data[0][0])

    def median_value(self, data):
        answer = data[round(len(data)/2)]
        return answer[0]