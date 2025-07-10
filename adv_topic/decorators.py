def logging(func):
    def wrapper():
        print('start logging..')
        func()
        print('end logging..')
    return wrapper

@logging
def add():
    print(10+2)
add()
@logging
def sub():
    print(10-2)
sub()

# log = logging(add)
# log()

# log = logging(sub)
# log()


def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(add(2,4,5,6,7,8))


def add(**kwargs):
    print(kwargs)

add(num1=10, num2=2)

def add(**kwargs):
    sum = 0
    for key, value in kwargs.items():
        sum+=value
    print(sum)

add(num1 = 10, num2=2)