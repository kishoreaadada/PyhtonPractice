from functools import reduce


def greatestnumber(*args):
    input_nums = list(args)
    input_nums.sort()
    return input_nums[-1]


def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False


def isodd(num):
    if num % 2 == 1:
        return True
    else:
        return False


def ispositive(num):
    if num >= 0:
        return True
    else:
        return False


def isnegative(num):
    if num < 0:
        return True
    else:
        return False


def print_course_fee(course):
    if course.lower() == 'big data':
        print("Big data course fee is 35000")
    elif course.lower() == 'spark':
        print("Spark course fee is 30000")
    elif course.lower() == 'datascience':
        sub_course = input()
        if sub_course.lower() == 'machine learning':
            print("machine learning course fee is 25000")
        elif sub_course.lower() == 'deep learning':
            print("deep learning course fee is 30000")
        else:
            print("fee for both machine and deep learning is 50000")
    else:
        print("Sorry we are not providing any course in your choice")


def ispalindrome(name):
    if name == "".join(reversed(name)):
        return True
    else:
        return False


def getinstance(name):
    if isinstance(name, int):
        return int
    elif isinstance(name, str):
        return str


def add(*args):
    try:
        return reduce(lambda x, y: x + y, args)
    except TypeError:
        return reduce(lambda x, y: int(x) + int(y), args)


def multiply(*args):
    try:
        return reduce(lambda x, y: x * y, args)
    except TypeError:
        return reduce(lambda x, y: int(x) * int(y), args)


def subtract(*args):
    try:
        return reduce(lambda x, y: x - y, args)
    except TypeError:
        return reduce(lambda x, y: int(x) - int(y), args)


def divide(*args):
    try:
        return reduce(lambda x, y: x / y, args)
    except TypeError:
        return reduce(lambda x, y: int(x) / int(y), args)


def calculator(a, b, operation='add'):
    switcher = {
        'add': add(a, b),
        'subtract': subtract(a, b),
        'multiply': multiply(a, b),
        'divide': divide(a, b),
        'all': (add(a, b), subtract(a, b), multiply(a, b), divide(a, b))
    }
    return switcher.get(operation, add(a, b))


def stringactions(name):
    print(name.capitalize())
    print(name.upper())
    print(len(name))
    print(len(name.split(" ")))
    print(name.endswith('s'))
    print(name.replace('e', 'a'))
