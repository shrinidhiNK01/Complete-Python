print("Good Morning, World!")
a=10
b="Shrinidhi"
c=23.98
print("I am:",a," ",b," ",c)

# This is a single line comment
""" welnsvionvlfoweinowienvo ===> Multiline Comment """  

string=""" welnsvionvlfowein           |
sfaaaaaaaaaaaaaaaaaaaaaaaaaaa          |---> DocStrings
owienvo ===> Multiline Comment """    #|
print(string)                         #|

# f-strings

Actor="Thalapathy Vijay"
Actress="Thrisha"
Movie="Leo"
Director="Lokesh Kanagaraj"

print(f"Director:{Director} is Making a Movie {Movie} with {Actor} and {Actress}")

# Id's 
print(id(Actor))
print(id(Actress))
print(id(Movie))
print(id(Director))

# Keywords
import keyword as k
print(k.kwlist)

# Lists
a=["Vijay","Ajith","Suriya","Karthi",1,2,3,10.90,45.78,True,False]
print(a)
print(type(a))

i=0
while(i<len(a)):
    print(a[i])
    i=i+1

#Primitive Data Types
x=10
y=23.98
z="Shrinidhi"
a=True
print(type(x))
print(type(y))
print(type(z))
print(type(a))

#Non Primitive Data Types
b=[1,2,3,4,5]
c=(1,2,3,4,5)
d={"Name":"Shrinidhi","Age":23,"City":"Bangalore"}
print(type(b))
print(type(c))
print(type(d))

#Type Casting
x=10
u=bool(x)
y=float(x)
z=str(x)
print(type(x))
print(type(y))
print(type(z))
print(type(u))

# Input
name=input("Enter your name:")
age=int(input("Enter your age:"))
Budget=float(input("Enter your budget:"))
print(f"Name:{name} Age:{age} Budget:{Budget}")

# We cannot concatenate string and integer directly
# print("My name is "+name+" and I am "+age+" years old") # This will give an error because age is an integer and we cannot concatenate string and integer directly
print("My name is "+name+" and I am "+str(age)+" years old") # This will work because we are converting age to string before concatenating      

# Area of Rectangle
length=float(input("Enter the length of rectangle:"))
breadth=float(input("Enter the breadth of rectangle:"))
area=length*breadth
print(f"The area of rectangle is: {area}")

# numlock+alt+0178 => ², 

#Assignment operators
x=10
x+=5 # x=x+5
print(x)
x-=3 # x=x-3
print(x)
x*=2 # x=x*2
print(x)
x/=4 # x=x/4
print(x)
x%=3 # x=x%3
print(x)
x**=2 # x=x**2
print(x)

# Mathematical operators
x=3.1457965659
y=10
z=20
print(round(x,2)) # round to 2 decimal places
print(round(x,4)) # round to 4 decimal places
print(round(x)) # round to nearest integer
print(abs(-10)) # absolute value
print(pow(2,3)) # 2 raised to the power of 3
print(10//3) # floor division
print(10%3) # modulus operator
print(sum([x,y,z])) # sum of x,y,z
print(min(x,y,z)) # minimum of x,y,z
print(max(x,y,z)) # maximum of x,y,z

# Importing math module
import math as m
print(m.sqrt(16)) # square root of 16
print(m.ceil(3.14)) # ceiling of 3.14
print(m.floor(3.14)) # floor of 3.14
print(m.factorial(5)) # factorial of 5
print(m.gcd(10,15)) # greatest common divisor of 10 and 15
print(m.lcm(10,15)) # least common multiple of 10 and 15
print(m.pi) # value of pi
print(m.e) # value of e


# Assignment = Calculate Circumference of a Circle

import math as m
# 2 pi r
radius=float(input("Enter the radius of Circle:"))
circumference=2*m.pi*radius
circumference2=round(circumference,2)

print(f"The circumference of Circle is: {circumference2}")

age=int(input("Enter your age:"))
if age>=18:
    print("You can watch porn")
    if age>=25:
        print("You can Fuck anybody")
        if age>=45:
            print("National Award for Best Jhony")
elif age>=13:
    print("You can watch cartoons")
else:
    print("You cannot watch porn or cartoons")