"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone_map = {}
        stack = [node]
        visited = set()

        while stack:
            node = stack.pop()
            visited.add(node)
            clone_map[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                stack.append(neighbor)
        
        for prev, curr in clone_map.items():
            for neighbor in prev.neighbors:
                curr.neighbors.append(clone_map[neighbor])
        
        return clone_map[node]