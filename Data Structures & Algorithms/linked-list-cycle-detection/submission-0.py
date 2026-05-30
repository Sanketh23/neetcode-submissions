# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = set()
        while head.next:
            if head.next in nodes:
                return True
            nodes.add(head.next)
            head = head.next
        
        return False