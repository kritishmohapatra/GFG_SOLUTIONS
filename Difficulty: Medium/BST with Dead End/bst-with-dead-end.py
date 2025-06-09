class Solution:
    def  solve(self, root, mini, maxi):
        if root is None:
            return False
        if  root.left is None and root.right is None and mini==maxi:
            return True
        return self.solve(root.left, mini, root.data-1) or self.solve(root.right, root.data+1, maxi)
    def isDeadEnd(self, root):
        # Code here
        return self.solve(root, 1, float("inf"))