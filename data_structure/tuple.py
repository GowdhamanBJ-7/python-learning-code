words = ('apple', 'banana', 'cherry')
print(words[0])    # apple
print(words[-1])   # cherry


print(words[0:2])   # ('apple', 'banana')

t1 = (1, 2)
t2 = (3, 4)
print(t1 + t2)      # (1, 2, 3, 4)
print(t1 * 2)       # (1, 2, 1, 2)


t = (1, 2, 2,1, 3 ,3,6)
print(t.count(2))   # 2

print(t.index(3))   # 4 (position of first occurrence)

t = ('python', 'java', 'c++', 'go')
# Your code here
print(t[-1])

fruits = ('apple', 'banana', 'apple', 'cherry', 'apple')
# Your code: use count()

lst = [1, 2, 3]
tpl = tuple(lst)

print(tpl)      # Output: (1, 2, 3)
print(type(tpl))  # Output: <class 'tuple'>

t = (1, [2, 3])
t[1].append(4)
print(t)  # (1, [2, 3, 4])


