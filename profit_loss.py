cost_price = float(input("Enter the cost price of the product here "))
selling_price = float(input("Enter the selling price of the product here "))
if cost_price > selling_price :
    amount = cost_price - selling_price
    print(f"The total loss is {amount}")
else:
    amount = selling_price - cost_price
    print(f"The total profit is {amount}")
