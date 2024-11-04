from collections import deque

class Solution:
    
    def canFinish(self, numTasks, prerequisites):
        graph = [[] for _ in range(numTasks)]
        inDegree = [0] * numTasks
        
        # Initialize graph & indegree
        for edge in prerequisites:
            graph[edge[0]].append(edge[1])
            inDegree[edge[1]] += 1
        
        queue = deque()
        
        # Push all the nodes with no dependencies
        # (in-degree = 0) into the queue
        for i in range(numTasks):
            if inDegree[i] == 0:
                queue.append(i)
        
        # For all the children nodes push (in-degree = 0) into the queue.
        
        while queue:
            node = queue.popleft()
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
            
            # All indegree = 0 of next-level are present in Q
        
        # Check if there is a node whose in-degree is not zero
        for i in range(numTasks):
            if inDegree[i] != 0:
                return False
            
        return True
    
if __name__ == "__main__":
    numTasks = 4
    prerequisites = [
        [1, 0],
        [2, 1],
        [3, 2]
    ]
    
    sol = Solution()
    
    if sol.canFinish(numTasks, prerequisites):
        print("Possible to finish all tasks")
    else:
        print("Impossible to finish all tasks")