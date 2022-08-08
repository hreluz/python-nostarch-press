pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}


print(f"You have ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        favorite_text = 'favorite languages are:'
    else:
        favorite_text = 'favorite languages is:'

    print(f"\n{name.title()}'s {favorite_text}")
    for language in languages:
        print(f"\t{language.title()}")