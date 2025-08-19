#User function Template for python3

class Solution:
    def uniqueId(self, arr):
        #  code here
        ans = []
    
        for i in arr:
            if i not in ans:
                ans.append(i)
        del arr
        return ans
    
