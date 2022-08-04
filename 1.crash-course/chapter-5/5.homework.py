usernames = ['staff', 'admin', 'supervisor', 'accountant', 'assistant', 'junior']

if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again")

current_users = ['Batman', 'Superman', 'Green Lantern', 'Wonder Woman', 'Flash', 'Nightwing']
new_users = ['Black Adam', 'Shazam', 'Cybork', 'Robin', 'NightwING']

for_comparison = [current_user.lower() for current_user in current_users]

for new_user in new_users:
    if new_user.lower() in for_comparison:
        print(f"The user {new_user} is already in the current users")

numbers = list(range(1, 10))
for number in numbers:
    if number == 2:
        print(f"{number}nd")
    else:
        print(f"{number}th")
