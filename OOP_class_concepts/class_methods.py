# Define a class with a class method
class MyClass:
    class_attribute = 0

    @classmethod
    def class_method(cls, value):
        # Access class attributes and methods within the class method
        cls.class_attribute += value
        print(f"Class attribute value: {cls.class_attribute}")

# Call the class method without creating an instance of the class
MyClass.class_method(5)
MyClass.class_method(10)
