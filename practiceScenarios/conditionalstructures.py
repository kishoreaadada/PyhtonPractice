

def greatest_number(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def print_even_negative(x):
    if x % 2 == 0 and x < 0:
        print(str(x) + " is even and negative")
    elif x % 2 == 0 and x > 0:
        print(str(x) + " is even but, not negative")
    elif x % 2 != 0 and x < 0:
        print(str(x) + " is not even but, negative")
    else:
        print(str(x) + " is neither even nor negative")


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


def check_palindrome(name):
    print("".join(reversed(name)))
    if name == "".join(reversed(name)):
        print("{} is palindrome".format(name))
    else:
        print("{} is not palindrome".format(name))


#print("Enter three values to find greatest number")
#a, b, c = int(input()), int(input()), int(input())
#print("greatest of given three numbers is: {}".format(greatest_number(a,b,c)))
#print("Enter your number to check whether even or negative")
#number = int(input())
#print_even_negative(number)
#print("Enter your course to check the fee")
#course = input()
#print_course_fee(course)
print("Enter your name to check whether palindrome or not")
name = int(input())
print(isinstance(name, str))
print(isinstance(name, int))
