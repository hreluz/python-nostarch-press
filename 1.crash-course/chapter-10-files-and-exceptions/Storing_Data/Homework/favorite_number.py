import json

filename = 'favorite_number.txt'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("Enter your favorite number: ")
    with open(filename, 'w') as f:
        json.dump(number, f)
    print("Your favorite number has been saved")
else:
    print(f"Your favorite number is: {number}")