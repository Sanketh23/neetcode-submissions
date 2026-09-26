# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            head = None
            return head
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        remove_length = length - n
        curr2_length = 0
        curr2 = head
        while curr2.next and curr2.next.next:
            curr2_length += 1

            if curr2_length == remove_length:
                curr2.next = curr2.next.next
                curr2.next.next = None
            curr2 = curr2.next
        return head        