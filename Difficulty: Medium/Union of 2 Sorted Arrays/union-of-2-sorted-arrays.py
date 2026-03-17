class Solution:
    def findUnion(self, a, b):
        # code here 
        u=[]
        i, j=0,0
        n=len(a)
        m=len(b)
        while i<n and j<m:
            if a[i]<b[j]:
                if not u or u[-1]!=a[i]:
                    u.append(a[i])
                i+=1
            elif a[i]>b[j]:
                if not u or u[-1]!=b[j]:
                    u.append(b[j])
                j+=1
            else:
                if not u or u[-1]!=a[i]:
                    u.append(a[i])
                i+=1
                j+=1
        while i<n:
            if not u or u[-1]!=a[i]:
                u.append(a[i])
            i+=1
        while j<m:
            if not u or u[-1]!=b[j]:
                u.append(b[j])
            j+=1
        return u