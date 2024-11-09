class TableDB:
    def __init__(self):
        self.table_database = []
    def insert(self, table):
        status = self.search(table)
        if status == -1:
            self.table_database.append(table)
        else:
            return f"Table {table} already exists"
    def search(self, table_name):
        for i in self.table_database:
            if i == table_name:
                return i
        return -1

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table
    def filter(self,condition):
        filtered_list = []
        for item in self.table:
            if condition(item):
                filtered_list.append(item)
        return filtered_list
    def aggregate(self, aggregation_key, aggregation_function):
        _list = []
        for item in self.table:
            value = float(item[aggregation_key])
            _list.append(value)
        return aggregation_function(_list)

    def __str__(self):
        return f"Table: {self.table_name}, with {len(self.table)}"

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
# Let's write code to

cities_table = Table("cities", cities)
countries_table = Table("countries", countries)

db = TableDB()
db.insert(cities_table)
db.insert(countries_table)

cities_in_italy = cities_table.filter(lambda x: x['country'] == 'Italy')
cities_in_sweden = cities_table.filter(lambda x: x["country"] == "Sweden")

cities_italy = Table("italy_cities", cities_in_italy)
cities_sweden = Table("sweden_cities", cities_in_sweden)

db.insert(cities_italy)
db.insert(cities_sweden)


# - print the average temperature for all the cities in Italy
avg_italy = cities_italy.aggregate("temperature", lambda x: sum(x)/len(x))
print(f"The average temperature of all the cities in Italy :\n{avg_italy}\n")
# - print the average temperature for all the cities in Sweden
avg_sweden = cities_sweden.aggregate("temperature", lambda x: sum(x)/len(x))
print(f"The average temperature of all the cities in Sweden :\n{avg_sweden}\n")
# - print the min temperature for all the cities in Italy
min_italy = cities_italy.aggregate("temperature", lambda x: min(x))
print(f"The min temperature of all the cities in Italy :\n{min_italy}\n")
# - print the max temperature for all the cities in Sweden
max_sweden = cities_sweden.aggregate("temperature", lambda x: max(x))
print(f"The max temperature of all the cities in Sweden :\n{max_sweden}\n")

max_latitude = cities_table.aggregate("latitude", lambda x: max(x))
min_latitude = cities_table.aggregate("latitude", lambda x: min(x))

print("Max latitude for the cities in every countries")
print(f"{max_latitude}\n")
print("Min latitude for the cities in every countries")
print(f"{min_latitude}\n")
