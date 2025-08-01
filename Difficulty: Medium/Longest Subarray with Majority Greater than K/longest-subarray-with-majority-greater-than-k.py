
#User function Template for python3
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        mp={0:-1}
        pf=0
        maxi=0
        for i in range(len(arr)):
            if arr[i]>k:
                pf+=1
            else:
                pf-=1
            if pf>0:
                maxi=i+1
            if pf-1 in mp:
                maxi=max(maxi, i-mp[pf-1])
            if pf not in mp:
                mp[pf]=i
        return maxi

