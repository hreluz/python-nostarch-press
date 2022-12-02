
print("If you want to finish enter quit")

while True:
    name = input("What is your name?: ")
    if len(name) == 0:
        print("That is not a valid name.")
    elif name == "quit":
        break
    else:
        filename = 'guest.txt'
        with open(filename, 'a') as file_object:
            file_object.write(name+'\n')
