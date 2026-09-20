
final_price = lambda price,discount : (price - (price * discount /100) )*1.18

print(final_price(1000, 10))