print("Press q to quit")

while True:
    try:
        number_1 = input('Enter a number: ')
        number_2 = input('Enter another number: ')

        if number_1 == 'q' or number_2 == 'q':
            break

        total = int(number_1) + int(number_2)
    except ValueError:
        print("Both values must be numeric")
    else:
        print(f"Total is {total}")
