print("Using range() function\n")
for value in range(1, 10):
    print(value)

for value in range(5):
    print(value)

print("Using range to make a list of numbers\n")
values = list(range(3, 8))
print(values)

even_numbers = list(range(2, 17,2))
print(even_numbers)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)

print(squares)

print(min(squares))
print(max(squares))