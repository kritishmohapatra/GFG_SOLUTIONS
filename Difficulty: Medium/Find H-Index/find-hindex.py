class Solution:
    def hIndex(self, citations):
        #code here
        citations.sort()
        n,ans=len(citations), 0
        for i in range(n-1, -1, -1):
            if citations[i]>=n-i:
                ans+=1
            else:
                break
        return ans