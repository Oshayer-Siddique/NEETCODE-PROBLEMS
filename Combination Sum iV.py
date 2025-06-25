print("Combination Sum iV")

def function(nums, target):
    array = [0 for i in range(target + 1)]
    array[0] = 1
    for i in range(1,target+1):
        for j in range(len(nums)):
            if(nums[j] < i):
                array[i] = array[i] + array[i - nums[j]]
    return array[target]


