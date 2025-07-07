# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        ans=[]
        s=[]
        for i in range(len(arr)-1, -1, -1):
            while len(s)>0 and arr[i]>=s[-1]:
                s.pop()
            if len(s)==0:
                ans.append(-1)
                s.append(arr[i])
            else:
                ans.append(s[-1])
                s.append(arr[i])
        return ans[::-1]


