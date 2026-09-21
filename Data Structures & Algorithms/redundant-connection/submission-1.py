class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        for edge in reversed(edges):
            adjList = [[] for _ in range(n + 1)]

            for src, dst in edges:
                if [src, dst] == edge:
                    continue                      
                adjList[src].append(dst)
                adjList[dst].append(src)

            queue = deque([1])
            visited = {1}
            while queue:
                node = queue.popleft()
                for neighbor in adjList[node]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)        
                    queue.append(neighbor)

            if len(visited) == n:             
                return edge

        return []