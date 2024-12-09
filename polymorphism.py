
class Smartphone:
    def speak(self):
        return "whistling"

class Phone:
    def speak(self):
        return "ringing"

# Polymorphism in action
devices = [Smartphone(), Phone()]  # Create a list of objects from both classes

for device in devices:
    print(device.speak())  # Call the speak method, demonstrating polymorphism
