price_list=[100,250,400,1200,50,2000,850]

def add_price(price_list,price):
     price_list.append(price)

def get_avg_price(price_list):
    total=0
    for price in price_list:
        total+=price
    avg_price=total/len(price_list)
    return avg_price

def get_max_price(price_list):
    return max(price_list)

add_price(price_list,500)
print(price_list)
print(get_avg_price(price_list))
print(get_max_price(price_list))