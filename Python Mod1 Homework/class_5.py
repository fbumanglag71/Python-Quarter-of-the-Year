## Author: Francisco Bumanglag
## Project: Quarter of the Year
## Assignment: Module 1 Project 5
## Course: Python Santa Ana College
## Class: CMPR114 Jason Sim
## Date: June 18, 2023


#INPUT MONTHLY INFORMATION 
month = int(input('Enter the month as a number between 1 and 12: '))

#LOOP STATEMENT TO DETERMINE QUARTER -- THEN DISPLAY OUTPUT OR ERROR MESSAGE
if month >= 1 and month <= 3:
    print('The month is in the first quarter')

elif month >= 4 and month <= 6:
    print('The month is in the second quarter')

elif month >= 7 and month <= 9:
    print('The month is in the third quarter')

elif month >= 10 and month <= 12:
    print('The month is in the fourth quarter')

else: 
  print('Error.  Invalid entry.  Please enter a number between 1 and 12')



