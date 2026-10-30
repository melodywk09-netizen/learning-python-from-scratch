#Python variables 
"""
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
"""

#variables

x=int(input("enter value one :"))
y=int(input("enter value two : "))
z=x*y
a=x+y
b=x**y
c=x/y
d=x//y
e=x-y
f=x%y
print("product of value one and value two",z)
print("sum of value one and value two", a)
print("exponent of value one and value two",b)
print("division of value one and value two",c)
print("the integer (whole number) after the divsion of value one and value two",d)
print("diffrence of value one and value two",e)
print("the remainder after division of value one and value two",f)