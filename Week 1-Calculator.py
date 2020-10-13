#program asks for two numbers
#Offer a menu to the user giving them a choice of operator
#Include +, -, /, *, **(to the power of)

def calculator():
    print("Welcome to this basic calculator")
    no1 = int(input("Type in your first number "))
    no2 = int(input("Type in your second number "))
    print("Operations: ")
    print("A - add")
    print("B - subtract")
    print("C - divide")
    print("D - multiply")
    print("E - to the power of")
    operation = input("Pick A, B, C, D or E: ")

    if (operation == "A"):
        add = str(no1 + no2)
        print(add)
    elif (operation =="B"):
        subract = str(no1 - no2)
        print(subract)
    elif (operation =="C"):
        divide  = str(no1 / no2)
        print(divide)
    elif (operation =="D"):
        multiply = str(no1 * no2)
        print(multiply)
    elif (operation =="E"):
        power = no1 ** no2
        print(power)
    else:
        print("Invalid input entered")


calculator()

