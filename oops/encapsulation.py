class Employee:
    def __init__(self, name, salary):
        self.name = name           # public
        self.__salary = salary     # private

    def display_info(self):
        print(f"Name   : {self.name}")
        print(f"Salary : {self.__salary}")

    def update_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary update")

    def get_salary(self):
        return self.__salary

# Usage
emp = Employee("Ravi", 50000)
emp.display_info()

emp.update_salary(60000)
print("Updated Salary:", emp.get_salary())

# Trying to access private variable directly
print(emp.name)
#print(emp.__salary)          #Error (AttributeError)
print(emp._Employee__salary) #Accessible via name mangling
