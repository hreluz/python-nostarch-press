age = 17

if age >= 18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote")

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}")

print('\n\nTesting Multiple Conditions')
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')

if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')

if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')

print('\nFinished making your pizza')