# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = head
        while curr.next:
            temp = curr.next
            curr.next = curr
            curr = temp

        left = head
        if left.val != curr.val:
            return False
        while left.next and curr.next:
            print(left.val, curr.val)
            if left.val != curr.val:
                return False
            left = left.next
            curr = curr.next
        return True