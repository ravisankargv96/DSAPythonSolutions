from collections import deque

class GraphNode:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

def cloneGraph(src: GraphNode) -> GraphNode:
    # A Map to keep track of all the
    # nodes which have already been created
    m = {}
    q = deque()

    # Enqueue src node
    q.append(src)
    node = None

    # Make a clone Node
    node = GraphNode()
    node.val = src.val

    # Put the clone node into the Map
    m[src] = node
    while q:
        # Get the front node from the queue
        # and then visit all its neighbors
        u = q.popleft()
        v = u.neighbors
        for neighbor in v:
            # Check if this node has already been created
            if neighbor not in m:
                # If not then create a new Node and
                # put into the HashMap
                node = GraphNode()
                node.val = neighbor.val
                m[neighbor] = node
                q.append(neighbor)

            # Add these neighbors to the cloned graph node
            m[u].neighbors.append(m[neighbor])

    # Return the address of cloned src Node
    return m[src]

# Build the desired graph
def buildGraph() -> GraphNode:
    """
    Given Graph:
    1--2
    | |
    4--3
    """
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node3, node1]
    return node1

# A simple bfs traversal of a graph to
# check for proper cloning of the graph
def bfs(src: GraphNode):
    visit = {}
    q = deque()
    q.append(src)
    visit[src] = True
    while q:
        u = q.popleft()
        print(f"Value of Node {u.val}")
        print(f"Address of Node {u}")
        v = u.neighbors
        for neighbor in v:
            if neighbor not in visit:
                visit[neighbor] = True
                q.append(neighbor)

if __name__ == "__main__":
    src = buildGraph()
    print("BFS Traversal before cloning")
    bfs(src)
    clone = cloneGraph(src)
    print("\nBFS Traversal after cloning")
    bfs(clone)

    # This code is contributed by vikramshirsath177
