'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def reverseList(self, head):
        prev = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    def addTwoLists(self, num1, num2):
        # code here
        num1 = self.reverseList(num1)
        num2 = self.reverseList(num2)
        d=Node(-1)
        t=d
        c=0
        while (num1!=None or num2!=None) or c:
            s=0
            if num1!=None:
                s+=num1.data
                num1=num1.next
            if num2!=None:
                s+=num2.data
                num2=num2.next
            s+=c
            c=s//10
            node=Node(s%10)
            t.next=node
            t=t.next
        result = self.reverseList(d.next)

        while result is not None and result.data == 0 and result.next is not None:
            result = result.next

        return result


        return d.next
                