##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2023
## Author: John.Fay@duke.edu (for ENV859)
##---------------------------------------------------------------------

# Import packages
import os, sys, arcpy

# Set input variable (hard-wired)
inputFile = 'C:/Users/jb878/ENV859/ARGOSTracking/Data/ARGOSdata/1997dg.txt'
outputFC = 'C:/Users/jb878/ENV859/ARGOSTracking/Scratch/ARGOSTrack.shp'