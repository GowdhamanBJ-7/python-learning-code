num = 7
print(type(num))

hello = 'value'

x = float(1)  # 1.0
y = int(2.8)  # 2
z = int("3")  # 3
a = str(2)    # "2"
#b = int("abc")

marks = 76
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade F")

#nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Access granted")
    else:
        print("No ID, access denied")
else:
    print("Too young")



import prime_module
print(prime_module.is_prime(6))

print(prime_module.add(3,9))

import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.1415
