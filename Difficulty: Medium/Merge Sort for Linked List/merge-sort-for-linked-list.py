'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def mergingTwoList(self,l1,l2):
        dummy=Node(0)
        currNode=dummy
        
        while l1 and l2:
            if l1.data<l2.data:
                currNode.next=l1
                l1=l1.next
            else:
                currNode.next=l2
                l2=l2.next
            currNode=currNode.next
        
        if l1:
            currNode.next=l1
        if l2:
            currNode.next=l2
        return dummy.next
            
    
    def findMiddle(self,head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def printList(self,head):
        while head:
            print(head.data)
            head=head.next
    def mergeSort(self, head):
        # code here
        if head is None or head.next is None:
            return head
        middle=self.findMiddle(head)
        r=middle.next
        middle.next=None
        l=head
        
        x=self.mergeSort(l)
        y=self.mergeSort(r)
        
        return self.mergingTwoList(x,y)
        # code here
        