product_name = input("What is the name of the product? ")
product_price = float(input("What is the price? "))
product_quantity = int(input("What is the quantity "))

total_price = str(product_quantity * product_price)
print("Total Price: " + total_price)