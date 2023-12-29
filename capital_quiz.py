"""
Author: Jorly Metzger
Date: 10/30/2023
License: GPLv3

Description:
    Reads in a file for state and capital then quizes user at random on capitals of each state.  Quiz ends when all states
    have been iterated or user enters '0'.

"""Import modules."""
import random

"""Classes and Functions"""
####
# Reads in an input file to create a dictionary of states and their capital
# ##
def get_state_data():
    document = open("state_capitals.txt")
    capitals = {}

    for iter in document:
        iter = iter.rstrip()
        line = iter.split(", ")
        state = line[1]
        capital = line[0]
        capitals[state] = capital

    document.close()
    return capitals


def main():
    states = get_state_data()                                       # create state : capital dictionary

    questionCnt = 0                                                 # initialize variables
    correct = 0
    exit = False
    
    while exit == False :                                           # loop until an exit condition is reached
        key = random.choice(list(states.keys()))                    # randomly select a state
        capital = states.pop(key)                                   # remove state from dictionary, and acquire capital

        answer = input (f"What is the capital of {key} (enter 0 to quit)? ")          # quiz the user

        if (answer == "0"):
            exit = True
        else:
            questionCnt += 1
            if (answer.lower() == capital.lower()):                 # assess the user
                print ("  That is correct!")
                correct += 1
            else:
                print ("  That is incorrect.")
                print (f"  The capital of {key} is {capital}.")
                states[key] = capital

        if len(states) == 0:                                        # if capital for all states correct, then exit
            exit = True

    if (questionCnt > 0):
        print (f"You answered {(correct/questionCnt)*100:.1f}% of the questions correctly.")
    else:
        print ("You didn't answer any questions.")


"""Main - Do not change anything below this line."""
if __name__ == "__main__":
    main()
