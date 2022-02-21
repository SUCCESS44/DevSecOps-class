Python keywords are special reserved words that have specific meanings and purposes 
and can’t be used for anything but those specific purposes.
These keywords are always available—you’ll never have to import them into your code.

Examples of python keywords

1.def keyword
Python def keyword is used to define a function, it is placed before a function name 
that is provided by the user to create a user-defined function

def my_function():
  print("Hello from a function")

my_function()

2.return keyword
The return keyword in Python exits a function and tells Python to run the rest of
the main program. A return keyword can send a value back to the main program. 
While values may have been defined in a function, you can send them back to your 
main program and read them throughout your code.

def myfunction():
  return 3+3

print(myfunction())

3. class keyword
The class keyword is used to create a class. A class is like an object constructor. 
See the example below to see how we can use it to create an object.

p1 = Person()

print(p1.name)
