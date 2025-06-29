print("Partition Equal Subset Sum")


def function1(nums ,target):
    n = len(nums)
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for i in range(len(nums)):
        for t in range(target, nums[i] - 1 , - 1):
            if(dp[t - nums[i]]) == 1:
                dp[t] = 1
    if dp[target] == 1:
        return True
    else:
        return False
    

def function2(nums):
    if(sum(nums) % 2 == 1):
        return False
    subTotal = sum(nums) // 2

    if(function1(nums,subTotal) == True):
        return True
    else:
        return False



nums = [1,2,3,4]

print(function2(nums = [1,2,3,4,5]))
