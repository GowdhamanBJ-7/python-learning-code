
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


#while loop --------------------------------------------------------------
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