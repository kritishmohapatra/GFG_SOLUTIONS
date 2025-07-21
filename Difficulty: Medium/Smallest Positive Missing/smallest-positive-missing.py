#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        f=0
        k=set(arr)
        for i in range(1, len(arr)+1):
            if i not in k:
                return i
        if f==0:
            return len(arr)+1


