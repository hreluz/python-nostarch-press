superheroes = ['batman', 'superman', 'flash', 'wonder woman', 'green lantern', 'cyborg']
print(f'The first three items are: {superheroes[0:3]}')
print(f'The items from the middle of the list are: {superheroes[2:5]}')
print(f'The last three items in the list are: {superheroes[-3:]}')

pizzas = ['american', 'germany', 'hawaiian', 'nordic', 'peruvian']
friend_pizzas = pizzas[:]
pizzas.append('all meat')
print(f'My favourite pizzas are: {pizzas}')
print(f'My friend\'s favourite pizzas are: {friend_pizzas}')