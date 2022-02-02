# Author: CMOB 2/2/2022

def profit(prices, sales):
    total = 0
    profit = 0
    for index, value in enumerate(prices):
        total = value * sales[0] # finds the total amount of the item sold
        profit += total # adds that amount to the total of all items sold
        del sales[0]
        
    return profit


print(profit([30, 40, 25, 55, 60, 80, 65],[1, 3, 2, 5, 2, 1, 2]))
