# Define a class called "Person"
class Person:
    # Class attribute
    species = "Human"

    # Constructor method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

# Define a class called "Employee" that inherits from "Person"
class Employee(Person):
    # Constructor method
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call the parent class constructor
        self.employee_id = employee_id

    # Override the introduce method
    def introduce(self):
        super().introduce()  # Call the parent class introduce method
        print(f"I am an employee with ID {self.employee_id}.")

# Create objects from the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Create objects from the Employee class
employee1 = Employee("Charlie", 35, "E001")
employee2 = Employee("Dave", 40, "E002")

# Access class attribute
print(f"Person 1 belongs to the {person1.species} species.")
print(f"Person 2 belongs to the {person2.species} species.")

# Call instance method
person1.introduce()
person2.introduce()

# Call overridden instance method
employee1.introduce()
employee2.introduce()

# OUTPUT: 
'''
Person 1 belongs to the Human species.
Person 2 belongs to the Human species.
Hi, my name is Alice and I am 25 years old.
Hi, my name is Bob and I am 30 years old.
Hi, my name is Charlie and I am 35 years old.
I am an employee with ID E001.
Hi, my name is Dave and I am 40 years old.
I am an employee with ID E002.
'''