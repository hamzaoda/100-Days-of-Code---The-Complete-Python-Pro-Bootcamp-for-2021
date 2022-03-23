travel_log=[
    {
        "country":"France",
        "visits" :12,
        "cities" :["Paris", "Lille", "Dijon"]
    },
    {
        "country":"Germany",
        "visits" :5,
        "cities" : ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(city, visits, cities):
    new_country = {
        "country" : city,
        "visits" : visits,
        "cities" : cities
    }
    travel_log.append(new_country)
add_new_country("Russia", 2, ["Mosco", "Saint"])
print(travel_log)