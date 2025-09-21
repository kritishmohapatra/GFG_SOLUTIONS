class Solution:
    def maxOfMins(self, arr):
       # code here
        def pse(arr, n):
            s=[]
            res=[-1]*n
            for i in range(n):
                while len(s)>0 and arr[s[-1]]>=arr[i]:
                   s.pop()
                if s:
                    res[i]=s[-1]
                s.append(i)
            return res
        def nse(arr, n):
            s=[]
            res=[n]*n
            for i in range(n-1,-1, -1):
                while len(s)>0 and arr[s[-1]]>=arr[i]:
                   s.pop()
                if s:
                    res[i]=s[-1]
                s.append(i)
            return res
        n=len(arr)
        ps=pse(arr, n)
        ns=nse(arr, n)
        ans=[0]*(n)
        for i in range(n):
            w=ns[i]-ps[i]-1
            ans[w-1]=max(ans[w-1], arr[i])
        for i in range(n-2, -1, -1):
            ans[i]=max(ans[i], ans[i+1])
        return ans
               