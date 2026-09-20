prices = [100,250,400,1200,50,2000,850]


discounted_item=list(map(lambda price:price-(price*10/100),prices))

last_price=list(filter(lambda price:price>300,discounted_item))

print("Discounted prices:",discounted_item)
print("price After discount:",last_price)














