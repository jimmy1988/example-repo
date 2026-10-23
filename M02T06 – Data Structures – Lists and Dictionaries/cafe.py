#Dictionary 1 with items and stock
stock = {
    "item1" : 22,
    "item2" : 12,
    "item3" : 50,
    "item4" : 100,
    "item5" : 1,
    "item6" : 34,
    "item7" : 20,
}

#Dictionary 2 with the same items and the prices
prices = {
    "item1" : 4.50,
    "item2" : 7.00,
    "item3" : 99.00,
    "item4" : 45.00,
    "item5" : 12.50,
    "item6" : 100.00,
    "item7" : 10.00,
}

#Initialize the total stock value with a 0 value
total_stock_value = 0.00

#loop through the stock dictionary and get the total stock value
for item, stock in stock.items():
    total_stock_value += (stock * prices[item]) #multiply the stock and the price together and add it to the total stock value

print(total_stock_value) #output the total