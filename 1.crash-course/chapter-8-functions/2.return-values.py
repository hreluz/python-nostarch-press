def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()


musician = get_formatted_name('JimmY', 'Hendrix')
print(musician)
musician = get_formatted_name('John', 'Lee', 'Hooker')
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', 27)
print(musician)

musician = build_person('Hector', 'Tricoche')
print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")

    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

