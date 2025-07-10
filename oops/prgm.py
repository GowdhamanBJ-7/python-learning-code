class person:
    def __init__(self,name, age,country='India'):
        self.name1 = name
        self.age = age
        self.country = country
p1 = person("Arun",34)
p2 = person('John',33,'UK')
print(p2.country)
print(p1.country)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bala", 36)
p1.myfunc()

class InstanceClass:
    def __init__(self):
        pass
    def display(self):
        print('class method')

obj1 = InstanceClass()
obj1.display()


#super keyword
class Parent:
    def greet(self):
        print("Hi from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Call parent method
        print("Hi from Child")

c = Child()
c.greet()
