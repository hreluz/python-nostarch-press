print('------- Tuples ---------')
# Tuples do not change
dimensions = (200, 50, 500, 350)
print(dimensions[0])
print(dimensions[1])

my_one_tuple = (3,)
print(my_one_tuple[0])

print('\n\n\n')
for dimension in dimensions:
    print(dimension)

# Cannot change value of a tuple, but you can reassign
dimensions = (200, 400)
print('\nOriginal dimensions')
for dimension in dimensions:
    print(dimension)

dimensions = (600, 700)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)