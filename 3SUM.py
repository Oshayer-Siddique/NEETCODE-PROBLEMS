print("3SUM")

def function(nums):
    res = []
    n = len(nums)
    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i + 1
        k = n - 1
        while(j < k):
            sum = nums[i] + nums[j] + nums[k]
            if(sum > 0):
                k = k - 1
            elif(sum < 0):
                j = j + 1
            else:
                res.append([nums[i],nums[j],nums[k]])

                while(j < k):
                    if nums[j] == nums[j+1]:
                        j = j + 1
                    else:
                        break
                while(j < k):
                    if nums[k] == nums[k-1]:
                        k = k - 1
                    else:
                        break
                j += 1
                k -= 1

                    

                
    return res


print(function(nums=[-1,0,1,2,-1,-4]))
