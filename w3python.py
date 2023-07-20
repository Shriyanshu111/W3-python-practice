print("Hello, World!")

>>> print("Hello, world")

if 5>2:
  print("Five is greater than two!")

x= 5
y= 4
print(y)

#This is a comment
print("Hello, World")

x=5
y="jhon"
print(x)
print(y)

x=4         # x is of int
x= "Sally"  # x is now of type str
print(x)

x= str(3)   # x will be '3'
y= int(3)   # y will be 3
z= float(3) # z will be 3.0

x=5
y="jhon"
print(type(x))
print(type(y))

x= "jhon"
# is the same as
x= 'jhon'

A= 4
a= "shriyanshu"
#A will not overwrite a

myvar= "jhon"
my_var= "John"
_my_var = "jhon"
myVar = "jhon"
MYVAR = "jhon"
myvar2 = "jhon"

2myvar = "jhon"
my-var = "jhon"
my var = "jhon"

my_variable_name = "jhon"

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x= y=z="Orange"
print(x)
print(y)
print(z)

fruits=["apple", "Banana", "cherry"]
x, y, z= fruits
print(x)
print(y)
print(z)

x="python is awesome"
print(x)

x="python"
y="is"
z="awesome"
print(x,y,z)

x= "Python "
y= "is "
z= "awesome"
print(x + y + z)

x=5
y=10
print(x+y)

x=5
y="jhon"
print(x+y)

x=5
y="jhon"
print(x, y)

x="Awesome"
def myfunc():
  print("Python is + x")

myfunc()

x="Awesome"

def myfunc():
  x="fantastic"
  print ("python is " + x)

myfunc()

print("python is " + x)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("python is "+ x)

x="awesome"

def myfunc():
  global x
  x="fantastic"

myfunc()

print("pyhton is "+ x)

x=5
print(type(x))

x="Hey i am Shriyanshu"
print(type(x))

x=20.5
print(type(x))

x= 1j
print(type(x))

x=["apple", "banana", "cherry"]
print(type(x))

x=("apple", "banana", "cherry")
print(type(x))

x=range(6)
print(x)
print(type(x))

x= "what is your name "
print(input(x))

x={"Name":"Shriyanshu","Age":"23"}
print(type(x))

x={"apple", "banana", "cherry"}
print(type(x))

x=frozenset({"apple", "banana", "cherry"})
print(type(x))

x= True
print(type(x))

x= False
print(type(x))

x=b"Hello"
print(type(x))

x=bytearray(5)
print(x)
print(type(x))

x=memoryview(bytes(5))
print(x)
print(type(x))

x=None
print(type(x))
print(x)

x=1
y=2.5
z=1j
print(type(x))
print(type(y))
print(type(z))

x=1
y=66289703728327
z= -377239
print(type(x))
print(type(y))
print(type(z))

x=1.10
y=2.0
z=-35.35
print(type(x))
print(type(y))
print(type(z))

x=1.24234
print(type(x))

x=35e3
y=12E4
z=-35.3e54
print(type(x))
print(type(y))
print(type(z))

x= 3+5j
y= 5j
z= -5j
print(type(x))
print(type(y))
print(type(z))

x=1     # int
y=2.8   # float
z=1j    # complex

#convert int to float:
a = float(x)

#convert float to int:
b = int(y)

#convert int to complex:
c= complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1,10))

x = int(1)    # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)

x = str("s1")
print(x)

y=str(2)
print(y)

z=str(3.0)
print(z)

print('hello')

print("Hello")

a = """Hey there i am shriyanshu"""
print(a)

a = '''Hey there i am shriyanshu'''
print(a)

a="Hello, World!"
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

for x in "Shriyanshu":
  print(x)

a="Hello, World!"
print(len(a))

a="What is your name?"
print(len(a))

txt="The best things in life are free!"
print("free" in txt)

txt="Hey there i am shriyanshu"
print("shriyanshu" in txt)
print("is" in txt)

txt="Hey there i am shriyanshu"
if "shriyanshu" in txt:
  print("Yes, 'Shriyanshu' is present.")

print("is" not in txt)

if "is" not in txt:
  print("No, 'is' is not present in txt.")

b="Hello, World!"
print(b[2:5])
print(b[1:8])
print(len(b))
print(b[:5])
print(b[2:])
print(b[-8:-2])

a="Hello, World!."
print(a.upper())

b= "HELLO WORLD!"
print(b.lower())

a="   Hello, World!.     "
print(a.strip())

a="Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(","))

a= "Hello"
b= " World"

c= a+b
print(c)

d= a+ " " +b
print(d)

age = 23
txt = "My name is Shriyanshu, and I am {} "
print(txt.format(age))

quantity=5
itemno=250
price=35500
myorder= "i want {} pieces of {} for {} Rupees."
print(myorder.format(quantity,itemno,price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

a= "how are you"
a=a.capitalize()
print(a)

a="HOW ARE YOU"
a=a.casefold()
print(a)

txt= "good boy"
x=txt.center(20)
print(x)

a= "Shriyanshu"
y=a.center(25)
print(y)

a= "i love apples, apple are my favorite fruit"
b= a.count("apple")
print(b)

txt= "My name is Shriyanshu"
x=txt.encode()
print(x)

y=(txt.encode(encoding="Ascii", errors="ignore"))
print(y)

txt="Hello, Welcome to my world"
x=txt.endswith("d")
print(x)

y=txt.startswith("H")
print(y)

txt = "Hello, welcome to my world 5,11"

x = txt.endswith("11")

print(x)

txt = "H\te\tl\tl\to"
x = txt.expandtabs(4)
print(x)

y = txt.expandtabs(1)
print(y)

txt="Welcome, to my world"
x=txt.find("my")
print(x)

y=txt.find("e", 5, 10)
print(y)

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
print(txt1)

txt= "For only {price:.2f} Rupees!"
print(txt.format(price = 49))

txt2 = "My name is {fname}, I'm {age}".format(fname = "Shriyanshu", age = 23)
print(txt2)

print(10>9)
print(10==9)
print(10<9)

a=200
b=50

if b > a:
  print("b is greater than a")
else:
  print("a is greater than b")

print(bool("Hello"))
print(bool(15))

x= "Hello"
y= 15
z= 0
print(bool(x))
print(bool(y))      # Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(z))      # Any number is true except o and none

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES")
else:
  print("NO")

x=200
print(isinstance(x,str))
print(isinstance(x,int))

print(10+5)

#Python divides the operators in the following groups:

#Arithmetic operators
#Assignment operators
#Comparison operators
#Logical operators
#Identity operators
#Membership operators
#Bitwise operators

x=15
y=20
print(x+y)
print(x-y)
print(x*y)
print(x/y)

x=50
y=100
print(x%y)    #Modulus

x=5
y=6
print(x**y)   #Exponentiation
print(x//y)   #floor division

6!=7

5==5

6>=5

6<=7

x=4
x<5 and x<10    #if both statement are true

x=6
x<5 or x<10     #if any one statement is true

x=4
not(x<5 and x<10)     #reverse the result

x is y    #True if both variables are the same object

x=["apple, banana"]
y=["apple, banana"]
z=x

print(x is z)
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x==y)

x=["apple, banana"]
y=["apple, banana"]
z=x

print(x is not z)
print(x is not y)
print(x!=y)

x="apple, banana, cherry"
print("banana" in x)
print("guava" in x)

print((6+3) - (6+2))
print(100+5*3)

print(100-3**3)

print(100+~3)     #The calculation reads 100 + -4 = 96
print(100-+3)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)     #Lists allow duplicate values

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(len(thislist))

list1=["apple", "banana", "cherry"]
list2=[1,5,3,4,9]
list3=[True, False, False]

list1 = ["abc", 34, True, 40, "Male"]
print(list1)

mylist = ["Apple", "banana", "cherry"]
print(type(mylist))

thislist = list(("apple", "banana", "cherry"))
print(thislist)

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")      #remove
thisset.discard("cherry")     #discard

print(thisset)

thisset = {"apple", "banana", "cherry"}
x=thisset.pop()
print(x)
print(thisset)

thisset={"Cherry", "Cherry", "Cherry","Cherry"}
x=thisset.pop()
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)      #this will raise an error because the set no longer exists

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

set1 = {"a", "b", "c"}
set2 = {1,2,3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1,2,3}

set1.update(set2)
print(set1)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.symmetric_difference(y)
print(z)

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}

z = x.symmetric_difference(y)
print(z)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
print(thisdict)

print(thisdict["Brand"])

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Year": 2023
}
               # #Duplicate values will overwrite existing values
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}

print(len(thisdict))

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red", "White", "Blue"]
}

print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red", "White", "Blue"]
}
print(type(thisdict))

thisdict = dict(name = "Shriyanshu", age = 23, country = "India")
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red", "White", "Blue"]
}
x=thisdict["Model"]
print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red", "White", "Blue"]
}
x= thisdict.get("Model")
print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964,
    "Colors": ["Red", "White", "Blue"]
}
x=thisdict.keys()
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x= thisdict["model"]
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=thisdict.get("model")
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x=thisdict.keys()
print(x)

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()

print(x)
car["color"] = "white"
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["model"] = "BMW"

print(x) #after the change

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=car.values()
print(x)
car["color"]="White"
print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
thisdict["Color"]="Red"
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
thisdict.update({"Color":"Red"})
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
thisdict.pop("Model")
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
thisdict.popitem()        #removes the last inserted item
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
del thisdict["Model"]
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
del thisdict      #this will cause an error because "thisdict" no longer exists.
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
thisdict.clear()      #empties the dictionary
print(thisdict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for x in thisdict:        #Print all key names
  print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for x in thisdict:        #Print all values
  print(thisdict[x])

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for x in thisdict.values():
  print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for x in thisdict.keys():
  print(x)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
for x, y in thisdict.items():
  print(x,y)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
mydict=thisdict.copy()
print(mydict)

thisdict = {
    "Brand": "Ford",
    "Model": "Mustang",
    "Year": 1964
}
mydict= dict(thisdict)
print(mydict)

myfamily = {
    "child1": {
        "Name" : "Shriyanshu",
        "Year":1999
    },
    "child2" : {
        "Name":  "Divyanshu",
        "Year": 1997
    },
    "child3" : {
        "Name" : "Kittu",
        "Year" : 1999
    },
    "child4": {
        "Name": "Bittu",
        "Year": 1997
    }
}
print(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myfamily)

myfamily = {
    "child1": {
        "Name" : "Shriyanshu",
        "Year":1999
    },
    "child2" : {
        "Name":  "Divyanshu",
        "Year": 1997
    },
    "child3" : {
        "Name" : "Kittu",
        "Year" : 1999
    },
    "child4": {
        "Name": "Bittu",
        "Year": 1997
    }
}
print(myfamily["child1"]["Name"])

a=33
b=200
if b>a:
  print("b is greater than a")

a=33
b=200
if b>a:
  print("b is greater than a")

a = 33
b = 33
if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are equal")

a=200
b=33
if b>a:
  print("b is greater than a")
elif a==b:
  print("a and b are same")
else:
  print("b is smaller than a")

a=200
b=33
if b>a:
  print("b is greater than a")
else:
  print("b is smaller than a")

if a> b: print("a is greater than b")

a=2
b=330
print("A") if a>b else print("B")

a=330
b=330
print("A") if a>b else print("B") if a==b else print("C")

a=40
b=33
c=60
if a>b and c>a:
  print("both condition are true")

a=220
b=200
c=500
if b>a or c>a:
  print("one condition is true")

a=33
b=50
if not a>b:
  print("a is not greater than b")

x=40
if x>10:
  print("Above ten,")
  if x>20:
    print("and also above 20!")
else:
      print("but not above 20")

a=20
b=30
if b>a:
  pass

i=1
while i<6:
  print(i)
  i+=1        #remember to increment i, or else the loop will continue forever.

i=1
while i<6:
  print(i)
  if i==3:
    break
  i+=1

i=0
while i<6:
  i+=1
  if i==3:
    continue
  print(i)

i=1
while i<6:
  print(i)
  i+=1
else:
  print("i is no longer less than 6")

principle= float(input("Priciple amount: "))
rate= float(input("Rate of principle amount: "))
time= float(input("time period in hours: "))
SI= (principle*rate*time)/100
print(SI)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
for x in "banana":
  print(x)
  if x=="banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in "banana":
  print(x)
  if x=="banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in range(6):
  print(x)

for x in range(2,6):  # from 2 to 30 with addition of 3
  print(x)

for x in range(6):
  print(x)
else:
  print("finally finished")

for x in range(6):
  if x==3: break
  print(x)
else:
  print("finally finsihed")

adj = ["good", "best", "tasty"]
fruits=["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x,y)

for x in [0,1,2]:
  pass

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname):
  print(fname +"Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(fname, lname):
  print(fname+"+lname")

my_function("Emil", "Refsnes")

def my_function(fname, lname):
  print(fname+"+lanme") #This function expects 2 arguments, but gets only 1
my_function("Emil")

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1="nobita", child2="doraemon", child3="Shriyanshu")

def my_function(**kid):
  print("His last name is "+ kid["lname"])
my_function(fname="tobias", lname="Refsnes")

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("India")
my_function("Bharat")
my_function("Hindustan")
my_function()
my_function("Aryavart")

def my_function(food):
  for x in food:
    print(x)

fruits=["apple", "banana", "cherry"]

my_function(fruits)

def my_function(x):
  return 5* x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def my_function():
  pass

def tri_recursion(k):
  if(k>0):
    result= k + tri_recursion(k-1)
    print(result)

  else:
    result=0
    return result

  print("\n\nRecursion Example Results")

x= lambda a: a+10
print(x(5))

x= lambda a,b: a*b
print(x(5,6))

x= lambda a,b,c: a*b*c
print(x(3,2,4))

def myfunc(n):
  return lambda a : a*n
mydoubler = myfunc(3)
print(mydoubler(11))

def myfunc(n):
  return lambda a:a*n
mytripler=myfunc(4)
print(mytripler(11))

def myfunc(n):
  return lambda a :a*n
mydoubler=myfunc(2)
mytripler=myfunc(3)
print(mydoubler(11))
print(mytripler(12))

(887-765)/4

cars=["ford","volvo","geely","tata"]
print(cars)

x=cars[0]
print(x)

cars=["ford","volvo","geely","tata"]
cars[0]="toyota"
print(cars)
x= len(cars)
print(x)
for x in cars:
  print(x)

cars=["ford","volvo","geely","tata"]
cars.append("Hero")
print(cars)

cars=["ford","volvo","geely","tata"]
cars.pop(2)       #to pop out geely
print(cars)

cars=["ford","volvo","geely","tata"]
cars.remove("volvo")
print(cars)

class Myclass():
  x=5

p1=Myclass()
print(p1.x)

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1= Person("shriyanshu",23)
print(p1.name)
print(p1.age)

class Person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1= Person("shriyanshu",23)
print(p1)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=person("Shriyanshu",23)
print(p1.name)
print(p1.age)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
p1=person("Shriyanshu", 23)
print(p1)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def __str__(self):
    return f"{self.name}({self.age})"
p1=person("Shriyanshu", 23)
print(p1)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1=person("Shriyanshu", 23)
p1.myfunc()

class person:
  def __init__(mysillyobject,name,age):
    mysillyobject.name=name
    mysillyobject.age=age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1=person("Shriyanshu",23)
p1.myfunc()

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1= person("Shriyanshu", 30)
p1.myfunc()
print(p1.age)
p1.age=23
print(p1.age)
del p1.age
print(p1.age)   #age attribute deleted
del p1
print(p1)

class person:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1= person("Shriyanshu", 30)
p1.myfunc()
del p1
print(p1)

class person:
  pass

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
x=person("Shriyanshu", "Singh")
x.printname()

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
x=person("The Great","Shriyanshu")
x.printname()

x= student("The Great", "Shriyanshu")
x.printname()

class person:
  def __init__(self,fname,lname):
    self.firtname=fname
    self.lastname=lname
  def printname(self):
    print(self.firtname,self.lastname)

class student(person):
  def __init__(self,fname,lname):
    person.__init__(self,fname,lname)
x= student("Shriyanshu", "singh")
x.printname()

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(person):
  def __init__(self, fname,lname):
    super().__init__(fname,lname)
x=student("Shriyanshu","Singh")
x.printname()

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(person):
  def __init__(self,fname,lname):
    super().__init__(fname,lname)
    self.graduationyear=2021
x=student("Shriyanshu","Singh")
x.printname()
print(x.graduationyear)

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(person):
  def __init__(self, fname, lname,year):
    super().__init__(fname, lname)
    self.graduationyear=year
x=student("Shriyanshu","Singh",2021)
print(x.firstname)
print(x.lastname)
print(x.graduationyear)

class person:
  def __init__(self,fname,lname):
    self.firstname=fname
    self.lastname=lname
  def printname(self):
    print(self.firstname,self.lastname)
class student(person):
  def __init__(self, fname, lname,year):
    super().__init__(fname,lname)
    self.graduationyear=year
  def welcome(self):
    print("welcome", self.firstname, self.lastname, "to the class of ", self.graduationyear)
x =student("Gautam","Malhotra",2021)
x.welcome()

mytuple=("apple", "banana","cherry")
myit= iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr="banana"
myit=iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple=("apple","banana","cheery")

for x in mytuple:
  print(x)

mytuple=("apple", "banana","cherry")
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr= "Banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple=("apple","banana","cherry")
for x in mytuple:
  print(x)

mystr= "banana"
for x in mystr:
  print(x)

class Mynumbers:
  def __iter__(self):
    self.a= 1
    return self

  def __next__(self):
    x = self.a
    self.a +=1
    return x

myclass=Mynumbers()
myiter= iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class Mynumbers:
  def __iter__(self):
    self.a = 1
    return self

  def  __next__(self):
    if self.a <= 20:
      x= self.a
      self.a +=1
      return x
    else:
      raise stopIteration

myclass= MyNumbers()
myiter= iter(myclass)

for x in myiter:
  print(x)

f=open("demofile.txt")
f=open("demofile.txt","rt")   #same as above

f=open("demofile.text","r")
print((f.read()))

sum=0
for i in range(10):
  sum+=1
print(sum)

sum=0
for i in range(1,6):
  cube=i**3
  sum+=cube
print(sum)