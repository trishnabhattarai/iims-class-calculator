import pandas as pd


product = {
    "Apple": {"price": 100, "stock": 20},
    "Banana": {"price": 50, "stock": 30},
    "Mango": {"price": 150, "stock": 15},
    "Orange": {"price": 80, "stock": 25},
}


card = []
quantities = []
total_amount = 0

print("Welcome to Virtual Supermarket!")
order_product = input("Enter the product you want to order: ")


if order_product in product:
    quantity = int(input(f"Enter the quantity of {order_product}: "))
    
    
    if quantity <= product[order_product]["stock"]:
       
        card.append(order_product)
        quantities.append(quantity)
        product[order_product]["stock"] -= quantity
        print("Product has been automatically added to the cart.")
    elif quantity > product[order_product]["stock"]:
        print(f"Sorry, we don't have enough stock for {order_product} product.")
else:
    print("Invalid product name. Please try again.")


user_receipt = input("Do you want to view the receipt? (yes/no): ")

if user_receipt.lower() == "yes":
    print("\nYour Receipt is as follows:")

    
    print(f"{'Product Name':<15} {'Quantity':<10} {'Price per unit':<15} {'Total Price'}")
    
   
    for i in range(len(card)):
        product_name = card[i]
        quantity = quantities[i]
        price_per_unit = product[product_name]["price"]
        total_price = quantity * price_per_unit
        total_amount += total_price
        
      
        print(f"{product_name:<15} {quantity:<10} {price_per_unit:<15} {total_price}")
    
    
    print(f"\n{'Total Amount':<40} {total_amount}")
