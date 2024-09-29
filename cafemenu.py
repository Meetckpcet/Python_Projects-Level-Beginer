menu = {
    "Pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}


print("Welcome to the Cafe")
print("Pizza: Rs-40\nPasta: Rs-50\nBurger: Rs-60\nSalad: Rs-70\nCoffee: Rs-80")


order_total = 0


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet Sorry!!")

another_order = input("Do you want to add another item? (yes/no) ")
if another_order == "yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to ypur order")
    else:
         print(f"Ordered item {item_2} is not available yet Sorry!!")  

print(f"The total amount of items to pay is {order_total}")