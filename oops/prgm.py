class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

p1 = person("Arun",34)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Bala", 36)
p1.myfunc()