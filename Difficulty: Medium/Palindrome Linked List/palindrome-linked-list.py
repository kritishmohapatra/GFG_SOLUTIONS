'''
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        new_head=self.reverse(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head
    def isPalindrome(self, head):
        #code here
        if head is None or head.next is None:
            return True
        slow=head
        fast=head
        while fast.next is not None  and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        new_head=self.reverse(slow.next)
        first=head
        second=new_head
        while second is not None:
            if first.data!=second.data:
                self.reverse(new_head)
                return False
            first=first.next
            second=second.next
        self.reverse(new_head)
        return True
