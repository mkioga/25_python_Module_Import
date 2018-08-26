
# ================
# turtle_demo.py
# ================

# MODULES AND FUNCTIONS

# MODULES AND IMPORT

# So far we have been writing programs that have everything they need in a single python program
# Exceptions so far are the import shelve and import random (for the guessing game)

# Python documentation refers to a file containing a python program like we have been doing as a "script"
# However it is possible to create a python code that is not intended to be executed directly.
# Instead the code provides functions, classes and variable definitions etc that are designed to be used by other programs

# Python allows us to use "modules" to be used for importing
# In order to use a "module", we have to import it to our program using the "import" command


# We are going to work with python's "turtle" module to see how it works

# ==========================
# "turtle" module
# ==========================

# The turtle module is based on an educational program from 1960's called logo.
# It allowed children to control an onscreen tutle that had a pen behind it and drew a line as it moved.

# we are going to do a simple example to move the turtle on the screen

# # first import turtle module
#
# import turtle
#
# # Then create commands to move forward, back, right, left etc
# # Note that it draws a line and then the screen goes away fast.
#
# turtle.forward(100)  # moves turtle forward distance of 100 units
# turtle.right(90)     # turns turtle right at 90 degrees
# turtle.forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# turtle.left(90)      # then turn left at 90 degrees
# turtle.forward(100)  # in new direction, move forward distance of 100 units
# turtle.back(300)     # moves turtle back distance of 300 units in opposite direction
#

# ===========================================================================
# There is a way to make the screen not go away fast after the program ends
# ===========================================================================

# We import a new module called "time
# then make the program sleep for a specified time after it stops running, to give you chance to see screen better

# import turtle
# import time
#
# turtle.forward(100)  # moves turtle forward distance of 100 units
# turtle.right(90)     # turns turtle right at 90 degrees
# turtle.forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# turtle.left(90)      # then turn left at 90 degrees
# turtle.forward(100)  # in new direction, move forward distance of 100 units
# turtle.back(300)     # moves turtle back distance of 300 units in opposite direction
#
# # Here we make it sleep for 5 seconds after program finishes executing
#
# time.sleep(5)



# # =================================================================
# # How to supress warnings in intellij
# # =================================================================
#
# # There is a but in intellij that makes it say "cannot find reference for "forward" etc in turtle.py
# # There is no problem with the code, only sometimes intellij struggles importing some modules
# # One way to ignore these warnings is to use "noinspection PyUnresolvedReferences"
#
# import turtle
# import time
#
# # Note that this clears the error for turtle.forward
# # you have to make this statement for every line you want to ignore. And that can get cumbersome
#
# # noinspection PyUnresolvedReferences
# turtle.forward(100)  # moves turtle forward distance of 100 units
# turtle.right(90)     # turns turtle right at 90 degrees
# turtle.forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# turtle.left(90)      # then turn left at 90 degrees
# turtle.forward(100)  # in new direction, move forward distance of 100 units
# turtle.back(300)     # moves turtle back distance of 300 units in opposite direction
#
# # Here we make it sleep for 5 seconds after program finishes executing
#
# time.sleep(5)
#


# How to ignore all warnings

# A good way to ignore all warnings is to click on a highlighted place showing warning, say right above
# it will bring up a lightbulb
# Click on that bulb and choose "Mark all unresolved attributes of "turtle" as Ignored"
# This will make all the warnings disappear


# How to bring back the warnings

# To bring back the warnings, click on "Analyze" > "Configure current file analysis" > "Configure inspections"
# Scroll down to "python" which will be showing in blue if a change has been made
# > find "Unresolved References" (also in blue) > click on it, then to the right, find "turtle" and click "-" sign
# This will make the warnings come back

# if you want to add some more ignore references, click "+" to add


#
#
# # =================================================================
# # How to view screen output indefinitely until you close
# # =================================================================
#
# # if you don't want output screen timed, you can use turtle's "done" method
# # you don't need to import time
#
# import turtle
#
# turtle.forward(100)  # moves turtle forward distance of 100 units
# turtle.right(90)     # turns turtle right at 90 degrees
# turtle.forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# turtle.left(90)      # then turn left at 90 degrees
# turtle.forward(100)  # in new direction, move forward distance of 100 units
# turtle.back(300)     # moves turtle back distance of 300 units in opposite direction
#
# # we use "done" method to keep screen up until we close it.
#
# turtle.done()
#



#
# # =================================================================
# # Import by specifying only the submodule you want from a module
# # =================================================================
#
# # In above examples, we imported the whole module e.g. turtle module and time module
# # And then had access to all their submmodules, by prefixing them with the module e.g. turtle.forward
# # turtle.back and time.sleep() etc
#
# # We can import only the objects that we need in a module
#
#
# # here we only import the submodules we want from turtle. in this case forward, right, left, back, done & circle
# # These are the only submodules imported and that is only what we can use
# # NOTE: This gives warning about unresolved reference but it still works
#
# from turtle import forward, right, left, back, done, circle
#
# # Then we use the objects and don't need to specify turtle.forward etc because we already imported them from turtle
#
# forward(100)  # moves turtle forward distance of 100 units
# right(90)     # turns turtle right at 90 degrees
# circle(100)   # do a circle with radius 100 units
# forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# left(90)      # then turn left at 90 degrees
# forward(100)  # in new direction, move forward distance of 100 units
# back(300)     # moves turtle back distance of 300 units in opposite direction
#
# # we use "done" method to keep screen up until we close it.
#
# done()



# =================================================================
# Import every submodule in a module
# =================================================================

# to import everything from a module, we say import *
# This is not recommended because you don't know what is being imported and can use it as a variable

# in this case, we are importing everything from turtle
# NOTE: This gives warning of unresolved reference but it still works.

from turtle import *

# Then we use the objects and don't need to specify turtle.forward etc because we already imported them from turtle

forward(100)  # moves turtle forward distance of 100 units
right(90)     # turns turtle right at 90 degrees
circle(100)   # do a circle with radius 100 units
forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
left(90)      # then turn left at 90 degrees
forward(100)  # in new direction, move forward distance of 100 units
back(300)     # moves turtle back distance of 300 units in opposite direction

# we use "done" method to keep screen up until we close it.

done()





# Example why import * is not recommended


# we have a variable named "done"
#
# done = "Well done. you have finished your drawing"
#
# # we import all (which includes submmodule done)
#
# from turtle import *
#
# forward(100)  # moves turtle forward distance of 100 units
# right(90)     # turns turtle right at 90 degrees
# circle(100)   # do a circle with radius 100 units
# forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# left(90)      # then turn left at 90 degrees
# forward(100)  # in new direction, move forward distance of 100 units
# back(300)     # moves turtle back distance of 300 units in opposite direction
# done()        # we use "done" method to keep screen up until we close it.
#
# print(done)   # Now we print above message

# in this case, drawing will succeed and when it finishes and you close screen, you get warning
# <function mainloop at 0x054D0978>
# This does not print the "done" message, but says the message printed is a submodule of turtle






#
# # if you have string "done" coming after the import, the drawing will work, but then after it finishes
# # you get an error saying "str object is not callable"
# # This is because python cannot call the string "done" because there is a submodule named "done" existing
#
#
# from turtle import *
#
# done = "Well done. you have finished your drawing"
#
# forward(100)  # moves turtle forward distance of 100 units
# right(90)     # turns turtle right at 90 degrees
# circle(100)   # do a circle with radius 100 units
# forward(150)  # after it turns 90 degrees, moves turtle forward a distance of 150 units in new direction
# left(90)      # then turn left at 90 degrees
# forward(100)  # in new direction, move forward distance of 100 units
# back(300)     # moves turtle back distance of 300 units in opposite direction
# done()        # we use "done" method to keep screen up until we close it.
#
# print(done)   # Now we print above message
