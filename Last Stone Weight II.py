print("Last Stone Weight II")

def function(stones):
    total = sum(stones)
    target = total // 2

    dp = [0 for i in range(target+1)]
    dp[0] = 1


    for i in range(len(stones)):
        for j in range(target, stones[i] - 1, -1):
            if(dp[j - stones[i]] == 1):
                dp[j] = 1
    for t in range(target , -1 , -1):
        if(dp[t] == 1):
            ans = total - 2 * t
            break
    return ans

    



stones = [2,4,1,5,6,3]

print(function(stones))
