# Author: CMOB 2/2/2022

def price_reduce(prices):
    
    for index, value in enumerate(prices):
        prices[index] = value - 5 # takes the value and reduces it by 5 before returning it to the same list

    return prices


print(price_reduce([30, 40, 25, 55, 60, 80, 65]))
