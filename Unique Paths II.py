print("Unique Paths 2")



def function(obstacleGrid):
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    matrix = [[0 for i in range(col)] for j in range(row)]


    if obstacleGrid[0][0] == 1:
        return 0
    else:
        matrix[0][0] = 1


    for i in range(1,row):
        if obstacleGrid[i][0] == 1:
            matrix[i][0] = 0
        else:
            matrix[i][0] = matrix[i-1][0]

    for j in range(1,col):
        if obstacleGrid[0][j] == 1:
            matrix[0][j] = 0
        else:
            matrix[0][j] = matrix[0][j-1]


    
    for i in range(1, row):
        for j in range(1,col):
            if obstacleGrid[i][j] == 0:
                matrix[i][j] = matrix[i-1][j] +  matrix[i][j-1]
            else:
                matrix[i][j] = 0

    

    return matrix[row-1][col-1]




obstacleGrid = [[0,0,0],[0,0,0],[0,1,0]]



print(function(obstacleGrid))   

