
menu = int(input("Would you like to\n1. View products\n2.Add product\n3.Delete products\n4. Restock Items\n"))

orders = {"Order1": ["Alice", "Laptop", "£899.99"],
          "Order2": ["Bob", "Smartphone", "£499.99"],
          "Order3": ["Charlie", "Headphones", "£79.99"],
          "Order4": ["David", "Laptop", "£899.99"],
          "Order5": ["Emma", "Smartwatch","£199.99"]}

if menu == 1:
    print(orders)
    with open("text.txt", "w") as text_file:
        text_file.write(str(orders))
if menu == 2:
    num = int(input("how many orders would you like to add ?"))
    counter = 1

    while counter<=num:
        name = input("Please enter your name")
        product = input("Please enter your product")
        price=int(input("Please enter the price"))
        orders["order",counter] = name,product,price
        print("Updated dictionary: ",orders)
        counter = counter + 1
    print("Thank you for using the produt inputter")
if menu == 3:
    delete = int(input("Would you like to delete \n1.The dictionary\n2.The name\n3.Product\n4.Price\n"))

    if delete == 1:
        del orders
    if delete == 2:
        del name
    if delete == 3:
        del product
    if delete == 4:
        del price

if menu == 4:
    orderID=input("Please enter a correct order ID")
    if orderID == orders:
        print (orders)
    decision = int(input("Are you sure you want to restock this item"))
    if decision == "no" or "No":
        d2=int(input("Thank you for using the restocker would you like to try again or return to main menu(1, 2)"))
        if d2 == 1:
            decision = int(input("Are you sure you want to restock this item"))
        else:
            print("Thank you for using the restocker returning you to the main menu")    
    if decision == "yes" or "Yes":
        add = int(input("How much of the product would you like to add"))
        product = product + add

else:
   menu = int(input("Would you like to\n1. View products\n2.Add product\n3.Delete products\n4. Restock Items"))
