class Solution:
    def minTime(self, ranks, n):
        # code here
        
        def ok(mid):
            nonlocal ranks,n
            remain=n
            for r in ranks:
                time=0
                duration=0
                while 1:
                    duration+=r
                    time+=duration
                    if time>mid:
                        break
                    remain-=1
                    if remain<=0:
                        return True
            return False
        left=1
        mxrank=max(ranks)
        right=(2*mxrank+(n-1)*mxrank)*n//2+1
        while left<right:
            mid=left+(right-left)//2
            if ok(mid):
                right=mid
            else:
                left=mid+1
        return left