# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = ListNode(head.val, head.next)
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        left = head
        if left.val != prev.val:
            return False
        while left.next and prev.next:
            if left.val != prev.val:
                return False
            left = left.next
            prev = prev.next
        return True