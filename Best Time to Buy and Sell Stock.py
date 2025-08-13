def function(prices):
    n = len(prices)
    min_price = float('inf')
    max_profit = 0
    for i in range(n):
        if(prices[i] < min_price):
            min_price = prices[i]
        profit = prices[i] - min_price
        if(profit > max_profit):
            max_profit = profit



    return max_profit
        



print(function(prices=[7,1,2,4,6,7]))