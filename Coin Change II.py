print("Coin Change 2")

def function(amount, coins):
    row = len(coins)
    col = amount
    array = [[0 for i in range(col+1)] for j in range(row)]
    for i in range(row):
        array[i][0] = 1
    for i in range(row):
        for j in range(amount+1):
            if(coins[i] > j):
                array[i][j] = array[i-1][j]
            else:
                if i > 0:
                    no_keep = array[i-1][j]
                else:
                    no_keep = 0
                keep = array[i][j - coins[i]]

                array[i][j] = keep + no_keep
    ans = array[row-1][col]
    return ans


print(function(amount=4,coins=[1,2,3]))