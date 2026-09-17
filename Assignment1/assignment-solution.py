# TASK--1 Product Collections

# Create a list
Product_list = [
    "jeans",
    "smartphones",
    "face wash",
    "snacks",
    "painkiller",
    "shoes"
]

# Create a tuple
sample_product = ("iphone", 300, "smartphones")

# Print 2nd and last product from the list
print("Second product:", Product_list[1])
print("Last product:", Product_list[-1])

# Add two new items to product list
Product_list.append("nike shoes")
Product_list.append("watch")

print("Updated Product List:", Product_list)


# Convert sample_product to a list
sample_product_list = list(sample_product)

print("Product as list:", sample_product_list)

# Change the item price
sample_product_list[1] = 500

print("Updated product list:", sample_product_list)

# Convert list to tuple
sample_product = tuple(sample_product_list)

print("Updated product tuple:", sample_product)


# TASK--2 Categories Using Sets

# Product categories corresponding to Product_list
categories = [
    "clothes",
    "electronics",
    "cosmetics",
    "food",
    "medicines",
    "footwear"
]

# Create a set of unique categories
categories_set = set(categories)

print("Unique categories:", categories_set)


# Demonstrate duplicate categories are ignored
categories_set.add("clothes")

print("After adding duplicate clothes:", categories_set)

# Add a new category
categories_set.add("beauty")

print("After adding new category:", categories_set)


# Check whether a category exists
print("Is electronics exist:", "electronics" in categories_set)
print("Is sports exist:", "sports" in categories_set)


# Total number of unique categories
print("Total unique categories:", len(categories_set))


# TASK--3 Product Price Dictionary

#create a price-dict
price_dict={
    "jeans": 100,
    "smartphones": 150000,
    "face wash": 50,
    "snacks": 20,
    "painkiller": 100,
    "shoes": 150
}

price_dict.update({"water bottle": 30});
print("Before updating the jeans price:", price_dict)

price_dict["jeans"] = 200;
print("After updating the jeans price:", price_dict)

price_dict.pop("water bottle");
print("After removing the water bottle:", price_dict)

Average_price=sum(price_dict.values())/len(price_dict)

print("Average price of all products:",Average_price)

print("maximum price product",max(price_dict.values()))
print("maximum price product",min(price_dict.values())) 

#TASK--4 Catalog and Category Mapping

#Create list of tuple of the products

catlog=[
    ("jeans", 100,"fashion"),
    ("tablets", 50000,"electronics"),
    ("smartphones", 150000,"electronics"),
    ("face wash", 50,"cosmetics"),
    ("snacks", 20,"grocery"),
    ("painkiller", 100,"medicines"),
    ("shirts", 300,"fashion"),
    ("shoes", 150,"footwear")
]

print(catlog)

# catogery_to_products

catogery_to_products={
    "fashion":["jeans","shirts"],
    "electronics":["smartphones","tablets"],
    "cosmetics":["face wash"],
    "grocery":["snacks"],
    "medicines":["painkiller",],
    "footwear":["shoes",]
};
print(catogery_to_products["fashion"])
print(catogery_to_products["footwear"])

#Find the maximum number of products

max_products=max(len(products) for products in catogery_to_products.values())
print("Maximum number of products:",max_products)

for category, products in catogery_to_products.items():
    if len(products) == max_products:
     print("Category with maximum products:", category)