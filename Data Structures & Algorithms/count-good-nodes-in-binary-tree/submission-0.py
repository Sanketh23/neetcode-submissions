# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        good = 0


        while stack:
            node, pathMax = stack.pop()
            if node.val >= pathMax:
                good += 1
                pathMax = node.val
            if node.left:
                stack.append((node.left, pathMax))
            if node.right:
                stack.append((node.right, pathMax))
        return good
