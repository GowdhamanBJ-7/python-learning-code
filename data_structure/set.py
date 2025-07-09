s = {1, 2, 3, 4}
print(s)  # {1, 2, 3, 4}

# Automatically removes duplicates
s2 = {1, 2, 2, 3, 4}
print(s2)  # {1, 2, 3, 4}

for item in s:
    print(item)

s.add(5)
print(s) #{1, 2, 3, 4, 5}

s.update([6, 7, 8])
print(s) #{1, 2, 3, 4, 5, 6, 7, 8}

s.remove(2)
print(s) #{1, 3, 4, 5, 6, 7, 8}
#s.remove(10)  #element not present
print(s)
# Traceback (most recent call last):
#
#     s.remove(10)
#     ~~~~~~~~^^^^
# KeyError: 10

s.discard(10)
print(s)

s.pop()
s.clear()
print(s) #set()