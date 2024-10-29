
"""
This is a docstring. It is used to provide information that may help the user
use the software e.g. documentation, licence information etc.

@author: PLACE YOUR NAME HERE: Nusatio Edwin Wirya
"""


# Welcome to your first Spyder file!
# Follow the tutorial to learn
# more about this coding environment


# Here is a sample line of code where we DEFINE a variable:
test_variable = 2 + 2

# Run the line above and see what happens in each
# display window (try figuring out how to run that individual line) copy paste the line or select the line ans press F9

# Run the following now:
test_variable

# Sometimes Spyder will warn you about errors
# or ways to improve your script.

# E.g.:
test_variable = 2 +

# Hover over the x symbol

# Properly commenting on your code is vital!
# For instance, would you easily know what is being done below?:

MWhpyr = [0]; #this list only contains one data element
MWhpyr[0] = 2*24*365; #define the value of the variable by calculation and set the type of variable as list instead of integer

# With inefficient code like the lines above, commenting helps with 
# optimisation, particularly within research groups


"""
Challenge (complete and submit entire Spyder file)
"""

# Let's get a bit deeper with lists. Here is what you will need to show in
# in your code below (well commented!):
    
#   1) Create a Python 'list' of 10 renewable energy fuel sources (wind, solar etc)
#   2) Use that list variable to 'print' the 4th fuel type
#   3) Assign the 5th fuel type to a variable called "fifth"
#   4) 'print' the statement "The 5th fuel type in the created list is 
#      <insert fuel type> and the fuel type with the most characters is
#      <insert fuel type>".

"""
Number 4 is going to be the most challenging and will require a bit of Googling
but ... that's the point. Coding involves a LOT of research and this will be 
a good skill to have. Sites like Stack Overflow will become your best friend!
"""

Renew_source = ['wind', 'solar_csp', 'solar_pv', 'geo', 'tidal', 'bio_plant', 'bio_animal', 'hydro', 'fusion', 'fission'] # create the list
print(Renew_source[3]) #print the fourth element that correspond to index of 3
fifth = Renew_source[4] #assign the fifth element that correspond to index of 4 to the variable
longest_renew = max(Renew_source,key=len) #max is for returning value of the largest item. key is for specifying a function that will be called on each element befor making comparisons. len is used for aquiring the length of each element
print ("The 5th fuel type in the created list is " + fifth + " and the fuel type with the most characters is "+longest_renew)

