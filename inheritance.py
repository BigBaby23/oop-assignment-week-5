
class Smartphone:
    def __init__(self, ram):
        self.ram = ram  # Initialize the RAM attribute

class Phone(Smartphone):  # Inherit from Smartphone
    pass

# Create an object of the Phone class
phone = Phone(4)
print(phone.ram)  # Output: 4
