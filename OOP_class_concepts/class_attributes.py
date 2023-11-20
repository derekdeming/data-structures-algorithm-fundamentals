class Car:
    """
    A class representing a car.

    Attributes:
        manufacturer (str): The manufacturer of the car.
        total_cars (int): The total number of cars created.
        fuel_types (list): The list of fuel types supported by the car.

    Methods:
        __init__(model, color): Initializes a new instance of the Car class.
        add_fuel_type(fuel_type): Adds a new fuel type to the list of supported fuel types.
        get_total_cars(): Returns the total number of cars created.
    """

    manufacturer = "Unknown"
    total_cars = 0
    fuel_types = []

    def __init__(self, model, color):
        """
        Initializes a new instance of the Car class.

        Args:
            model (str): The model of the car.
            color (str): The color of the car.
        """
        self.model = model
        self.color = color
        Car.total_cars += 1

    @classmethod
    def add_fuel_type(cls, fuel_type):
        """
        Adds a new fuel type to the list of supported fuel types.

        Args:
            fuel_type (str): The fuel type to be added.
        """
        cls.fuel_types.append(fuel_type)

    @staticmethod
    def get_total_cars():
        """
        Returns the total number of cars created.

        Returns:
            int: The total number of cars created.
        """
        return Car.total_cars

# Create instances of Car class
car1 = Car("Toyota", "Blue")
car2 = Car("Honda", "Red")

# Accessing fundamental class attribute
print(f"Car manufacturer: {Car.manufacturer}")

# Accessing advanced class attribute
Car.add_fuel_type("Gasoline")
Car.add_fuel_type("Diesel")
print(f"Available fuel types: {Car.fuel_types}")

# Accessing instance attributes
print(f"Car 1: {car1.model}, {car1.color}")
print(f"Car 2: {car2.model}, {car2.color}")

# Accessing total cars using static method
print(f"Total cars: {Car.get_total_cars()}")
