#create a list cafe menu
menu=["cake","croissant","coffee","chocolate"]
#create a dictionary cafe stock amounts
stock={"cake":20, "croissant":30, "coffee":150, "chocolate":35}
#create a dictionary menu prices
price={"cake":3,"croissant":2, "coffee":3.5, "chocolate":1.5}

#calculate the total stock worth in the cafe
total_stock= 0
for item in menu:
    item_value=(stock[item]* price[item])
    total_stock+=item_value
print(total_stock)