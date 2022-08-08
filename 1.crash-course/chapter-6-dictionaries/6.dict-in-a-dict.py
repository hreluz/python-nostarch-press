users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

cities = {
    'lima': {
        'population': '10 million',
        'country': 'Peru'
    },
    'new york': {
        'population': '25 million',
        'country': 'USA'
    }
}

for city, city_info in cities.items():
    print(f"Lima is located in {city_info['country'].title()} and has a population of {city_info['population']}")