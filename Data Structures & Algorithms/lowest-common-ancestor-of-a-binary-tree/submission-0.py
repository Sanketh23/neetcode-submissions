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
        p_list = []
        q_list = []

        curr = p
        while curr:
            p_list.append(curr)
            curr = parentMap[curr]
            
        curr2 = q
        while curr2:
            if curr2 in p_list:
                return curr2
            q_list.append(curr2)
            curr2 = parentMap[curr2]
            
        
        
        
        
        