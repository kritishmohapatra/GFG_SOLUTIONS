

from collections import deque, defaultdict
class Solution:
    def shortCycle(self, V, edges):
        # code here
        graph = defaultdict(list)
        
        # Build the adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Initialize result with infinity
        result = float('inf')

        # Perform BFS from each node
        for start in range(V):
            distance = [-1] * V  # Distance from the start node
            parent = [-1] * V    # Parent node for BFS tree

            queue = deque()
            queue.append(start)
            distance[start] = 0

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if distance[neighbor] == -1:
                        distance[neighbor] = distance[current] + 1
                        parent[neighbor] = current
                        queue.append(neighbor)
                    elif parent[current] != neighbor:
                        # Found a cycle
                        cycle_length = distance[current] + distance[neighbor] + 1
                        result = min(result, cycle_length)

        return -1 if result == float('inf') else result