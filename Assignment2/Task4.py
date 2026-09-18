daily = [200, 150, 0, 400, 50, -1, 300]

total_sales = 0

for sales in daily:

    if sales == -1:
        break

    if sales == 0:
        continue

    total_sales += sales

    print("Running total:", total_sales)

print("Final total sales:", total_sales)
