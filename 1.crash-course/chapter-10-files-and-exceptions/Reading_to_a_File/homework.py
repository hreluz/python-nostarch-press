filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()

print(contents)

lines = []
with open(filename) as file_object:
    for line in file_object:
        lines.append(line)
        print(line)
        print('---------')

print(lines)