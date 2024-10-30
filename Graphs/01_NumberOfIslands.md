**Bfs**:

> ```python
>grid
>(r,c) # cell index
>(rows, cols) # mxn
> visited # grid_shape + tracking
> ```

##### BFS Algo:
1. *Store visited cells in Q*:
```python
visited[r][c] = '1'
Q.append((r,c))
```
2. *loop:*`len(Q) > 0`
  1. get current cell `row, col`
  ```python
  row, col = Q.popleft()
  ```
  2. look around neighbours
  ```python
  [
    (row - 1, col), # = up
    (row + 1, col), # = down
    (row, col - 1), # = left
    (row, col + 1)  # = right
  ]
  ```
  3. Add unvisited neighbours
  ```python
  for n_row, n_col in [up, down, left, right]
  ```
    * New cell should be in the grid
    * Cell will be land `1`
    * Cell is unvisited
  ```python
          # it should be unvisited land in the grid.
          if  0 < n_row < len(grid) # row
              and 0 < n_col < len(grid[0]) # col
              and grid[n_row][n_col] == "1" # land
              and not visited[n_row][n_col]: # not visited
  ```
    * ***Visit them & add to Q***
    ```python
              visited[n_row][n_col] = 1 # visited.
              Q.append((n_row, n_col)) # added to queue
    ```



```python
from typing import List
from collections import deque
```


```python
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
```

### NumIslands:

##### 1. Null check
```python
grid: [[]]
# given list should not be null, if it's null return 0
not grid or not grid[0]
```

##### 2. Get grid size.
```python
# [
#   [0, 0, 0],
#   [0, 0, 0],
# ]  
rows = len(grid)
cols = len(grid[0])
```

##### 3. Traverse across the grid
```python
for r in rows:
  for c in cols:
```
  * Explore each island
  * Increment the count
  * Mark it as visited `bfs` takes care of it.
  ```python
  if grid[r][c] == '1':
          num_islands += 1 # increment the count
          bfs(r,c, visited) # Exploring & marking it as visited
  ```

##### 4. Returns total count
```python
return num_islands
```


```python

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

```

### Dfs:

> ```python
>grid
>(r,c) # cell index
>(rows, cols) # mxn
> ```

##### Boundary Conditions:
1. *Out of bounds*:
```python
r < 0 or c < 0 or r >= rows or c >= cols
```
2. *Already Visited* or *Contains water*:
```python
grid[r][c] == '0'
```

#### Traversal Begins
```python
grid[r][c] == '0' # visit the cell
```

#### Explore all 4 directions
```python
# current (r, c)
dfs(r - 1, c)  # Up
dfs(r + 1, c)  # Down
dfs(r, c - 1)  # Left
dfs(r, c + 1)  # Right
```


```python
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

```

### NumIslands:

##### 1. Null check
```python
grid: [[]]
# given list should not be null, if it's null return 0
not grid or not grid[0]
```

##### 2. Get grid size.
```python
# [
#   [0, 0, 0],
#   [0, 0, 0],
# ]  
rows = len(grid)
cols = len(grid[0])
```

##### 3. Traverse across the grid
```python
for r in rows:
  for c in cols:
```
  * Explore each island
  * Increment the count
  * Mark it as water `dfs` takes care of it.
  ```python
  if grid[r][c] == '1':
          num_islands += 1 # increment the count
          dfs(r,c) # Exploring & marking it as water
  ```

##### 4. Returns total count
```python
return num_islands
```


```python
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
```
