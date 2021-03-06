# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17_vanQLyxBbG2XEoYpJZXk9ZoeITW7fe
"""

# CS 110A programming exercise to review for midterm test:
# A program to practice functions, if statements, loops, etc.
# Written by ____Nancy Chen______

import random

def main():
    print("Please enter one of the following options:")
    print("1 to check if a state is on the West Coast")
    print("2 to output a rectangle with random length and height, both between 2-10")
    print("3 to input a number and check if it is divisible by both 2 and 3,")
    print("  or if it's odd, or even, but not divisible by 3")
    print("4 to practice calculations and loops: ")
    choice = int(input())    
    if choice == 1:
        state = input("Enter 2-letter state code: ").upper()
        if checkWestCoast(state):

    # WRITE YOUR CODE HERE
          print("That state is on the West Coast")
    
    if choice == 2:
        randomRect()

    if choice == 3:
        numInput = int(input("Enter an integer: "))
        divisibleNum(numInput)

    if choice == 4:
        weddingGuests = int(input("Please enter a number of people coming to your wedding: "))
        busPassengers = int(input("How many people fit on a bus? "))
        calculationsLoops(weddingGuests, busPassengers)

    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
      print("Invalid input")

def checkWestCoast(stateCode):
    '''
    Returns a Boolean value: 
    True if the 2-letter state code is for a west-coast US state.
    '''
    # WRITE YOUR CODE HERE

    if stateCode == "CA" or stateCode == "OR" or stateCode == "WA": 
        print("That state is on the West Coast")
    else:
        print("That is not on the West Coast of the US")

def randomRect():
    '''
    Outputs a rectangle with random length and height, both between 2-10
    '''
    # WRITE YOUR CODE HERE
    length = random.randrange(2,11)
    height = random.randrange(2,11)

    for i in range(length):
      print("*" * length)

def divisibleNum(numTest):
    """
    Checks if number is divisible by both 2 and 3,
    or if it's odd, or even, but not divisible by 3
    """

    if numTest % 3 != 0 and numTest % 2 != 0: #if number is NOT divisible by three but is odd
      print("This number is odd")
    elif numTest % 2 == 0 and numTest % 3 == 0: #number divisible by 2 and 3
      print("This number is divisible by both 2 and 3") 
    elif numTest % 2 == 0 and numTest % 3 != 0: #number even but not divisible by 3
      print("This number is even, but not divisible by 3")

def calculationsLoops(testGuests, testPassengers):
    """
    Outputs calculations for bus seats 
    And integers and loops
    """

    busesAvail = int(testGuests/testPassengers)
    intDiv = print("Integer division: they will completely fill " + str(busesAvail) + " buses")

    busesDec = float(testGuests/testPassengers)
    decDiv = print("Decimal division: mathemtically, they will use " + str(busesDec) + " buses")
  
    modDiv = int(testGuests%testPassengers)
    modAns = print(str(modDiv) + " people will be on the bus that isn't full.")

    for i in range(5): #how to make for loop count numbers multiple times
      print("Repeating 5 times, Counting from " + str(i) + " using range:")
      count = i - 1
      for i in range(5): 
        count += 1
        print(count)


main()