#User function Template for python3

class Solution:
    def isBSTTraversal(self, arr):
        # Code here
        for i in range(1,len(arr)):
            if arr[i]<=arr[i-1]:
                return False
        return True