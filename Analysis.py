class Statistics():
    avg_city_pop_query = "SELECT AVG(Population) FROM city "
    avg_country_pop_query = "SELECT AVG(Population) FROM country WHERE IndepYear IS NOT NULL"
    median_city_pop_query = "SELECT Population FROM city ORDER BY Population ASC"
    median_country_pop_query = "SELECT Population FROM country WHERE IndepYear IS NOT NULL ORDER BY Population ASC"
    offical_languages_popsize_spoken_query = "SELECT      Name,     Language,     Percentage,     ROUND(Population * (Percentage / 100)) AS PeopleSpeakingOfficial,     Population FROM     countrylanguage AS cl         INNER JOIN     country AS c ON cl.CountryCode = c.Code WHERE     IsOfficial = TRUE ORDER BY Name , PeopleSpeakingOfficial"

    def offical_languages_popsize_spoken(self, data):
        for i in range(len(data)):
            if data[i][0] == data[i-1][0]:
                print(data[i])
                print(data[i-1])
            else:
                print(data[i])

        pass

    def average_value(self, data):
        return round(data[0][0])

    def median_value(self, data):
        answer = data[round(len(data)/2)]
        return answer[0]

