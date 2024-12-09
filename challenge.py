class Car:
    def move(self):
        return "Driving 🚗"

class Plane:
    def move(self):
        return "Flying ✈️"

class Boat:
    def move(self):
        return "Sailing 🚤"

class Bicycle:
    def move(self):
        return "Pedaling 🚲"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat(), Bicycle()]  # Create a list of vehicle objects

for vehicle in vehicles:
    print(vehicle.move())  # Call the move method, demonstrating polymorphism





