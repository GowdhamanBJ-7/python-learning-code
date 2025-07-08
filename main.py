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

#for loop
#a. for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#b. for loop over string
word = 'python'
for i in word:
    print(i)

#c for loop using range()
for i in range(5):  # 0 to 4
    print(i)

#with range(start, stop, step)
for i in range(0,10,2): #0 2 4 6 8
    print(i)

#reverse loop
for i in range(10,0,-1): #10 to 1
    print(i)

for i in range(10,0,-2): #10 8 6 4 2
    print(i)


#while loop
i = 20
while i <= 30:
    print(i)
    i+=2

#20 22 24 26 28 30

'''while True:
    print('infinite loop')'''

number = 123
reverseNumber = 0

while number > 0:
    final = number % 10
    reverseNumber = (reverseNumber * 10) + final
    number = number // 10
print(reverseNumber)

num = 5
fact = 1
for i in range(1,num+1):
    fact  *= i
print(fact)

n=5
f = 1
while n > 0:
    f = f * n
    n-=1
print('while fact',f)

#prime number
numb = 9
for i in range(2,numb):
    if numb % i == 0:
        print('not a prime')
        break
else:
    print('prime')

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

import prime_module
print(prime_module.is_prime(6))

print(prime_module.add(3,9))

import math

print(math.sqrt(16))    # 4.0
print(math.pi)          # 3.1415
