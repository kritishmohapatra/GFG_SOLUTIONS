class Solution:
    def nse(self, arr, n):
        stack=[]
        res=[-1]*n
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]
            else:
                res[i]=n
            stack.append(i)
        return res
    def pse(self, arr):
        res=[]
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if not st:
                res.append(-1)
            else:
                res.append(st[-1])
            st.append(i)
        return res
                 
    def sumSubMins(self, arr):
        # Code her
        ns=self.nse(arr, len(arr))
        ps=self.pse(arr)
        res=0
        for i in range(len(arr)):
            res+=arr[i]*(ns[i]-i)*(i-ps[i])
        return res