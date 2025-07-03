print("Minimum Path Sum")

def function(grid):
    row = len(grid)
    col = len(grid[0])

    matrix = [[0 for i in range(col)] for j in range(row)]

    matrix[0][0] =grid[0][0]

    for i in range(1, row):
        matrix[i][0] = matrix[i-1][0] + grid[i][0]
    for j in range(1,col):
        matrix[0][j] = matrix[0][j-1] + grid[0][j]


    for i in range(1, row):
        for j in range(1, col):
            matrix[i][j] = grid[i][j] + min(matrix[i-1][j], matrix[i][j-1])

    return matrix[row-1][col-1]


grid = [
    [1,2,0],
    [5,4,2],
    [1,1,3]
]


print(function(grid))