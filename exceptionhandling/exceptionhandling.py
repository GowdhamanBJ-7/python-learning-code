try:
    x = 5 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

#----

try:
    x = 1 / 0
except:
    print("Some error")

#---
try:
    num = int("abc")
except ValueError:
    print("Invalid number")
except TypeError:
    print("Wrong type used")


try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print("You entered:", num)
finally:
    print("This always runs.")


# def set_age(age):
#     if age < 0:
#         raise ValueError("Age cannot be negative")
#     print("Age is set to", age)

#set_age(-3)  # Raises ValueError

#raise
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    print("Age is set to", age)

try:
    set_age(-5)
except ValueError as e:
    print("Handled:", e)

def convert_and_divide(a, b):
    return int(a) / int(b)

try:
    result = convert_and_divide("10", "i")  # Raises ZeroDivisionError
except ValueError:
    print("Conversion failed!")
except ZeroDivisionError:
    print("Cannot divide by zero")
