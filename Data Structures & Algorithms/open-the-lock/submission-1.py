class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        q = deque([("0000", 0)])

        def bfs(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i]) - 1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res

        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for node in bfs(lock):
                if node not in visited:
                    visited.add(node)
                    q.append((node, turns + 1))
        
        return -1
                
                
        
        
        
