List1 = [1, 2,  3, "GFG", 2.3]
print(List1)

List2 = [['first', 'second'], ['third']]
print("\nMulti-Dimensional List: ")
print(List2)
print(List2[0])

fruits = ['apple', 'banana', 'cherry']
#modifying elements
fruits[1] = 'mango'
print(fruits) #['apple', 'mango', 'cherry']


#append
fruits.append('orange')
print(fruits)  #['apple', 'mango', 'cherry', 'orange']

fruits.insert(1,"grape")
print(fruits) #['apple', 'grape', 'mango', 'cherry', 'orange']

fruits.extend(["lemon","kiwi"])
print(fruits) #['apple', 'grape', 'mango', 'cherry', 'orange', 'lemon', 'kiwi']


#remove
fruits.remove("orange")
print(fruits)  #['apple', 'grape', 'mango', 'cherry', 'lemon', 'kiwi']

#pop()
fruits.pop()
print(fruits) #['apple', 'grape', 'mango', 'cherry', 'lemon']

fruits.pop(2) #fruits = ['apple', 'grape', 'mango', 'cherry', 'lemon']
print(fruits) #['apple', 'grape', 'cherry', 'lemon']

fruits.clear()
print(fruits) #[]


fruits = ['apple', 'banana', 'cherry']

#index() – Get index of first match
print(fruits.index("apple"))  #0
print(fruits.index("cherry")) #2

#count() – Count occurrences
numbers = ['one', 'two', 'two', 'two', 'three', 'two']
print(numbers.count('two'))  # 4

num_value = [2, 3, 6, 6, 5]
set_value = set(num_value)
print('reverse', list(set_value))
setValue =list(set_value)
setValue.sort(reverse=True)
print('reverse', setValue[2])

numbers.sort() #numbers = ['one', 'two', 'two', 'two', 'three', 'two']
print(numbers) #['one', 'three', 'two', 'two', 'two', 'two']

numbers.sort(reverse=True)
print(numbers) #['two', 'two', 'two', 'two', 'three', 'one']

fruits.reverse() #fruits = ['apple', 'banana', 'cherry']
print(fruits)    #['cherry', 'banana', 'apple']

copy1 = fruits.copy()       # Safe copy
copy2 = fruits[:]           # Also works


print(copy1)
print(copy2)
