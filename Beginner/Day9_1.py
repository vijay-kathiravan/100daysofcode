country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country:str,visits:int,list_of_cities:list):
    """
    This function allows us to add new key, value pairs to our exsisting nested dictionary
    :param country: Takes the countries name as input
    :param visits: Takes the number of visits made to that country
    :param list_of_cities: Takes a list of cities as input
    :return: Returns a nested dictionary
    """
    travel_log_dict = {}
    travel_log_dict['country'] = country
    travel_log_dict['visits'] = visits
    travel_log_dict['cities'] = list_of_cities
    travel_log.append(travel_log_dict)

add_new_country(country, visits, list_of_cities)
print(travel_log)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")