coffee_prices = [("Capuchino",1.5),("Expresso",1.2),("Moka",1.9)]
def more_expensive_coffee(list):
    more_price = 0
    more_expensive_coffee = ""

    for coffee,price in list:
        if price > more_price:
            more_price = price
            more_expensive_coffee = coffee

    return more_expensive_coffee,more_price

print(more_expensive_coffee(coffee_prices))