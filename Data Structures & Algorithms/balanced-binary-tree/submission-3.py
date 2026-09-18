# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node is None:
                return [0, True]
            leftH, leftBalanced = dfs(node.left)
            rightH, rightBalanced = dfs(node.right)

            height = 1 + max(leftH, rightH)

            balanced = leftBalanced and rightBalanced and abs(leftH - rightH) <= 1
            return [height, balanced]
        
        return dfs(root)[1]
