MAX_LEN = 6
CATALAN = [1] * MAX_LEN
for i in range(1, len(CATALAN)):
    CATALAN[i] = CATALAN[i - 1] * 2 * (2 * i - 1) // (i + 1)
class Solution:
    def countBSTs(self, arr):
        # Code here
        from bisect import bisect_left
        n = len(arr)
        order = sorted(arr)
        ans = [0] * n
        for i, a in enumerate(arr):
            less = bisect_left(order, a)
            more = n - 1 - less
            ans[i] = CATALAN[less] * CATALAN[more]
        return ans