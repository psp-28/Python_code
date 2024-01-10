# Note : Enter the Input as -- 
# Enter the country: India
# Number of visits: 10
# Enter cities: ["Mumbai", "Pune"]      // here enter in the list format

#################################################################################################################

country = input("Enter the country: ")   # Add country name
visits = int(input("Number of visits: "))   #Number of visits
list_of_cities = eval(input("Enter cities: "))  # create list from formatted string. If you not use eval() then only the first character is taken, to take the whole string we are using eval().


travel_log = [
    {
        "country": "France",
        "visits" : 12,
        "cities" : ["Paris", "Lille", "Dijon"]
    },
    {
        "country" : "Germany",
        "visits" : 10,
        "cities" : ["Berlin", "Warsaw", "Hamburg"]
    },
    
]
def add_new_country(name, times_visited,cities_visited):
    new_country = {}
    new_country["country"] = name           # here country is the key that we are passing and name is the value.
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I have been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")

import random
print(f"My favourite city was {travel_log[2]['cities'][random.randrange(0,3)]}.")       # Random will choice random index from 0 to 3 and will select the index number to selec the city from the list.
