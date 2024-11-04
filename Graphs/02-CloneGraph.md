```python
jupyter nbconvert 02-CloneGraph.ipynb --to markdown --output 02-CloneGraph.md
```


      File "<ipython-input-1-3d7c5850d1a3>", line 1
        jupyter nbconvert 02-CloneGraph.ipynb --to markdown --output 02-CloneGraph.md
                          ^
    SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers



# Clone Graph:
###Solving approach: BFS
**storing visited clones in HashMap**
```python
clones = {} # {node: copy_node}
```
1. Handling the edge case
```python
if not node:
      return node #None
```
2. Using BFS in traversing original graph
```python
clones[node] = Node(node.val) # {node1: copy_node1}
Q = [node] # Q initialization
```
3. Traversal begins `Q > 0`
  1. Standing on: current node, copyNode
```python
  node = Q.deque()
  copyNode = clones[node]
```
  2. Visit neighbours of node (in original graph)
  ```python
  for nei in node.neighbours:
  ```
    a. Non-visited neighbour: create clone, add to queue (& traverse)
  ```python
  if nei not in clones:
        clones[nei] = Node(node.val)
        Q.append(nei)
  ```
    b. Visited neighbour: add it as neighbour to copyNode
  ```python
  copyNode.neighbours.append(clones[nei])
  ```
4. return `clones[node]`


```python
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return node

        q, clones = deque([node]), {node.val: Node(node.val, [])}
        while q:
            cur = q.popleft()
            cur_clone = clones[cur.val]

            for ngbr in cur.neighbors:
                if ngbr.val not in clones:
                    clones[ngbr.val] = Node(ngbr.val, [])
                    q.append(ngbr)

                cur_clone.neighbors.append(clones[ngbr.val])

        return clones[node.val]
```

# Clone Graph:
###Solving approach: DFS
**storing visited clones in HashMap**
```python
clones = {} # {node: copy_node}
```
1. Handling the edge case
```python
if not node:
      return node #None
```
2. Using DFS in traversing original graph
```python
def clone(node: Node) -> Node:
```
  1. Visited node : return `copy`
  ```python
  if node in clones:
        return clones[node]
  ```
  2. Non-Visited node: traverse
  ```python
  copy = Node(node.val)
  clones[node] = copy # {node1: copy1}
  ```
    1. Visit all the neighbors
    ```python
    for nei in node.neighbors:
            copy.neighbors.append(clone(nei))
    ```
    2. Now we have `copy`, `copy.neighbors`
    ```python
    return copy
    ```


```python
def cloneGraph(self, node: 'Node') -> 'Node':
  if not node:
    return node # None

  clones = {}

  return clone(node, clones)

```


```python
def clone(node, clones):
    if node in clones:
      return clones[node]

    copy = Node(node.val)
    clones[node] = copy

    for nei in node.neighbors:
      copy.neighbors.append(clone(nei))
    return copy
```


