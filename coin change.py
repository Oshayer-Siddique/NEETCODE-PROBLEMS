print("Coin change")



def function(coins,amount):
    row = len(coins)
    col = amount
    array = [[(10**10) for i in range(col+1)] for j in range(row)]
    for i in range(row):
        array[i][0] = 0
    for i in range(row):
        for j in range(amount+1):
            if(coins[i] > j):
                array[i][j] = array[i-1][j]
            else:
                if i > 0:
                    no_keep = array[i-1][j]
                else:
                    no_keep = 10**10
                keep = 1 + array[i][j - coins[i]]
                array[i][j] = min(keep,no_keep)
    
    ans =  array[row-1][col]
    return -1 if ans == 10**10 else ans


print(function(coins=[1,5,6,9], amount=10))

    