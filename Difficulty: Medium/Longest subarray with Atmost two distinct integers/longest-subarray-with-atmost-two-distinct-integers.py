class Solution:
    def totalElements(self, arr):
        # Code here
        mp={}
        i=j=0
        maxi=0
        n=len(arr)
        while j<n:
            mp[arr[j]]=mp.get(arr[j], 0)+1
            while len(mp)>2:
                mp[arr[i]]-=1
                if mp[arr[i]]==0:
                    del mp[arr[i]]
                i+=1
            maxi=max(maxi, j-i+1)
            j+=1
        return maxi