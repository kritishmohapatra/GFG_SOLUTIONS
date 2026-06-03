class Solution:
    def countFreq(self, arr):
        #code here
        mp={}
        for i in arr:
            mp[i]=mp.get(i,0)+1
        ans=[]
        for k, v in mp.items():
            ans.append([k, v])
        return ans