from f1_dog_class import Restaurant
from f3_electric_car_inheritance import ElectricCar, Car


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        for flavor in self.flavors:
            print(flavor)


ice_cream = IceCreamStand('Zugatti', 'desserts', ['lemon', 'strawberry', 'passion fruit'])
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.show_flavors()


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"The user name is {self.first_name}, and the last name is {self.last_name}")

    def greet_user(self):
        print(f"Say hello to my new friend, {self.first_name} {self.last_name}")


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('The privileges are:')
        for privilege in self.privileges:
            print(f"\t {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges


admin = Admin('Tony', 'Montana', Privileges(['sell', 'buy']))
admin.describe_user()
admin.privileges.show_privileges()
