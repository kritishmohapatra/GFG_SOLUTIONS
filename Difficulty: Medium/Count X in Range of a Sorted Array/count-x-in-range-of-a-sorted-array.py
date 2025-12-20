class Solution:
    def countXInRange(self, arr, queries):
        # code here
        from bisect import bisect_left, bisect_right
        answers = []
        for l, r, x in queries:
            i = bisect_left(arr, x, lo=l, hi=r + 1)
            if i <= r and arr[i] == x:
                answers.append(bisect_right(arr, x, lo=i + 1, hi=r + 1) - i)
            else:
                answers.append(0)
        return answers