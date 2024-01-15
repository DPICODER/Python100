country = input("Enter Country Name :")
visits = int(input("Enter Times Visited :"))
list_of_cities = input("Enter List of cities : ").split(",")

travel_log = [{
    "country" : "france",
    "visits" : 12,
    "cities" : ["paris","lille","Dijon"]
}
]

def add_new_country(name, times_visited , cities_list):
    user_country = {}
    user_country["country"] = name
    user_country["visits"] = times_visited
    user_country["cities"] = cities_list 

    travel_log.append(user_country)



add_new_country(country,visits,list_of_cities)

# print(travel_log[1])

print(f"I have been to {travel_log[1]["country"]}{travel_log[1]["visits"]} times")
print(f"My Favorite city was {travel_log[1]["cities"][0]}.")