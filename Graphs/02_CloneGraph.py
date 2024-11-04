from collections import deque

class GraphNode:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

# Implementing from bfs
def cloneGraph(src: GraphNode) -> GraphNode:
    m = {}
    q = deque()
    q.append(src)
    
    # Make a clone Node
    m[src] = GraphNode(src.val) 
    
    while q:
        # parent
        u = q.popleft()
        v = u.neighbors # children/neighbor
        
        for nei in v:
            # un-visited children are appended to queue.
            if nei is not m:    
                m[nei] = GraphNode(nei.val)
                q.append(nei)    
            m[u].neighbor.append(m[nei])
            
        # all the children at this level are in Q
    
    return m[src]

def bfs(src: GraphNode):
    visit = {}
    q = deque()
    q.append(src)
    visit[src] = True
    while q:
        # parent node
        u = q.popleft()
        v = u.neighbors
        for nei in v:
            # appending non-visited neighbors/children
            if nei is not visit:
                visit[nei] = True
                q.append(nei) 
        #Q is appended with unvisited-children of parent.

def buildGraph() -> GraphNode:
    """
    Given Graph:
    1--2
    |  |
    4--3
    """
    
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]
    return node1