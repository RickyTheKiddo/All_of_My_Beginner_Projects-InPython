stock = 1000
jeans_sold = 500
target = 800

target_hit = jeans_sold == target
print ("Hit jeans sale target: ")
print (target_hit)

current_stock = stock - jeans_sold
in_stock = current_stock != 0
print ("Jeans in stock: ")
print (in_stock)