#TASK--1 DISCOUNT RULES

# Taking user input
try:
    order_amount = int(input("Enter order amount: "))
except ValueError:
    print("Error: Please enter a valid number.")
    exit()

if order_amount>=2000:
    discount=15
    discount_amount=order_amount*discount/100
    subtotal=order_amount-discount_amount
    tax=subtotal*5/100
    final_total=subtotal+tax

    print("Subtotal:",subtotal)
    print("tax:",tax)
    print("final total:",final_total)

elif 1500<=order_amount<2000:
    discount=10
    discount_amount=order_amount*discount/100
    subtotal=order_amount-discount_amount
    tax=subtotal*5/100
    final_total=subtotal+tax
    print("Subtotal:",subtotal)
    print("tax:",tax)
    print("final total:",final_total)

elif 1000<=order_amount<1500:
    discount=7
    discount_amount=order_amount*discount/100
    subtotal=order_amount-discount_amount
    tax=subtotal*5/100
    final_total=subtotal+tax
    print("Subtotal:",subtotal)
    print("tax:",tax)
    print("final total:",final_total)
else:
    discount=0
    discount_amount=order_amount*discount/100
    subtotal=order_amount-discount_amount
    tax=subtotal*5/100
    final_total=subtotal+tax
    print("Subtotal:",subtotal)
    print("tax:",tax)
    print("final total:",final_total)



