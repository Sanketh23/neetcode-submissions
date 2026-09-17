# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left:
            qLeft = deque([root.left])
        if root.right:
            qRight = deque([root.right])
        rightDepth, leftDepth = 0, 0

        while qRight:
            for i in range(len(qRight)):
                node = qRight.popleft()
                if node.left:
                    qRight.append(node.left)
                if node.right:
                    qRight.append(node.right)
            rightDepth += 1

        while qLeft:
            for i in range(len(qLeft)):
                node = qLeft.popleft()
                if node.left:
                    qLeft.append(node.left)
                if node.right:
                    qLeft.append(node.right)
            leftDepth += 1

        return (abs(leftDepth - rightDepth) <= 1)