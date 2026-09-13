# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        parentMap = {root:None}
        while queue:
            node = queue.popleft()
            if node.right:
                parentMap[node.right] = (node)
                queue.append(node.right)
            if node.left:
                parentMap[node.left] = (node)
                queue.append(node.left)
        p_set = defaultdict(int)
        q_list = []

        curr = p
        while curr:
            p_set[curr] = 1
            curr = parentMap[curr]
            
        curr2 = q
        while curr2:
            if p_set[curr2]:
                return curr2
            q_list.append(curr2)
            curr2 = parentMap[curr2]
            
        
        
        
        
        