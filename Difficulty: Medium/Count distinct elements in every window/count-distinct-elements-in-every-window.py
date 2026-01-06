class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        m=defaultdict(int)
        n=len(arr)
        ans=[]
        for i in range(k):
            m[arr[i]]+=1
        ans.append(len(m))
        for i in range(k,n):
            m[arr[i-k]]-=1
            if m[arr[i-k]]==0:
                del m[arr[i-k]]
            m[arr[i]]+=1
            ans.append(len(m))
        return ans