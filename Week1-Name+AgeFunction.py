#defines a function called nameAgeFuntion
def nameFunction():
    yourName = input("What's your name? ")
    print("Hello " + yourName)

#expanding to enter age, a number, day of the month and multiply
def AgeNumberDay():
    age = int(input("How old are you? "))
    number = int(input("Pick a random number"))
    day = int(input("What day of the month is it?"))
    multiplied = str(age * number * day)
    print("Your age multipled by a number you chose and the day of the month is: " + multiplied)

#calling functions
nameFunction()
AgeNumberDay()