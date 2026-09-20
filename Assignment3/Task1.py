
def apply_discount(price,discount=5):
    if discount>60:
      print("Discount cannot be more than 60%")
      return
    discount_amount=price*discount/100
    final_price=price-discount_amount
    return final_price

print(apply_discount(500))
print(apply_discount(1000,10))
print(apply_discount(2000,68))  