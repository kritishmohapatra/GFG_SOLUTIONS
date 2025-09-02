"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        # code here
        if head is None or head.next is None:
            return head
        pre=None
        curr=head
        while curr is not None:
            pre=curr.prev
            curr.prev=curr.next
            curr.next=pre
            curr=curr.prev
        return pre.prev

        