print("Container with most water")


def function(heights):
    n = len(heights)
    max_water = 0
    i = 0
    j = n - 1
    while(i < j):
        high = min(heights[i], heights[j])
        width = (j - i)
        total = high * width
        max_water = max(max_water, total)
        if heights[i] < heights[j]:
            i = i + 1
        else:
            j = j - 1
    return max_water



heights = [1,7,2,5,4,7,3,6]


print(function(heights = [2,2,2]))


