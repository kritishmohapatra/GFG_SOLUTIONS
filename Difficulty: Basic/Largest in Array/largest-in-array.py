class Solution:
    def largest(self, arr):
        # code here
        ans=arr[0]
        for i in range(1, len(arr)):
            if ans<arr[i]:
                ans=arr[i]
        return ans
