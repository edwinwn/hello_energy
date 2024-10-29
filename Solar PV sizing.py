# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 12:22:27 2024

@author: Nusatio Edwin W
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Copyright 2024 University of Oxford. All Rights Reserved.
The authors, being Dr Scot Wheeler, have asserted their moral rights.

This is the module docstring. It can be used to introduce the purpose and
key functionality of the module. It will appear in documentation/help.
As an example, in the spyder help window (top right subwindow be default), 
type scipy.optimize to see an example of the docstring for the 
optimize module of the scipy library.

The very first line of the script is an optional shebang line. It tells the 
operating system which interpreter to use to execute the code if the script 
was treated as a stadalone executable.
"""

# import required libraries
import math
import numpy as np
import pandas as pd


def calc_pv_array_size():
    """
    This is a docstring. Use it to explain to the user what a function does.
    It will automatically be read by 'help' functions such as in spyder.
    
    Function to calculate the size of a PV array that can fit on a building
    with shed style roof.

    Parameters
    ----------
    building_width : float
        Width of building in metres.
    building_length : float
        Length of building in metres.
    roof_angle : float
        Angle of the roof from horizontal in degrees.
    pv_width : float
        Width of single PV panel in mm.
    pv_height : float
        Height of single PV panel in mm.
    pv_power : float
        Power of single PV panel in W.

    Returns
    -------
    total_panels : float
        Maximum number of PV panels that fit on the roof.
    total_power : float
        Total power of PV array in kW.

    """

    # add your code to calculate PV array size below. You may wish to use
    # the comments below to structure your code.

    #input parameters
    building_width = float(input("Width of building in metres: "))
    building_length = float(input("Length of building in metres: "))
    roof_angle = float(input("Angle of the roof from horizontal in degrees: "))
    pv_width = float(input("Width of single PV panel in mm: "))
    pv_height = float(input("Height of single PV panel in mm: "))
    pv_power = float(input("Power of single PV panel in W: "))

    #output parameters
    total_panels = float()
    total_power= float()


    #convert pv size to meter
    pv_width_m = pv_width/1000
    pv_height_m = pv_height/1000
    
    #convert angle from deg to rad
    roof_angle_rad = math.radians(roof_angle)
        
    # calculate rooftop dimensions accounting for angle
    roof_length = building_length #assuming roof length is running along E-W direction.
    roof_width = (building_width/2)/math.cos(roof_angle_rad) #assuming roof width is running along N-S direction. 
    #in UK, solar only work if faces south
        
    # calculate maximum panels in each dimension (better than using total area) and two different orientations
    panels_l = math.floor(roof_length/pv_height_m)
    panels_w = math.floor(roof_width/pv_width_m)
    # // is the python floor division operator. Could also use math.floor(roof_length // pv_width)

    # calculate the number of panels by multiplying x and y number of panels
    total_panels = panels_l * panels_w
    
    # calculate the total power of the system
    total_power = (total_panels * pv_power)/1000
    
    return total_panels, total_power

# Capture the returned values in variables
total_panels, total_power = calc_pv_array_size()

# Print the result
print("Total Panels:", total_panels)
print("Total Power (kW):", total_power)


