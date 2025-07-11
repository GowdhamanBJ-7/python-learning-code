# A lambda function to add two numbers
add = lambda x, y: x + y
print(add(4,8))

#higher order function
def first():
    print('first function')

def second():
    print('second function')

def higher(first,second):
    first()
    second()

higher(first,second)



num=[1,2,3,4,5]
square=map(lambda x: x**2 , num)
print (square)
#Output: <map object at 0x000001C92726BAC0>
print (list(square))
#Output: [1, 4, 9, 16, 25]

def cube(x):
    return x**3
cube = map(cube, num)
print(cube)
print(list(cube))

#filter
number = [1,2,3,4,5,67]
even = filter(lambda num1: num1 % 2==0, number)
print(list(even))

programming = ['python','java','c++','c']
programming_len = filter(lambda x: len(x)>5,programming)
print(list(programming_len)) #output ['python']

#reduce
from functools import reduce
nums = [1, 2, 3, 4]
result = reduce(lambda x,y: x+y, nums)
print(result)  # 10

#Using an initializer
nums = [1, 2, 3]
result = reduce(lambda x, y: x + y, nums, 10)  # starts from 10 (initializer)
print(result)  # 16


#flatten list
from itertools import chain

nested = [[1,2],[3,4],[5,6]]
flattened = list(chain.from_iterable(nested))
print(flattened) #[1, 2, 3, 4, 5, 6]


flat_map = list(chain.from_iterable(map(lambda x: x, nested)))
print(flat_map)


sentences = ["hello world", "python is fun"]
# flatMap: split each sentence into words and flatten the result
words = list(chain.from_iterable(map(str.split, sentences)))
print(words)  # ['hello', 'world', 'python', 'is', 'fun']
