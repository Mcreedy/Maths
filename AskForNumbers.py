#! usr/bin/env

from HowManyNumbers import numofnum

def whatNumbers():
    repeatnumber = numberOfNumbers()
    numbersToAdd = []

    for loop in range (0,repeatnumber):
        number = input(int("Enter Number", repeatnumber+1))
        numbersToAdd.append(number)
    return numbersToAdd
