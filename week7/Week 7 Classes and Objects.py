#Classes and Objects
#
#Class is like a blue print
#
#an obnject is an instance of a class

#Alternative Metaphor
#you might look at classes vs objects like you would a video game
#the game in the game store is a class
#you can look at its features and learn what it can do but you canlt actually do anything with it
#
#when you purchase the game you get a unique instance of it
#you customize it

#Class Components
#Class
#Methods
#Attributes
#Constructors
#Class Variables
#Destructors
#Private Instance Variables
#Hidden Variables
#Inheritance

#Defining a Class
#all class variables and methods are indented
#attributes are also referred to as instance variables and are referenced inside a method using do notation and prefixed with 'self'
#the firsty line that is not indented indicates that the class definition ended with the previous line

#like the definition of a function defining a class just provides information to python on what to do when an object of that class is created


#Basic Format of a simple class
#__INIT__ is the constructor and is called by python when an instance(onject) of the class is created
#'self' is a unique identifier for the instance created by python
#although methods always have a self parameter there is no mathcing argument when the method is called
#all instance attributes are referenced using self and dot notation and persist as long as the object exists



class MyStuff:
    def __init__(self, some_val)
        self.some_val = some_val
    def showme(self):
        print(self.some_val)

stuff_one = mystuff("first")
stuff_one.showme()

Creating attributes
Instance attributes can be created whereever they are needed using the 'self' keyword and dot notation
typically this would be done with a method with initial default values assigned to the attributes in the constructor

class with destructor and class attribute

class attributes are defined outside of methods and maintain information about the class not the individual instances
class attributes are referenced using the class name and dot notation
Destructors are defined with the name __del__, with two underscores at the beginning and end of the name
Destructors are called automatically by python when an instance is deleted and are only needed if special clenup is neded for the class or instance

Information Hiding
Other languages like Java and C++ emphasize information hiding and don't allow access to attribuets
to get or set the value of an attribute getter and setter methods must be defined within the class

while you may choose to define getter and setter methods in python class doing so is gernally discouraged

Access an objhects attributes in python
to access attributes of an instace use the instance variable name and dot notation

note that this is the python way and is not supported in other programming langages like Java or C++ which implement information hiding

In languages like those typically getter() and setter() methods would be defined for viewing or changing an attribute

Private and hidden variables
Python implements information hiding by convention
If an isntance variable attribute should not be accessed directly add a single underscore before the name
This informs the programmer that the variable should not be accessed directly but this is just a convention and not inforced by the language

if you really really feel strongly about it add two underscores bfefore the anme and at most one trailing undercore so that pythong can perform "name mangaling" This concept beyond the scope of this course and is insteded to prevent naming collisions using subclasses
see private variables

you should nknow that there is such as private and hidden variables and may choose to explore iot on your own if you are so inclined



