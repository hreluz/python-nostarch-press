# print("\n\nThe while loop")
# current_number = 1
#
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
#
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter  'quit' to end the program"


# print("\n\nLetting hte User choose when to quit")
# message = ""
#
# while message != 'quit':
#     message = input(prompt)
#     print(message)
#

# print("\n\nUsing a Flag")
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.)"
#
# while True:
#     city = input(prompt)
#
#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}")


print("\n\nUsing continue in a loop")
current_number = 0
while current_number < 10:
    current_number +=1
    if current_number % 2 == 0:
        continue

    print(current_number)