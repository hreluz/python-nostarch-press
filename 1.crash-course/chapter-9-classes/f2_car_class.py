"""A class that can be used to represent a car."""


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(40)
# my_new_car.read_odometer()
# my_new_car.update_odometer(20)
# my_new_car.read_odometer()
#
# my_used_card = Car('subaru', 'outback', 2015)
# print(my_used_card.get_descriptive())
# my_used_card.update_odometer(23_500)
# my_used_card.read_odometer()
# my_used_card.increment_odometer(100)
# my_used_card.read_odometer()
