cars = ['bmw', 'audi', 'toyota', 'subaru']
print('------ Order list ASC, altering current list -------')
cars.sort()
print(cars)
print('------- Order list DESC, altering current list -------')
cars.sort(reverse=True)
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print('\n\n\n---- Order list ASC, without altering list -----')
print('Here is the original list')
print(cars)
print('\n Here is the sorted list:')
print(sorted(cars))
print('Here is the original list again')
print(cars)


print('\n\n --- Printing a list in reverse order ----')
# reverse the list order, but it does not order it asc or desc
print(cars)
cars.reverse()
print(cars)

print('\n\n ---- Length of a List ----')
print(len(cars))

print('\n\n\n --- Homework ----')
places = ['Estados Unidos', 'Puerto Rico', 'Brasil', 'Paraguay', 'Argentina', 'Colombia']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
