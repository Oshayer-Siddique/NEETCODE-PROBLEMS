print("Decode Ways")


def function(s):
    n = len(s)
    if not s or s[0] == "0":
        return 0
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        one = int(s[i-1:i])
        two = int(s[i-2:i])
        if 1<= one <= 9:
            dp[i] = dp[i] + dp[i-1]
        if 10<= two <= 26:
            dp[i] = dp[i] + dp[i-2]
        
    return dp[n]





s = "12"

print(function(s))