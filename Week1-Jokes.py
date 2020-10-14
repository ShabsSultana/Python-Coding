#Program asks a user for favourite number and then tells them a joke
#The program will call a joke printing function with the users favourite number

def jokefunc():
    print("Your joke is: " + joke[number])
    print("Your number is: " + str(number + 1))

joke = ["I invented a new word! Plagarism", "Why do we tell actors to “break a leg?” Because every play has a cast.", "Where are average things manufactured? The satisfactory."]
number = (int(input("Pick a number between 1 and 3:")) - 1)
jokefunc()





