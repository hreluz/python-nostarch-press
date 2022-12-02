words = input('Enter the phrase or word you want to search: ')

try:
    count = 0
    with open('hamlet.txt') as f:
        lines = f.readlines()

    for line in lines:
        count += line.lower().count(words)

except FileNotFoundError:
    pass
else:
    print(f"The word was found {count} times")

