#User enters favourite starter, main, dessert and drink.
#Output: message which says: “Your favourite meal is ………with a glass of….”

def favFood():
    starter = input("What is your favourite starter? ")
    main = input("What is your favourite main? ")
    dessert = input("What is your favourite dessert? ")
    drink = input("What is your favourite drink? ")
    print("Your favourite meal is " + starter +", " + main + " and " + dessert + " with a glass of " + drink)

favFood()