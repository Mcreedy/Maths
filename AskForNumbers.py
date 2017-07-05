#! usr/bin/env

def whatNumbers():

    from HowManyNumbers import numofnum

    repeatnumber = numofnum()
    numbersToAdd = []

    for loop in range (0,repeatnumber):
        number = int(input("Enter number: "))
        numbersToAdd.append(number)

    total = sum(numbersToAdd)
    return total
