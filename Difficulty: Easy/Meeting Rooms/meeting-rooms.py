class Solution:
    def canAttend(self, arr):
        # Code Here
        arr.sort(key=lambda e:(e[0], e[1]))
        e=0
        for start, end in arr:
            if start<e:
                return False
            e=max(e, end)
        return True
        