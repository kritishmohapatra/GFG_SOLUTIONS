class Solution:
    def nge(self, arr, n):
        stack = []
        res = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res

    def pge(self, arr):
        res = []
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(i)
        return res

    def sumSubarrayMaxs(self, arr):
        n = len(arr)
        ng = self.nge(arr, n)
        pg = self.pge(arr)
        ans = 0
        for i in range(n):
            ans += arr[i] * (ng[i] - i) * (i - pg[i])
        return ans

    def nse(self, arr, n):
        stack = []
        res = [n] * n
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(i)
        return res

    def pse(self, arr):
        res = []
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            res.append(stack[-1] if stack else -1)
            stack.append(i)
        return res

    def sumSubarrayMins(self, arr):
        n = len(arr)
        ns = self.nse(arr, n)
        ps = self.pse(arr)
        ans = 0
        for i in range(n):
            ans += arr[i] * (ns[i] - i) * (i - ps[i])
        return ans
    def subarrayRanges(self, arr):
        # Code here
         return self.sumSubarrayMaxs(arr) - self.sumSubarrayMins(arr)
        