
#function
def laptop(name):
    print("company,", name)

laptop("hp")
laptop("lenovo")

def greet(name="Guest"):
    print("Hello,", name)

greet()         # Hello, Guest
greet("Sam")    # Hello, Sam

# def square(n):
#     return n * n
#
# num = int(input("Enter a number: "))
# print("Square is:", square(num))