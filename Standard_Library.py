

# ====================
# Standard_library.py
# ====================

# =================================================================
# PYTHON STANDARD LIBRARY
# =================================================================

# The standard library ships with python and provides modules that we can use
# it includes everything built in python that we can use without importing anything

# using "dir" method

# "dir" method can be used to show all the built in functions in python

print(dir())

print("="*40)


# This gives below output which includes all the built in functions in python
# We see they start with two underscores (__). So anything starting with __ should not be changed
# Because there are no private variables in python and everything is available everywhere
# so if you change them for one program, it can affect other programs
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# Note that if you create a variable starting with __, it indicates private variabl (not enforced by python)
# so its up to you to respect that in your coding.

# Most of the above built ins are used for internal running of python
# we are mostly interested with the __builtins__ functions
# for a list of built in functions, go to this link
# https://docs.python.org/2/library/functions.html

# you can also look at what is in the __builtins__ function from python using command below

print(dir(__builtins__))

print("="*40)
# you can also use a for loop to give a better list

for m in dir(__builtins__):
    print(m)

print("="*40)



# =======================================================
# Now we can import shelve and see what modules it has
# =======================================================

import shelve

print("All builtin functions and shelve:")
print(dir())  # you will see shelve included in the functions because it was imported
print()
print("All the methods inside shelve:")
print(dir(shelve))  # prints the methods in shelve.
# Notice we have the open method here. we have used it with shelve but no "close"
# This is because "close" is a method of the shelf class
print()
print("="*40)

# Now we are going to list the methods provided by shelve.Shelf (NOTE: Shelf starts with Capital S )
print("All the methods inside shelve.Shelf:")
print(dir(shelve.Shelf))
print()
print("="*40)
# We will use a for loop to see what is in the shelve.Shelf

print("Methods in shelf.Shelf using for loop")
for m in dir(shelve.Shelf):
    print(m)

print()
print("="*40)

# We can also decide to ignore the methods starting with two underscores __

print("Methods in shelve.Shelf excluding those starting with _")
for n in dir(shelve.Shelf):
    if n[0] != '_':  # Test if n starts with _. Note n[0] means the first character in n
        print(n)

print("="*40)
# you can also check the methods available by doing "shelve.Shelf. (and it will show you the options)

# Another way to see the details of the module (e.g. shelve), click CTRL and then click shelf (where you imported it)
# It will take you to a new window with the details of the module.
# Shelve module is written in python, Some other modules are written in C




# ===========================
# Using the "help" module
# ===========================

# The "help" module gives you information about the module you pass to it.
# In this case, it gives you more information about shelve module

import shelve

help(shelve)

print("="*40)

# you can also search for shelve in python website for documentation


# you can also get help for specific submodules in a module

import random

print(dir(random))  # Gives you info about random module
print()
print(dir(random.BPF))  # Gives you info about submodule BPF
print()
help(dir(random.BPF))   # Gives you help about submodule BPF


