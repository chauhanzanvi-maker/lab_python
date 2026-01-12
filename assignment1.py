Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
print("hello!! , welcome to python")
hello!! , welcome to python
a=(input("Enter first number:"))
Enter first number:2
b=(input("Enter second number:"))
Enter second number:4
sum=a+b
print("Addition=",sum)
Addition= 24
num=int(input("Enter a number:"))
Enter a number:21
if num%2==0:
    print("Even num:")
else:
    print("odd num:")

    
odd num:
year=int(input("Enter year:"))
Enter year:2024
if(year %4==0 and year % 100!=0)or(year % 400=0):
    
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
if(year %4==0 and year % 100!=0)or(year % 400==0):
   print("leap year")
else:
    print("not a leap year")

    
leap year
import math
print("pi value=",math.pi)
pi value= 3.141592653589793
name=input("Enter your name:")
Enter your name:zanvi
print("Name",name)
Name zanvi
print("Age",age)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print("Age",age)
NameError: name 'age' is not defined
age=input("Enter age name:")
Enter age name:18
print("Age",age)
Age 18
PI=3.14 #constant value
r=int(input("Enter radius:"))
Enter radius:5
area=PI*r*r
print("Area of circle=",area)
Area of circle= 78.5
num=int(input("Enter a number:"))
Enter a number:5
square=num*num
print("square=",square)
square= 25
>>> PI=3.14
>>> r=float(input("Enter radius:"))
Enter radius:7
>>> area=PI*r*r
>>> print("area of circle=",area)
area of circle= 153.86
>>> value=input("Enter any value:")
Enter any value:python
>>> print("data type is :", type(value))
data type is : <class 'str'>
>>> import math
>>> num=int(input("Enter a number:"))
Enter a number:5
>>> print("square root",math.sqrt(num))
square root 2.23606797749979
>>> print("Factorial",math.factorial(num))
Factorial 120
>>> print("Absolute value=",abs(num))
Absolute value= 5
>>> a=int(input("Enter base:"))
Enter base:2
>>> b=int(input("Enter power:"))
Enter power:8
>>> num=int(input("Enter your number :"))
Enter your number :-4
>>> if num>0:
...     print("positive number")
... elif num<0:
...     print("nagative number")
... else:
...     print("zero")
... 
...     
nagative number
