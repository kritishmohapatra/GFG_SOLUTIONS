class Solution:
    def checkElements(self, A, B, arr):
        # code here
        for i in range(A, B+1):
            if i not in arr:
                return False
        return True
