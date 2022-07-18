superheroes = ['Batman', 'Superman', 'Shazam', 'Green Lantern']
print(superheroes[0].lower())
print(superheroes)

message = f'Hello to the best superheroe ever, I mean {superheroes[0].title()}'
print(message)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

print('\n--- Adding Flash to Superheroes ---')
superheroes.insert(1,'Flash');
print(superheroes)

print('\n--- Removing Flash from Superheroes ---')
del superheroes[1]
print(superheroes)

print('\n--- Popping last value ----')
last_superheroe = superheroes.pop()
print(last_superheroe)
print(superheroes)


print('\n--- Popping from index 0 -----')
first_superheroe = superheroes.pop(0)
print(first_superheroe)
print(superheroes)

print('\n ---- Removing by value: Shazam -----')
superheroes.remove('Shazam')
print(superheroes)
#Removes only deletes the first coincidence, not all of em


print('\n\n--- Homework ----')
guests = ['Manuel', 'Zoila', 'Karla', 'Reni']
print(guests)
print(f'{guests[1]} cannot make it for dinner')
guests[1] = 'Clau'
print(f'{guests[1]} will go instead ')

guests.append('Lucho')
guests.append('Aurora')
guests.append('Patty')
guests.insert(0,'Ofelia')
guests.insert(3,'Fabi')
guests.append('Fabio')
print(guests)

print('Now you can only invite 2 people')
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
guests.pop()
print(guests)
del guests[1]
del guests[0]
print(guests)