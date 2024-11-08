import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

# Print the average temperature of all the cities
def avg_temp(list_of_dictionary):
    print("The average temperature of all the cities:")
    temps = []
    for city in list_of_dictionary:
        temps.append(float(city['temperature']))
    return f"{sum(temps) / len(temps)}\n"
    # print(sum(temps)/len(temps))
    # print()
print(avg_temp(cities))

# Print all cities in Italy
def all_cities(country, list_of_dictionary):
    cities_temp = []
    # my_country = countries
    for city in list_of_dictionary:
        if city['country'] == country:
            cities_temp.append(city['city'])
    return f"All the cities in {country} :\n{cities_temp}\n"
    # print("All the cities in", my_country, ":")
    # print(cities_temp)
    # print()
print(all_cities("Italy", cities))

# Print the average temperature for all the cities in Italy
def avg_temp(country, list_of_dictionary):
    temps = []
    # my_country = 'Italy'
    for city in list_of_dictionary:
        if city['country'] == country:
            temps.append(float(city['temperature']))
    return f"The average temperature of all the cities in {country} :\n{sum(temps) / len(temps)}\n"
    # print("The average temperature of all the cities in", my_country, ":")
    # print(sum(temps)/len(temps))
    # print()
print(avg_temp("Italy", cities))

# Print the max temperature for all the cities in Italy
def max_temp(country, list_of_dictionary):
    temps = []
    # my_country = 'Italy'
    for city in list_of_dictionary:
        if city['country'] == country:
            temps.append(float(city['temperature']))
    return f"The maximum temperature of all the cities in {country} :\n{max(temps)}\n"
    # print("The max temperature of all the cities in", my_country, ":")
    # print(max(temps))
    # print()
print(max_temp("Italy", cities))

# Print the min temperature for all the cities in Italy
def min_temp(country, list_of_dictionary):
    temps = []
    # my_country = 'Italy'
    for city in cities:
        if city['country'] == country:
            temps.append(float(city['temperature']))
    return f"The min temperature of all the cities in {country} :\n{min(temps)}\n"
    # print("The min temperature of all the cities in", my_country, ":")
    # print(min(temps))
    # print()
print(min_temp("Italy", cities))

def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list

x = filter(lambda x: float(x['latitude']) >= 60.0, cities)
for item in x:
    print(item)

def aggregate(aggregation_key, aggregation_function, dict_list):
    lst = []
    for item in dict_list:
        value = float(item[aggregation_key])
        lst.append(value)
    return aggregation_function(lst)

# Let's write code to
# - print the average temperature for all the cities in Italy
print(avg_temp("Italy", cities))
# - print the average temperature for all the cities in Sweden
print(avg_temp("Sweden", cities))
# - print the min temperature for all the cities in Italy
print(min_temp("Italy", cities))
# - print the max temperature for all the cities in Sweden
print(max_temp("Sweden", cities))