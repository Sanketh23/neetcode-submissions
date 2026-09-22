class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [0] * (n+1)
        for i in range(n + 1):
            par[i] = i

        rank = [1] * (n+1)

        def find(n):
            if n != par[n]:
                par[n] = find(par[n])
            return par[n]
        
        def union(x, y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for x, y in edges:
            if not union(x,y):
                return [x,y]
        
        
        