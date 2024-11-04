steps = [
    [-1, 0], # Up
    [0, 1], # Right
    [1, 0], # Bottom
    [0, -1] # Left
]

def withinLimits(row_num, col_num, total_rows, total_cols):
    if 0 <= row_num < total_rows and 0 <= col_num < total_cols:
        return True
    return False


# change this method to bfs
def waterSlope(oceanMatrix, matrix, row, col):
    nrows, ncols = len(matrix), len(matrix[0])
    for i in steps:
        if withinLimits(row + i[0], col + i[1], nrows, ncols):
            if matrix[row+i[0]][col+i[1]] >= matrix[row][col] and not oceanMatrix[row+i[0]][col+i[1]]:
                oceanMatrix[row+i[0]][col+i[1]] = True
                waterSlope(oceanMatrix, matrix, row+i[0], col+i[1])

def commonWaterFlow(matrix):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    pacificMatrix = [[False for _ in range(matrix_cols)] for _ in range(matrix_rows)]
    atlanticMatrix = [[False for _ in range(matrix_cols)] for _ in range(matrix_rows)]
    
    pacificMatrix[0][1] = True
    pacificMatrix[0][2] = True
    
    for i in range(matrix_cols):
        pacificMatrix[0][i] = True
        atlanticMatrix[matrix_rows - 1][i] = True
    
    for i in range(matrix_rows):
        pacificMatrix[i][0] = True
        atlanticMatrix[i][matrix_cols-1] = True 
    
    for i in range(matrix_cols):
        waterSlope(pacificMatrix, matrix, 0, i)
        waterSlope(atlanticMatrix, matrix, matrix_rows-1, i)
    
    
    for i in range(matrix_rows):
        waterSlope(pacificMatrix, matrix, i, 0)
        waterSlope(atlanticMatrix, matrix, i, matrix_cols-1)
    
    Count = 0
    
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            if pacificMatrix[i][j] and atlanticMatrix[i][j]:
                Count += 1
    
    return Count

mat = [
    [1, 2, 2, 3, 5],    # [T, T, T, T, T]       #[F, F, F, F, T]
    [3, 2, 3, 4, 4],    # [T, T, T, T, T]       #[F, F, F, T, T]
    [2, 4, 5, 3, 1],    # [T, T, T, F, F]       #[F, F, T, T, T]
    [6, 7, 1, 4, 5],    # [T, T, F, F, F]       #[T, T, T, T, T]
    [5, 1, 1, 2, 4]     # [T, F, F, F, F]       #[T, T, T, T, T]
]

print(commonWaterFlow(mat))