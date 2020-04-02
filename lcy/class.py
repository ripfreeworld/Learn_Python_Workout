class Foo():
    def __init__(self, x):
        self.x = x

f = Foo(10)
print(f.x)

# __init__ is not only a "constructor"
# When we call Foo(10), Python first looks for the Foo identifier
# in the same way as it looks for every other variable in the 
# language, following the LEGB rule. It finds Foo as a globally 
# defined variable, referencing a class. Classes are "callable",
# meaning that they can be invoked with parentheses.

class Person:
    def __init__(self, name):
        self.name = name

p = Person('myname')

# What happens inside of Python? First, the __new__ method, 
# which we never define, runs behind the scenes, creating the 
# object. It creates a new instance of Person, and holds onto 
# it as a local variable. Then __new__ calls __init__. It passes
# the newly created object as the first argument to __init__, 
# and then passes all additional arguments using *args and **kwargs
# Now __init__ adds one or more attributes to the new object, 
# which it knows as self, a local variable
# Finally, __new__ returns the newly created object to its caller, 
# with the attribute that was added.
# the point of __init__ is to modify the new instance by adding 
# attributes, not for its return value. Once __init__ is done, 
# it exits, leaving __new__ with an updated and modified object. 
# __new__ then returns this new object to its caller