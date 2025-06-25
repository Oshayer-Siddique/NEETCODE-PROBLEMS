print("Climbing Stairs")


ways = [0 for i in range(30)]

def function(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return function(n-1) + function(n-2)


print(function(n=30))