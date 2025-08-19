#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        res=0
        n=len(arr)
        curr=0
        for i in range(n):
            if arr[i]==0:
                curr+=1
            else:
                res+=(curr*(curr+1))//2
                curr=0
        res+=(curr*(curr+1))//2
        return res