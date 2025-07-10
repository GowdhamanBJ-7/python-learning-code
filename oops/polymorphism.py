#Polymorphism in Functions
def add(a,b):
    return a+b

print(add(3,7))
print(add("hello, ","string"))

#class polymorphism
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "781")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

class Laptop:
    def specs(self):
        print("Laptop: 16GB RAM, 512GB SSD")

class Mobile:
    def specs(self):
        print("Mobile: 8GB RAM, 128GB Storage")

devices = [Laptop(), Mobile()]

for device in devices:
    device.specs()
