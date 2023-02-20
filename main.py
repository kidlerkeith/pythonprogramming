import operator
x=operator.add(12,34)
print (x)

#functions.subtract()
y= operator.subtract(45,89)
print (y)

from operator import add
x= add (23,45)

print(x)
from operator import subtract
y=(89,58)

import others
others.cube(5)

#get 2 numbers
num1=eval(input("enter number1 "))
num2=eval(input("enter number 2"))
operator= input("enter operator")
if operator=="+":
    x=operator.add(num1,num2)
    print(x)
if operator=="-":
    x= operator.subtract(num1,num2)
    print(x)
if operator =="/":
    x = operator.divide(num1,num2)
    print(x)
elif operator=="*":
    x=operator.multiply(num1,num2)
elif operator =="3":
    x=others.cube(num1)

    print (x)

import operator
import others
import trig

#build a better calcultor
x=others.cube(9)
y=operator.add(23,56)
""
#get numbers
operator =input("enter operator")
if operator=="cube":
    num =eval(input("enter a number"))
    x=others.cube(num)
    print(x)

elif operator =="sin":
    angle=eval(input("enter angle in degrees"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)

elif operator=="tan":
    angle=eval(input("enter angle in degrees"))
    print(trig.get_tan(angle))


elif operator== "cos":
    angle= eval(input("enter angle in degrees"))
    print(trig.get_cos(angle))






























