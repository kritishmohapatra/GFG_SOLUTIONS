class Solution:
    def longestSubarray(self, arr):
        # code here
        if not arr:
            return 0
   
        n = len(arr)
       
        prev_greater = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                prev_greater[i] = stack[-1]
            stack.append(i)
    
        next_greater = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            if stack:
                next_greater[i] = stack[-1]
            stack.append(i)
    
        max_len = 0
        for i in range(n):
            span = next_greater[i] - prev_greater[i] - 1
           
            if arr[i] <= span:
                max_len = max(max_len, span)
               
        return max_len