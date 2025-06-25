print("Unique Paths")


def function(m,n):
    row  = m-1
    col =  n-1
    array  = [[0 for i in range(col+1)] for j in range(row+1)]
    for i in range(row+1):
        array[i][0] = 1
    for j in range(col+1):
        array[0][j] = 1
    for i in range(1,row+1):
        for j in range(1,col+1):
            array[i][j] = array[i-1][j] + array[i][j-1]



    return array[row][col] 


print(function(3,6))
