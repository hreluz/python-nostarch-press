print('------ Slice ---------')
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[0:5:2])

print('\n\n------- Looping ---------')
print('Here are the first three players on my team:')
for player in players[0:3]:
    print(player.title())

print('\n\n------- Copying a List ---------')
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('lomo saltado')
friend_foods.append('tallarin saltado')

print('My favourte foods are:')
print(my_foods)
print("\n My friend's favorite foods are:")
print(friend_foods)

another_friend_foods = my_foods
my_foods.append('cannoli')
print(another_friend_foods)


