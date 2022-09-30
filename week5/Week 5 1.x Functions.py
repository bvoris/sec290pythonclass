# Week 5 Functions
# Functions provide a means to re-use code DRY Don't Repeat yourself
# Functions also provide a means to organize your work
# modules provide access to specialized software you can use in your programs

# Built in funcitons input() len()
# input() get input from the keyboard
# len() report the length of a string or data structure
# Functions take input and does something with it, produces output
# creating user defined functions
# pick a name for the function that says what it does, and does not confliuct with another variable or function
# start with the def keyword followed by the name, parentheses and ending in a colon
# an optional list of parameters spearated by commas may be included inside the parentheses
# The lines of code indented under the function belong ot the function
# the end of the function can be indicated with a return statement or by an unindented line of code.

def greetings():
    print ("Hello world")
greetings()
input()

def greetings(name):
    print("Sec 290 welcomes {}!".format(name))
your_name = input("Please enter your name: ")
greetings(your_name)
input()

# function with output
def get_letter_grade(number_grade):
    if number_grade >= 90:
        letter_grade = "A"
    elif number_grade >= 80:
        letter_grade = "B"
    elif number_grade >= 70:
        letter_grade = "C"
    elif number_grade >= 65:
        letter_grade = "D"
    else:
        letter_grade = "F"
    return letter_grade
num_grade = int(input("Please enter your grade: "))
let_grade = get_letter_grade(num_grade)
print("Your grade for {} is {}.".format(num_grade,let_grade))
input()

# Postional Arguments
# order matters, each function call must supply arguments for each parameter in the function definition
def greetings (first_name, last_name):
    message = f'Welcome, {first_name} {last_name}'
    return message
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
msg = greetings(first, last)
print(msg)
input()
# Keyword arguments
# if the calling program knows the names of the parameters in the function definition the parameter names can be used as keywords
# values can be assigned to the keywords in the function call
# order of the arguments doesn't matter
# parameter and argument names must exactly match
#
# for most simple programs, there is no need to know the parameter names and no need to use keyword arguments
def greeting(first_name, last_name):
    message = f'welcome, {first_name} {last_name}!'
    return message
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
msg = greeting(last_name=last, first_name = first)
print(msg)

# default values
# functions can be created assuming default values for one or more parameters
# if the default values for these parameters is good enough, matching argum,ents do not have to be provided in the function call.
# the print() function is an example in which the default is to provide a space between the argument values in the output and to append a line break.
# The defaults can be overridden by providing keyword arguments.
# when using default keyword aguments, all positional arguments must come firsst in the function call.
print ("Hello", "Delicious Sandwhich!")
print("to the world of my stomach!")
print("===========================")
input()
# sep and end are keyword pareemeters for print
# set the separator to "*" and replace the ending
# line break with a colon.
print ("Hello", "Delicious Sandwhich!", sep="*", end=":")
print("to the world of my stomach!")
input()

# Defining Funcitons without parameters
# To define a default value for a parameter, assign a value to it in the function definition
# when a default parameter value is assigned it must follow all positional parameters
# If the default value is accaptable the argument can be omitted in the function call
# default parameters are a means of making parameters options
def greeting(name, where_abouts = "the world of Python"):
    msg = "f'Welcome, {name}, to {where_abouts!}'"
    return msg

your_name = input("Please enter your name: ")

message = greeting(your_name)
print(message)
message = greeting(your_name, where_abouts= "Wilmington University")
print(message)
input()