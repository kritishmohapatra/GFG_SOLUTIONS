class Solution:
    def largest(self, arr):
        # code here
        k=arr[0]
        for i in range(1, len(arr)):
            if(arr[i]>k):
                k=arr[i]
        return k
        
