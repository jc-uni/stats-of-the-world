class Statistics():
    
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

