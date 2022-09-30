# Week 5 Namespaces and Scope
# Namespace and scope refers to where a variable function or class reside in a program

# Why should you care about Scope and Namespace?
# Understanding scope and namespace ccan help prevent logic errors, logic errors are hard to find.
# Scopre Resolution and LEGB
# pint() is a function you have used in your programs how do you know that the variable names you create won't conflict with variable names used in the print() function?
# you don't have to worry about that because Python does scope resolution using LEGB rule...
#
# First Python looks to see if the variable is defined in the local scope , if so thats the one it uses. If not it checks the enclosed scope then the global scope then the built-in scope.
#
# Namespaces
# a namespace refers to where a variable/function/object is stored. Possibilities include:
# built in
# global
# local
# nested
#
# An example of the built-in namespace include True and print(). The True constant and the print() function are defined outside of your program.
# The global namespace include variables and functions defined at the program level.
# The local namespace refers to variables defined within a function.
# Nested refers to variables defined within a function that was defined within another function.
# Example: print = "Grandma"
#
# Global vs. Local Namespace
# When you create a variable at the program level it is in the global namespace and is said to have global scope.
# within a function you create, python will look for a variable name created within the function(local scope) before looking for it at the global level.
#
# You can refer to global variables within a function but if you assign a value to a variable inside the function you create a local variable. The resulkt is two different variables of
# the same name, one global and the other local. The global variables value doesn't change.
# Example:
def which_fish():
    fish = "blue"
    print(f'Printing fish from within the which_fish function: {fish}')
fish = "red"
which_fish()
print(f'Printing fish at the program level: {fish}')
input()
# global variable_name can be created but it is NEVER to be used in a function
