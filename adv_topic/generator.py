def simple_generator():
    yield "Hello"
    yield "World"
    yield "!"

# Using the generator
for value in simple_generator():
    print(value)


def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
gen = count_up_to(4)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # Raises StopIteration

#using loop
for i in gen:
    print(i)