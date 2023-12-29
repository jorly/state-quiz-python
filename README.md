# state-quiz-python
Quiz on U.S. capitols written in Python

This program will quiz the user by asking them to enter the capital for a particular state. The states are asked in a randomized order and the answers are not case sensitive. If the user answers correctly, that state should is not asked again.  If the user answers incorrectly, the state is added to the end of the quiz so that it will be asked again. This allows states to be asked as many times as necessary for the user to answer correctly. The program ends after all of the state capitals have been entered correctly or the user enters ‘0’. 

The program also tracks the number of correct and incorrect responses.  At the end of the quiz it reports how many questions were answered correctly and how many in total were asked.  The progam assumes that the state names are unique, but does not assume that the state capital names are unique.

get_state_data that loads state capital data from the provided file state_capitals.txt. The function returns this data as a dictionary with the state
names as keys and the state capitals as values. 


