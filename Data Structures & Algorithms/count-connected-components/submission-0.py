class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = list(range(n))

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])
            return par[x]
        
        for a1, b1 in edges:
            if find(a1) == find(b1):
                continue
            par[find(a1)] = find(b1)
            n -= 1
        
        return n

        