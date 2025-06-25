print("Minimum cost of climbing stairs")


def function(cost):
    
    n = len(cost)
    def newfunction(n):
        if n == 1 or n == 0:
            return 0
        else:
            return min(newfunction(n-1) + cost[n-1], newfunction(n-2) + cost[n-2])
    return newfunction(n)

cost = [1,2,3]



print(function(cost))

