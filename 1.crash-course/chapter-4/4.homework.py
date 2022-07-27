
print('***** Homework *****')
for value in range(1,21):
    print(value)

numbers = []
for value in range(1, 100000):
    numbers.append(value)
    print(value)

print('**** min value from numbers *****')
print(min(numbers))
print('**** max value from numbers *****')
print(max(numbers))
print('**** sum value from numbers *****')
print(sum(numbers))


for value in range(2,21,2):
    print(value)

for value in range(3, 31, 3):
    print(value)

for value in range(1,11):
    print(value**3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)