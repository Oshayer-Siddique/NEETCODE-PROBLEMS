print("4SUM")


def function(nums,target):
    res = []
    n = len(nums)
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            k = j + 1
            m = n - 1
            while(k < m):
                sum = nums[i] + nums[j] + nums[k] + nums[m]
                if(sum > target):
                    m = m - 1
                elif(sum < target):
                    k = k + 1
                else:
                    res.append([nums[i] , nums[j] , nums[k] , nums[m]])
                    while(k < m):
                        if(nums[k] == nums[k+1]):
                            k = k + 1
                        else:
                            break
                    while(k < m):
                        if(nums[m] == nums[m-1]):
                            m = m - 1
                        else:
                            break
                    k = k + 1
                    m = m - 1

    return res




nums = [3,2,3,-3,1,0]
target = 3

print(function(nums = [1,-1,1,-1,1,-1],target = 2))