print("Perfect Squares")


import math

def function(n):
    nums = []
    for i in range(1,int(math.sqrt(n)+1),+1):
        nums.append(i*i)
    row = len(nums)
    col = n
    array = [[(10**10) for i in range(col+1)] for j in range(row)]
    for i in range(row):
        array[i][0] = 0
    for i in range(row):
        for j in range(n+1):
            if(nums[i] > j):
                array[i][j] = array[i-1][j]
            else:
                if i > 0:
                    no_take = array[i-1][j]
                else:
                    no_take = 10 ** 10
                take = 1 + array[i][j - nums[i]]
                array[i][j] = min(take,no_take)
    ans = array[row-1][col]
    return -1 if ans == 10**10 else ans





n = 13

print(function(n))





