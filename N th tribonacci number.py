print("N th tribonacci")



def function(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    nums = [0 for i in range(n+1)]
    nums[0] = 0
    nums[1] = 1
    nums[2] = 1


    for i in range(3,n+1,+1):
        nums[i] = nums[i-1] + nums[i-2] + nums[i-3]
    return nums[n]


 

print(function(21))