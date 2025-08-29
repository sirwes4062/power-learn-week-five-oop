class Smartphone:
    def __init__(self, brand, model, battery):
        self.brand = brand              
        self.model = model
        self.__battery = battery       

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_battery(self):
        return f"Battery level: {self.__battery}%"

    def charge(self, amount):
        self.__battery = min(100, self.__battery + amount)
        print(f"{self.brand} {self.model} charged. {self.get_battery()}")


class SmartPhoneWithCamera(Smartphone):
    def __init__(self, brand, model, battery, camera_megapixels):
        super().__init__(brand, model, battery)  
        self.camera_megapixels = camera_megapixels

    def call(self, number):
        print(f"📱 {self.brand} {self.model} (with camera) is making a video call to {number}...")

    def take_picture(self):
        print(f"Picture taken with {self.camera_megapixels}MP camera!")


phone1 = Smartphone("Samsung", "Galaxy S23", 70)
phone2 = SmartPhoneWithCamera("Apple", "iPhone 15", 50, 48)

phone1.call("123-456-789")
print(phone1.get_battery())
phone1.charge(20)

print()

phone2.call("987-654-321") 
phone2.take_picture()
phone2.charge(40)

class Vehicle:
    def move(self):
        print("This vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving")
class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

my_car = Car()
my_plane = Plane()
my_boat = Boat()

vehicles = [my_car, my_plane, my_boat]

for v in vehicles:
    v.move()
