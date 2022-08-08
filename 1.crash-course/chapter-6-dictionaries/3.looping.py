user_0 = {
    'username': 'efermi',
    'first_name': 'enrico',
    'last': 'fermi',
}

# items() returns al ist of key-value pairs
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("\n\nLooping through all keys in a dictionary with keys()")
for name in favorite_languages.keys():
    print(name.title())
print("\n\nLooping through all keys in a dictionary by default behaviour")
for name in favorite_languages:
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages:
    print("\nErin, please take our poll!")

print("\n\nLooping through a dictionary's keys in a particular order")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

print("\n\nLooping through all values in a dictionary")
print("The following languages have been mentioned:")
values = favorite_languages.values()
for language in values:
    print(language.title())

print("\n\nPrinting languages without repeating:")
values = favorite_languages.values()
for language in set(values):
    print(language.title())

