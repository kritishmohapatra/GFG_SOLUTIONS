class Solution:
    def minDaysBloom(self, bloomDay, K, M):
        # Code here
        def calci(bloomDay, M, K, value):
            cnt=0
            day=0
            for i in bloomDay:
                if i<=value:
                    cnt+=1
                else:
                    day+=cnt//K
                    cnt=0
            day+=cnt//K
            return day>=M
        if len(bloomDay)<(M*K):
            return -1
        low=min(bloomDay)
        high=max(bloomDay)
        ans=high
        while(low<=high):
            mid=(low+high)//2
            if calci(bloomDay, M,K, mid):
                ans=min(ans, mid)
                high=mid-1
            else:
                low=mid+1
        return ans
        