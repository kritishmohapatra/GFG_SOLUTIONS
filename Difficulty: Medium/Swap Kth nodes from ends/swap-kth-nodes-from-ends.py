'''
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def swapKth(self, head, k):
        # code here
        left,right=None,None
        right=head
        cnt=k
        while right:
            if cnt==1:
                left=head
                ksta=right
            elif cnt<1:
                left=left.next
            right=right.next
            cnt-=1
        if left:
            ksta.data,left.data=left.data,ksta.data
        return head
