"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Dictionary to store old node -> new node mapping
        old_to_new = {}
        curr = head
        # First pass: create all nodes and map them
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        # Second pass: assign next and random pointers
        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next
        # Return the head of the copied list
        return old_to_new.get(head)