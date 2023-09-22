#variables
a = 1
a = a + 2
print(a)

#strings
b = "hello"
c = "world"
d = b + " " + c
print(d)

#functions
def add(a, b):
    return a + b
  
print(add(1, 2))

#lists
e = [1, 2, 3, 4, 5]
print(e[0])
print(e[1])
print(e[2])
print(e[3])
print(e[4])

#loops
for i in range(1, 100):
  if i % 2 == 0:
    print(i)

for i in e:
    print(i)

#if statements
a = 2
if a + 1 == 3:
    print(True)

#dictionaries
f = {
    "name": "John",
    "age": 30
}
print(f["name"])
print(f["age"])

#classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
g = Person("John", 30)
print(g.name)
print(g.age)

#modules
import math
print(math.sqrt(16))

#libraries
from flask import Flask #flask is a library that makes it easy to spin up a server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
  


