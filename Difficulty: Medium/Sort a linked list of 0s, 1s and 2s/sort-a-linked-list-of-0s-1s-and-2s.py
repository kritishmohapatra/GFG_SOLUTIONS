'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
	
class Solution:
    def segregate(self, head):
        #code here
        if not head or not head.next:
            return head
        zd=Node(-1)
        od=Node(-1)
        td=Node(-1)
        
        z,o,t=zd, od, td
        c=head
        while c:
            if c.data==0:
                z.next=c
                z=z.next
            elif c.data==1:
                o.next=c
                o=o.next
            else:
                t.next=c
                t=t.next
            c=c.next
        z.next=od.next if od.next else td.next
        o.next=td.next
        t.next=None
        head=zd.next
        return head
    