# motorbike costs £2000
# loses 10% of its value every year
# Print the bike’s value every year until it falls below £1000

motorbike = 2000

while (motorbike >= 1000):
    print("Value of motorbike is £" + str(motorbike))
    motorbike = (motorbike * (9/10))
else:
    print("Value of motorbike is below £1000")