class Solution:
    def nextLargerElement(self, arr):
        # code here
        ans=[]
        stack=[]
        n=len(arr)
        for i in range(2*n-1, -1, -1):
            while len(stack)>0 and arr[i%n]>=stack[-1]:
                stack.pop()
            if i<n:
                if len(stack)==0:
                    ans.append(-1)
                else:
                    ans.append(stack[-1])
            stack.append(arr[i%n])

        return ans[::-1]