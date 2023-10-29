# Class
# Collection of blueprints to create objects
# Attributes means Variables

# Empty class
class Mainclass:
    pass

# Class have state, behaviour and Identity

# State means: Attibutes-variables and variables have properties- int, char, float etc
# Behaviour means: Methods of an object and response of an object to others
# Identity: Uinque name to an object to use it in other objects


# Objects
object = Mainclass()

# Self- means pointers to use the current instance or params of a class
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

# __init__() constructor that called as soon as initialization is called

class Dog:
    # class attribute
    attr1 = "mammal"

    # Instance attribute
    def __init__(self, name):
        self.name = name

    # Driver code
    # Object instantiation
Rodger = Dog("Rodger")

    # Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))

    # Accessing instance attributes
print("My name is {}".format(Rodger.name))


# instances
# creating of objects by calling the class name


# initialization
# using of __init__ to initialize the object


# Fllow

# Class name is created
# class name should always starts with Capital letter
# We can create class attributes
# __init__ is a constructor to initialize to create the instance of a class ie object.
#  Classes doesn't always need constructor. it is required if there are any methods or have parameters to use in the methods
# Self is a pointer to point the class instance in the objects.


# Python is a dynamic programming language
# Dyamic means checking the datatypes while execution.
# Static means checking before the execution ie may in compilation

# Interpreted programming language means checking the types while executing each line by line.



# Lists and Tuples
# Lists = [], tuples = ()
# Mutable-can change, edit or slice, immutables-no changes possible

# None

# A namespace in Python ensures that object names in a program are unique and can be used without any conflict.
