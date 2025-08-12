

class Solution:
    def reverseList(self, head):
        # Code here
        if not head.next:
            return head
        prev=None
        nextn=0
        curr=head
        while curr!=None:
            nextn=curr.next
            curr.next=prev
            prev=curr
            curr=nextn
        return prev