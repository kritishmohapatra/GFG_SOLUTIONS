'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

'''
class BSTIterator:

    def __init__(self, root, rev):
        self.stack = []
        self.rever=rev
        self.push(root)  # <-- Needed to initialize stack with leftmost path

    def next(self) -> int:
        cur = self.stack.pop()
        if not self.rever:
            self.push(cur.right)
        else:
            self.push(cur.left)
        return cur.data

    def hasNext(self) -> bool:
        return bool(self.stack)

    def push(self, node):
        while node:
            self.stack.append(node)
            if self.rever:
                node = node.right
            else:
                node=node.left
class Solution:
    def findTarget(self, root, target): 
        # your code here.
        if not root:
            return False
        l=BSTIterator(root, False)
        r=BSTIterator(root, True)

        i=l.next()
        j=r.next()

        while i<j:
            if i+j==target:
                return True
            elif i+j<target:
                i=l.next()
            else:
                j=r.next()
        return False