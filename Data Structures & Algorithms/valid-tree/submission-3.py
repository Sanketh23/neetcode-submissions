class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle = True
        visited = set()
        neighborsList = [[] for _ in range(n)]
        for edge in edges:
            neighborsList[edge[0]].append(edge[1])
            neighborsList[edge[1]].append(edge[0])

        def dfs(node, parent):
            nonlocal cycle
            if node in visited:
                cycle = False
                return
            visited.add(node)                
            for neighbor in neighborsList[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
        dfs(0, None)
        if len(visited) == n:
            return cycle
        return False
