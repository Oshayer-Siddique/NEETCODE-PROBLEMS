print("Two Integer Sum II")


def function(numbers,target):
    res = []
    n = len(numbers)
    i = 0
    j = n - 1
    while(i <= j):
        if(numbers[i] + numbers[j] > target):
            j = j - 1
        elif(numbers[i] + numbers[j] <target):
            i = i + 1
        else:
            res.append(i+1)
            res.append(j+1)
            break
    return res


    

print(function(numbers=[1,2,3,4],target=3))

