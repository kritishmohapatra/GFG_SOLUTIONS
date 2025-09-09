'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''


class Solution:

    def deleteMid(self, head):
        '''
        head:  head of given linkedList
        return: head of resultant llist
        '''
        if head==None or head.next==None :
            return None
        fast_ptr=head
        slow_ptr=head
        fast_ptr=fast_ptr.next.next
        while(fast_ptr!=None and fast_ptr.next!=None):
            fast_ptr=fast_ptr.next.next
            slow_ptr=slow_ptr.next
        slow_ptr.next=slow_ptr.next.next
        return head

        #code here