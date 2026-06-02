numBottles = 9, numExchange = 3

def numWaterBottles(numBottles, numExchange):
    for numBottles in range(numBottles, 0, -1):
        exchange = numBottles // numExchange
        numBottles += exchange