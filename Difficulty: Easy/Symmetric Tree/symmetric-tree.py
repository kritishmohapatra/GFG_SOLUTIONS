#User function Template for python3

class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def check(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.data!=q.data:
            return 0
        left=self.check(p.left, q.right)
        right=self.check(p.right, q.left)
        return left and right
        
        
    def isSymmetric(self, root):
        # Your Code Here
        return self.check(root, root)


