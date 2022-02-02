# Author: CMOB 2/2/2022

def greater_than_40(prices):
    for index, value in enumerate(prices):
        if value > 40: # if the value is greater than 40
            prices[index] = value - 10 # reduce the value by 10 and return it into the list

    return prices


print(greater_than_40([30, 40, 25, 55, 60, 80, 65]))
