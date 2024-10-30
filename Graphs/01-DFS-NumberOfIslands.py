from typing import List

def dfs(grid: List[List[str]], r: int, c: int, rows: int, cols: int):
    
    # Check if current position is out of bounds or already visited/water
    if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
        return
    
    # Mark the cell as visited by setting it to '0'
    grid[r][c] = '0'
    
    # Visit all adjacent cells (up, down, left, right)
    dfs(grid, r - 1, c, rows, cols)  # Up
    dfs(grid, r + 1, c, rows, cols)  # Down
    dfs(grid, r, c - 1, rows, cols)  # Left
    dfs(grid, r, c + 1, rows, cols)  # Right


# Main function to count the number of islands
def numIslands(grid: List[List[str]]) -> int:
    
    # If the grid is empty, there are no islands
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    
    num_islands = 0

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            
            if grid[r][c] == '1':
                num_islands += 1  # Increment the island count
                dfs(grid, r, c, rows, cols)

    return num_islands
