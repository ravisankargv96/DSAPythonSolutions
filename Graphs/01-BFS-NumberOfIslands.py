from typing import List
from collections import deque

# Helper function to perform BFS and mark connected land as visited
def bfs(grid: List[List[str]], r: int, c: int, rows: int, cols: int, visited: set):
    q = deque()
    visited.add((r, c))
    q.append((r, c))
    
    while q:
        row, col = q.popleft()
        # Define directions for moving up, down, left, and right
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for dr, dc in directions:
            new_r, new_c = row + dr, col + dc
            # Check boundaries, unvisited land, and mark it visited
            if (new_r in range(rows) and new_c in range(cols) 
                and grid[new_r][new_c] == '1' 
                and (new_r, new_c) not in visited):
                
                q.append((new_r, new_c))
                visited.add((new_r, new_c))

# Main function to count the number of islands
def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    # Traverse each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land ('1') and hasn't been visited, it's a new island
            if grid[r][c] == "1" and (r, c) not in visited:
                bfs(grid, r, c, rows, cols, visited)  # Perform BFS to mark the entire island
                islands += 1  # Increment island count

    return islands
