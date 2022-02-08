class Queries():
    avg_city_pop_query = "SELECT AVG(Population) FROM city "
    avg_country_pop_query = "SELECT AVG(Population) FROM country WHERE IndepYear IS NOT NULL"
    median_city_pop_query = "SELECT Population FROM city ORDER BY Population ASC"
    median_country_pop_query = "SELECT Population FROM country WHERE IndepYear IS NOT NULL ORDER BY Population ASC"
    offical_languages_popsize_spoken_query = "SELECT Name,Population,Language,ROUND(Population * (Percentage / 100)) AS PeopleSpeakingOfficial,Percentage FROM countrylanguage AS cl INNER JOIN country AS c ON cl.CountryCode = c.Code WHERE IsOfficial = TRUE ORDER BY Name,PeopleSpeakingOfficial"
    life_expectancy_popdensity_correlation_query = "SELECT Name, LifeExpectancy, (Population / SurfaceArea) AS PopDensity FROM country WHERE LifeExpectancy IS NOT NULL"