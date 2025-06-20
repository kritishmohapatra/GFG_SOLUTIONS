from collections import Counter
class Solution:
    def validgroup(self, arr ,k):
        # Code here
        mp=Counter(arr)
        if len(arr)%k!=0:
            return False
        arr.sort()
        for i in range(len(arr)):
            if mp[arr[i]]==0:
                continue
            for j in range(k):
                if mp[arr[i]+j]==0:
                    return False
                mp[arr[i]+j]-=1
        return True
                