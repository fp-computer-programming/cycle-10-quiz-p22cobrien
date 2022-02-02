# Author: CMOB 2/2/2022

def price_average(prices):
    total = 0
    for index, value in enumerate(prices): # looks through the list
        total += value # adds each value together into a total
    amount = len(prices) # finds the number of items
    average = total / amount # divides the total by the items for the average

    return average # returns the average  


print(price_average([30, 40, 25, 55, 60, 80, 65]))