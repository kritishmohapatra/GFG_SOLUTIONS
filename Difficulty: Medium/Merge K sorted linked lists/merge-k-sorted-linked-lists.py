import heapq
'''
class Node:
    def _init_(self, x):
        self.data = x
        self.next = None
'''

class Solution:
    def mergeKLists(self, arr):
        # code here
        pq=[]
        for node in arr:
            if node:
                heapq.heappush(pq,(node.data, node))
        d=Node(-1)
        temp=d
        while pq:
            c, curr=heapq.heappop(pq)
            if curr.next:
                heapq.heappush(pq,(curr.next.data, curr.next))
            temp.next=curr
            temp=temp.next
        return d.next

        