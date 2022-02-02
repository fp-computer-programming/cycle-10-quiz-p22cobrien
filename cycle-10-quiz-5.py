# Author: CMOB 2/2/2022

def item_prices(prices, items):
    for rows in items: # goes into the nested list
        for index, value in enumerate(rows): # finds the item in the nested list
            rows[index] = "{0} ${1}".format(value, prices[0]) # adds the price to the items
            del prices[0] # removes price from list to prevent reuse

    return items



print(item_prices([30, 40, 25, 55, 60, 80, 65],[['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]))   

