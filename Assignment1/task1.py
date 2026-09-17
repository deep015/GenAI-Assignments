#create a list
Product_list=["cloths","electronics","cosmetics","grocessary","medicines"];

#create a tuple
sample_product=("Face wash",300,"cosmetics");

#print 2nd and last product form the list
print(Product_list[1],Product_list[-1]);

#add new item in product list
Product_list.append("shoes");
print(Product_list);

#convert sample_product to  a list
sample_product_list=list(sample_product);
print(sample_product_list); 

# change the item price
sample_product_list[1]=500;
print(sample_product_list);

#convert list to tuple
sample_product=tuple(sample_product_list);
print(sample_product);
