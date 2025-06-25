print("Concentration of  array")


def function(nums):
    n = len(nums)
    ans = [0 for i in range(2*n)]
    for i in range(n):
        ans[i] = nums[i]
    for i in range(n):
        ans[i+n] = nums[i]

    return ans


print(function(nums=[1,4,1,2]))