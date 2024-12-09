# Defining a class
class Phone:
    color= "silver"  # Attribute
    brand= "Techno"
    Model= "Spark 30"

    # Method
    def brand(self):
        print("The phone is silver in colour🚗")

# Creating an object
my_phone = Phone()
print(my_phone.color)
print(my_phone.brand)


class Phone:
    color = "silver"  # Attribute
    brand = "Techno"  # Attribute
    model = "Spark 30"  # Corrected casing for consistency

    # Method
    def show_color(self):  # Renamed method to avoid conflict
        print("The phone is silver in colour, the brand is techno Spark 30 🚗")

# Creating an object
my_phone = Phone()
print(my_phone.color)  # Access the 'color' attribute
print(my_phone.brand)  # Access the 'brand' attribute
print(my_phone.model)  #Access the model attribute
my_phone.show_color()  # Call the method

class phone:
    def __init__(self, color, model):
        self.color = color    # Instance variable
        self.model = model    # Instance variable

# Creating objects with unique attributes
car1 = phone("blue", "Techno spark 30")
car2 = phone("red", "Techo Spark 20")

print(car1.color)  # Output: blue
print(car2.model)  # Output: Techno Spark 2o


