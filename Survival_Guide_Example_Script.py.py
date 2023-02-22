# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:39:07 2022
Examples and Exercises for the JACS Python Intro Session
@author: Soheb Mandhai
"""


"Importing libraries"
import numpy as np #Used for numerical calculations
import matplotlib.pyplot as plt #Useful for creating visualisations with data
import pandas as pd #Useful for processing tables and data files

# =============================================================================
# DATA Types
# =============================================================================

# =============================================================================
# NUMERICAL
# =============================================================================

"These exercises will help you learn how data types in pythons work"

"Working with Integers"
a = 100
b = 2
c = a*b
print(c)

"Working with floats"

af = 100.
bf = 3.
cf = af/bf
print(cf) 

"Working with complex numbers"
ac = 100 + 2j
bc = 2 + 1.2j
cc = ac+bc
print(cc)

# =============================================================================
# Strings
# =============================================================================
"Printing out a string"
print("Hello World")

"Assigning a string"
word = 'Manchester City '
print(word)

"Extracting character by index"
print(word[4])

"You can also modify strings in Python!"
print(word.upper()) #All upper case
print(word.lower()) #All lower case
print(word.lower().capitalize()) #Capitalize the first letter
print(word.replace('M','F')) #Replace a letter
print(word.strip()) #Remove white spaces from the front or end of a word
print(word.split('e')) #Splits the word around the letter e

# =============================================================================
# Sequences
# =============================================================================

"Defining a list"
alist = [1,2,3]
print(alist)
"Remember, indexing in Python starts from 0 for the first element"
print(alist[2])
"Replacing a value in a list"
alist[2] = 4
print(alist)

"Defining a tuple"
atuple = (4,5,6)
print(atuple)
print(atuple[0])

"Defining a dictionary"
adict = {"snack":"chocolate", "amount":3, "healthy": False}
print(adict)
print(adict['snack'])

"Defining a set"
aset = {"banana","apple","oranges"}
print(aset)

# =============================================================================
# Booleans
# =============================================================================

"Assigning Booleans"
abool = False
print(abool)
"Checking if the condition holds"
if abool == False:
    print("I'm not abool, you are!")
a = 1
b = 3
if a<b:
    print("a is lower than b")
    
# =============================================================================
# End of Chapter Exercises
# =============================================================================
fruits = {'banana':3,'strawberries':4,'pineapple':1,'lemon':2}
type(4*(2+6j))
print(fruits['banana'])
#print(fruits[3]) #This will return a KeyError
food =  ("toast","cereal","croissant")
# food[1] = "banana" #Will return a TypeError

# =============================================================================
# Conditions and Loops
# =============================================================================

# =============================================================================
# If, Elif, and Else statements
# =============================================================================

JACS = True #Set a boolean variable

"Boolean example of using conditions"
if JACS: #If JACS == True
    #do something
    print("Python JACS Session 2022...\n")
else:
    print("Something else...\n")

"Numerical example of using conditions"
people = 9
if people > 10:
    print("There are over 10 people...\n")
elif (people <= 10) & (people>0):
    print("There are less than or equal to 10 people...\n")
else:
    print("No one is here...\n")

# =============================================================================
# For Loops
# =============================================================================
"""For loops iterate over the block of code indented following the colon. 
The iteration number is determined by the limiting condition.
"""

#Iterate over values 0-9 and run the code, setting i to the number
for i in range(10):
    #do something
    print(i)

# =============================================================================
# While
# =============================================================================

cut_off = 10 #Value to terminate at
count = 0 #Initialise a counter 
#While conditions requires termination conditions
print('While loop')
while (count < 10):
    print(count)
    count+=1
    
# =============================================================================
# End of Chapter Exercise: Looping
# =============================================================================
#%%
#Q1

magic_beans = 3
if magic_beans > 3:
    print("Jack got a good bargain for the cow... maybe")
elif (magic_beans==3):
    print("Woah... three magic beans???")
else:
    print("""
          Jack's Mom: WHERE'S THE COW?
          Jack: I sold it for beans and then ate some
          because I got hungry.""")

#Q2
cutoff = 10
i = 0
while i < cutoff:
    print(i)
    i+=1

# =============================================================================
# Advanced Operations
# =============================================================================
# =============================================================================
# Functions
# =============================================================================

"A function is a block of code that can be reused without retyping lines"

#Basic designation for a function
def my_function(arg="I'm an argument"):
    #You can use assignements to initialise default arguments
    #Coding block here
    print(arg)

"Once a function has been defined like the above, we can call it with"
my_function() #without an argument, uses default value of arg
my_function("I like chocolate")

"Simple Pythagoras' Theorem"
def pythag(a=1,b=1):
    return (a**2+b**2)**(1./2)

c = pythag(3,4)
print(c) # Works

# =============================================================================
# Lambda 
# =============================================================================
"Mini functions that carry out a single operation"
lambda_func = lambda x : x+10
print(lambda_func(5))

# =============================================================================
# Classes
# =============================================================================
"Classes makes use of Object-Oriented programming aspect of Python"
"These are blueprints for creating objects"
"Example"
class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

cat = Animal("Floofington","Feline")
dog = Animal ("Doglas", "Canine")
print(cat.name, cat.species)
print(dog.name,dog.species)

# =============================================================================
# Generators
# =============================================================================
#%%
"Generators can create controlled iterables"
"This generator will keep increasing n by one when it is iterated over"
def my_gen():
    n = 0 #Initialise counter
    while n > -1:
        if n%2 == 0:
            print(n, " is even")
        else:
            print(n, " is odd")
        n+=1
        if n == 10:
            raise StopIteration
        yield n
        

#Assign generator to a variable
agen = my_gen() 
next(agen)

"Uncomment to see how StopIteration Works"
# for item in agen:
#     print(item)

# =============================================================================
# Decorators
# =============================================================================
"Decorators are a neat approach to handle nested functions"
def my_decorator(func):
    "Define a wrapper to conduct operations on the passed function"
    def wrapper():
        f =  func() #Call function
        f_upper = f.upper() #Capitalises all letters in text
        return f_upper #returns result to outer scope
    return wrapper #returns wrapper results to global scope

"Our test function simply returns text"
def test_func(text='Hello There'):
    return text

print(test_func()) #Original Text
present = my_decorator(test_func) #Decorated Function
print(present()) #Print

"Alternatively... we can apply the decorator using the following convention."
"This is the equivalent to the assignments from above"
@my_decorator
def test_func_2(text='General Kenobi!'):
    return text

print(test_func_2())

# =============================================================================
# End of Chapter Exercises
# =============================================================================
#Q2
smol_func = lambda x,y: x**2 + y**2
print(smol_func(3,2))

# =============================================================================
# Scope
# =============================================================================
#%%
"Global variables are available to all functions"
x= 1
def scope():
    print(x)
scope()
print(x)

"You can define the var. within a local scope with no effect on the global scope"

x= 1
def scope():
    x=2
    print(x)
scope()
print(x)

"Finally, you can overwrite the global var. by invoking the global keyword"

x= 1
def scope():
    global x
    x = 2
    print(x)
scope()
print(x)

# =============================================================================
# Docstring Template
# =============================================================================
def foo(a, b, c=False): #Credit: Josh Hayes
  """
  a short one-line description of the function  

  Parameters
  ----------
  a : float
    description of a
  b : str
    description of b
  c : bool, optional
    description of c. Default is False

  Returns
  -------
  out : dtype of out
    dexcription

  Notes
  -----
  Anything else you'd like to say about odd behavious

  """

  # do stuff

  return
#Use ?foo to find out more about this function
# =============================================================================
# Excessive for loops
# =============================================================================
"Excessive looping can be avoided in most cases"
for i in range(10):
    for j in range(4):
        for k in range(3):
            print(i*j*k)