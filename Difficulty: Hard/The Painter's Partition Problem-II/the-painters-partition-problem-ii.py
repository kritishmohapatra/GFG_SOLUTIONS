class Solution:
    def minTime (self, arr, k):
        # code here
        def check_time(time: int) -> bool:
            curr_time = 0
            painters = 1
            for a in arr:
                curr_time += a
                if curr_time > time:
                    if painters == k:
                        return False
                    painters += 1
                    curr_time = a
            return True
        
        lo, hi = max(arr), sum(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if check_time(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo