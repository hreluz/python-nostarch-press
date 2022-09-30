def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello there {username}!")


greet_user('Hector')

print("\n\nPositional Arguments")


def describe_pet(animal_type, pet_name):
    """"Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('dog', 'Hachiko')
describe_pet('cat', 'Garfield')


def describe_pet_with_keyword_arguments(pet_name, animal_type='dog'):
    """"Display information about a pet"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet_with_keyword_arguments(animal_type='dog', pet_name='Hachiko')
describe_pet_with_keyword_arguments(pet_name='Garfield', animal_type='cat')
describe_pet_with_keyword_arguments('Beethoven')


def make_shirt(size='L', message="Be happy"):
    print(f"\nYour T-shirt size is: {size}")
    print(f"The message on your shirt is: {message}")


make_shirt(size='S', message='I love python')
make_shirt(size='XL')
