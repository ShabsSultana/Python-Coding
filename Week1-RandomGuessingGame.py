#imports random function
import random

#asks for name
myName = input("Hello! What is your name? ")
#assigns a random integer from 1 to 10 to variable 'number'
number = random.randint(1,8)

#asks user to take a guess, casts it as an integer, stores as guess
guess = int(input("Take a guess: "))

#if statement, if guess and number are the same then print good job
if guess == number:
    print("Good job, " + myName + "! Your guessed the number")
#is guess and number aren't the same then better luck next time
else:
    print("Sorry, better luck next time")
    