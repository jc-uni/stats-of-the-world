class Statistics():
    avg_city_pop_query = "SELECT AVG(Population) FROM city "
    avg_country_pop_query = "SELECT AVG(Population) FROM country WHERE IndepYear IS NOT NULL"
    median_city_pop_query = "SELECT Population FROM city ORDER BY Population ASC"
    median_country_pop_query = "SELECT Population FROM country WHERE IndepYear IS NOT NULL ORDER BY Population ASC"

    def avg_city_pop(self, data):
        return data[0][0]

    def avg_country_pop(self, data):
        return data[0][0]

    def median_city_pop(self, data):
        answer = data[round(len(data)/2)]
        return answer[0]

    def median_country_pop(self, data):
        answer = data[round(len(data)/2)]
        return answer[0]
