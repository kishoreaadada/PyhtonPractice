#variable declaration and operation
x=100
y=10
#division
print(x/y)
#floor division
print(x//y)
#multiplication
print(x*y)
#addition
print(x+y)
#subtraction
print(x-y)
#remainder
print(x%y)
#incremental/decrement operators doesn't support in python
print(++x)
z=++x
print(z,x)
z=x
z+=x
print(z)
z-=x
print(z)
print(--y)
#Dynamically typed example
y=str(x)
print(x, type(x))
print(y, type(y))
#Strongly typed exaple. Here x is of int type and y is of str type, so it doesn't allow addition of x,y
#print(x+y)
#declare multiple variables on single line
a,b,c,d=10,23,34,54
print(a,type(a),b,type(b),c,type(c),d,type(d))
a,b,c='string',23,[1,2,3]
print(a,type(a),b,type(b),c,type(c))

#Python variables are case sensitive
age, name=28, 'Kishore'
#print(Age, name) -- throws unresolved reference error
print(age,name)

#Python naming conventions
'''
variable should not start with a numeric digit
variable must start with a letter or underscore
variable name can only contain alpha-numeric characters or underscores, it should not contain any other special characters
variable in python are case sensitive
'''
Age, age = 20, 23
_address_ = "Naidu's street, kittalapdu"
print(Age,age, _address_)
#$specailVar=12 --throws invalid syntax error
#1two=12 -- throws invalid decimal literal error

#Arithmatic operators
x,y=100,10
print(x/y)
print(x//y)
print(x*y)
#x power y
print(x**y)
print(x+y)
print(x-y)
print(abs(y-x))
print(x%y)

#Relational/comparison Operators:
print(x==y, x==y*10)
print(x!=y, x!=y*10)
print(x>=y, x>y)
print(x<=y, x<y)

#Logical Operators
print(x==y or x==y*10, x==y | x==y*10)
print(x==y and x==y*10, x==y & x==y*10)
print(not x==y*10, x!=y*10)
