def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


greet_users(['hannah', 'ty', 'margot'])


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(f"The unprinted design list is : {unprinted_designs}\n")

completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(f"The unprinted design list is : {unprinted_designs}")

