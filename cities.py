""""
- write a menu-based program
-practice Python list, dict types
-How to represent program entitites  list vs dict
-how to structure the program


Problem statement
-Manage a list of cities. Eeach city has a name, population and county

Program requirements
-sort them by any of their features(name, pop, county)
-Add a city frim the console
-Generate some random cities
-Search for a city, using case-insensitive partial string matching
-exit the program
"""

#--- Functions that deal with how a city is represented
#my_city = ["Constanta", 200000, "Constanta"]

# A dict is a set of key-to value mappings; keys must be unique, values not necesarely
#my_city = {"name" : "Braila", "population" : 150_000, "county" : "Braila"}

def create_city (name: str, population: int, county: str):
    #list representation
    #return [name, population, county]
    #dict representation
    return {"name" : name, "population" : population, "county" : county}

def get_name(city) -> str:
    #return city[0]
    return city["name"]

def get_population(city) -> int:
    #return city[1]
    return city["population"]

def get_county(city) -> str:
    #return city[2]
    return city["county"]

def to_str(city) -> str:
    return get_name(city) + " with population of " + str(get_population(city)) + " is in " + get_county(city)

#my_city = create_city(" Braila", 150_000,  "Braila")

def show_all_city(city_list: list) -> None:
    print("List of cities:")
    for city in city_list:
        print(to_str(city))

def sort_cities(city_list: list) -> None:
    sort_flag = False
    while sort_flag == False:
        sort_flag = True
        for i in range(0, len(city_list) - 1):
            if get_name(city_list[i] > get_name(city_list[i + 1])):
                 city_list[i], city_list[i + 1] = city_list[i + 1], city_list[i]
                 sort_flag = False


def add_city(city_list: list) -> None:
    print("Add a new city")
    name = input("City name =")
    while True:
        try:
            pop = int(input("City population ="))
            break
        except ValueError:
            print("Population must be an integer!")

    county = input("County =")
    city_list.append(create_city(name, pop, county))



def start():
    cities_list = []

    cities_list.append(create_city("Braila", 150_000, "Braila"))
    cities_list.append(create_city("Roman", 40_000, "Neamt"))
    print(len(cities_list))
    while True:
        print("1. Show all citites")
        print("2. Add a city")
        print("3. Search for a city")
        print("4. Sort the city list")
        print("0. Exit")

        command = input(">")

        if command == "1":
            show_all_city(cities_list)
        elif command == "2":
            add_city(cities_list)
        elif command == "0":
            break
        else:
            print("Bad command or file name")

a = 2
start()