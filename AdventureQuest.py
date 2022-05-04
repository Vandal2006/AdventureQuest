# Henry Gilson
# AdventureQuest
#functions
import os
from webbrowser import Chrome
clear = lambda: os.system('cls')
clear()
import webbrowser

def validateInput(userResponse) :
    print("Reasonable Input Traveler")
    try:
        while userResponse <1 or userResponse >3:
            print(ERROR_MESSAGE)
            userResponse = int(input(QUESTION[i]))
            continue
    except ValueError:
        while userResponse <1 or userResponse >3:
            print(ERROR_MESSAGE)
            userResponse = int(input(QUESTION[i]))
            continue
# Constants

QUESTION_WIEGHT = [
    1,
    2,
    3,
    4,
    8
]
ERROR_MESSAGE = ("please enter an interger between 1 and 3")
QUESTION = [
    '''You begin your journy.
    Do you take the obvoius path forward?(1)
    The Path that seems least traveled?(2) 
    or do you stumble through the wood?(3)
    Enter your awnser here travaler:''',
    '''On your travels you have had a number of chances to make a friend, but who do you chose as your true companion?
    Odysseus?(1)
    Hercules?(2)
    or Apollo?(3)
    nter your awnser here travaler:''',
    '''You have a chance to stop and pray, at wich gods temple do you go to?
    Zeus?(1)
    Posideian?(2)
    Gaia?(3)
    Enter your awnser here travaler:''',
    '''As you aproach the den of the PYTHON you realize that the beast may have some kind of weakness, what do you bring with you?
    A bag of wind?(1)
    A strong torch perphaps it will guid you with its light?(2)
    A vile of poisen?(3)
    Enter your awnser here travaler:''',
    '''You are now in the den of the mighty PYTHON! what do you plan to do?
    charge it head on?(1)
    change your mind about the whole thing, maybe its not so bad stuck in this code...(2)
    wait in ambush, perhaps one day it will leave its den.(3)
    Enter your awnser here travaler:'''
]
DESIRED_RESPONSE = [
    1,
    3,
    3,
    2,
    1 
]
MAX_SCORE = 3 * len(QUESTION)
COMPATIBILITY_RANGE = [
    'You have slayed the mighty PYTHON! Here is your reward!',
    'Your soul is now traped in this realm forever. Here is your punishment',
]
INTRODUCTION = '''
                                    Adventure Quest

                        ***Brought to you by GilsoSoft***


*******************************************************************************************************

Welcome brave soul. You have been summoned to this world to slay the dragon known as PYTHON sent to this
realm of existence by the Goddess Gaia. There are only two ways out of this realm for your poor trapped 
soul. To successfully vanquish the Dragon PYTHON by  passing through the trial and tribulations on the 
path to the creature, or to die in the attempt. Since your soul does not properly belong to this world 
you will have to pass through it by selecting the decisions open to you by entering in a number 
1, 2, or 3 from your “keyboard”. I wish you luck on your quest travaler.

********************************************************************************************************

'''
print(INTRODUCTION)
# main loop
response = []
comaptablity = []
for i in range(len(QUESTION)):
    try:
        userResponse = int(input(QUESTION[i]))
        validateInput(userResponse)
        response.append(userResponse)
        questionCompatability = 5 - abs(userResponse - DESIRED_RESPONSE[i])
        questionCompatability = questionCompatability * QUESTION_WIEGHT[i]
        comaptablity.append(questionCompatability)
    except ValueError:
        print(ERROR_MESSAGE)
        userResponse = int(input(QUESTION[i]))
        validateInput(userResponse)
#Python slaying success chance
totalCompatibility = 0
for c in comaptablity:
    totalCompatibility += c
if totalCompatibility>85:
    print(COMPATIBILITY_RANGE[0])
    webbrowser.open('https://proud-grass-02d65ec10.1.azurestaticapps.net/')
if totalCompatibility<84:
    print(COMPATIBILITY_RANGE[1])
    webbrowser.open('https://red-cliff-0186fc610.1.azurestaticapps.net/')
