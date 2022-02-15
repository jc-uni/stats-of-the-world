class Reformat():
    def life_expectancy_popdensity_correlation(self, data):
        #labels = []
        life_expectancy = []
        pop_density = []

        for i in range(len(data)):
            #labels.append(data[i][0])
            life_expectancy.append(data[i][0])
            pop_density.append(data[i][1])

        return life_expectancy, pop_density

    def offical_languages_popsize_spoken(self, data):
        names = []
        total_pops = []
        pops = []

        for i in range(len(data)):
            names.append(data[i][0] +", " +data[i][2])
            total_pops.append(data[i][1])
            pops.append(data[i][3])

        return names, total_pops, pops

    def average_value(self, data):
        return round(data[0][0])

    def median_value(self, data):
        answer = data[round(len(data)/2)]
        return answer[0]