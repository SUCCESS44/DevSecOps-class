The Python built-in functions are defined as the functions whose functionality is pre-defined in Python.
The python interpreter has several functions that are always present for use.
These functions are known as Built-in Functions.

Examples
 
print() function
The print() function prints the given object to the standard output device (screen) or to the text stream file.

Example
message = 'Python is fun'

# print the string message
print(message)

# Output: Python is fun

type() function
type() method returns class type of the argument(object) passed as parameter. 
type() function is mostly used for debugging purposes.
Two different types of arguments can be passed to type() function, single and three argument.
If single argument type(obj) is passed, it returns the type of given object. 
If three arguments type(name, bases, dict) is passed, it returns a new type object.

Syntax :

type(object)
type(name, bases, dict)

dir() function
dir() function in Python. dir() is a powerful inbuilt function in Python3,
which returns list of the attributes and methods 
of any object (say functions , modules, strings, lists, dictionaries etc.)
Returns : dir() tries to return a valid list of attributes of the object it is called upon.


Example
dir(object)
