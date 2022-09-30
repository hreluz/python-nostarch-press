# * => send a tupple to the function with all the arguments
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

    print(f"The size of the pizza is {size}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# Using Arbitrary Keyword Arguments
# ** => It will send a key-value dictionary
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein',
                             location='princenton',
                             field='physics')

print(user_profile)


def sandwich_maker(*ingredients):
    for ingredient in ingredients:
        print(f"We are adding {ingredient} to your sandwich ")


sandwich_maker('onion', 'jam', 'lettuce', 'tomatoes')
sandwich_maker('bread')


def car_info(manufacturer, model, **car):
    car['manufacturer'] = manufacturer
    car['model'] = model

    return car


car = car_info('Tsubaru', 'Impreza',
               plate='HEC-RC',
               colour='black')
print(car)
