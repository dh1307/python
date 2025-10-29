# => Welcome 

print("Hii , sir/Madam \n Welcomes to DHARM's CAfe : \n Here is The Menu Sir/Madam =>")

# => Menu 
print("------MENU------")
menu  = {
    "Soup": 70,
    "Salad": 100,
    "Coffee": 80,
    "Pizza": 120,
    "Pasta": 70,
    "Burger": 50,
    "Garlic Bread ": 60,
    "Coke": 50
}
for item,price in menu.items() :
    print(f'{item:25} : {price:}RS')

order_total = 0

# => item_1
item_1 = input("\nEnter Name of Item You Want to Order :").title()

if item_1 in menu:
    order_total += menu[item_1]
    print(f"✅Your Order of {item_1} has been placed :")
    print(f"Your Total Amount is : {order_total}RS ")
else:
    print(f"❌sorry, {item_1} is Not available in Our Menu")

# => item_2
another_order = input("Do You Want Another item {Yes or No}").lower()
if another_order=="yes" :
    item_2 = input("Enter Name of Item You Want to Order:").title()
    
    if item_2 in menu:
       order_total += menu[item_2]
       print(f" Your Another Order of {item_2} has Been Placed :")
       print(f" Your Total Amount is {order_total}RS ")
    
    else:
       print(f"❌sorry, {item_2} is Not available in Our Menu")
else:
    print("Thank You")

print("Thanks For Your Order Wait For Just 2 Minutes ")    