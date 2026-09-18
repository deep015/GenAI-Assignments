# TASK--3 ORDER MENU

orders=[]

while True:

    print("\n---MENU---")
    print("1 - Add order amount")
    print("2 - show all Orders and final amount")
    print("q - Quit")

    choice = input("Enter your choice:")

    if choice == "1":

        order_amount=int(input("Enter order amount:"))
        orders.append(order_amount)

        print("Order added successfully")

    elif choice == "2":

        for order_amount in orders:
            if order_amount >=2000:
                discount=15
            elif 1500 <=order_amount <2000:
                discount=10
            elif 1000 <=order_amount <1500:
                discount=7
            else:
                discount=0

            discount_amount=order_amount*discount/100
            subtotal=order_amount-discount_amount
            tax=subtotal*5/100
            final_total=subtotal+tax

            print("Order Amount:",order_amount)
            print("Discount:",discount,"%")
            print("Final Amount:",final_total)
    elif choice == "q":
        print("Program Ended")
    else:
        print("Invalid choice")
        continue
    

