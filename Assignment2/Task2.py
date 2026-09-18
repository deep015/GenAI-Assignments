# TASK-2

# list of orders
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discounted_items = 0

for order_amount in orders:

    # apply discounts according to the order_amount
    if order_amount >= 2000:
        discount = 15
        discounted_items += 1

    elif 1500 <= order_amount < 2000:
        discount = 10
        discounted_items += 1

    elif 1000 <= order_amount < 1500:
        discount = 7
        discounted_items += 1

    else:
        discount = 0

    discount_amount = order_amount * discount / 100
    subtotal = order_amount - discount_amount

    total_revenue += subtotal

    print("-- Order Summary --")
    print("Order Amount:", order_amount)
    print("Discount %:", discount)
    print("Final Amount:", subtotal)

print("-- Total Revenue After Discount --")
print("Total Revenue:", total_revenue)
print("No. of Discounted Items:", discounted_items)