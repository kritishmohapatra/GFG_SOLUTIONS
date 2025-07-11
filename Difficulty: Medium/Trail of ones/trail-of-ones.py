class Solution:
    def countConsec(self, n: int) -> int:
        # code here 
        if n==2:
            return 1
        prev=0
        curr=1
        nxt=0
        ans=1
        for i in range(3, n+1):
            nxt=prev+curr
            ans=ans*2+nxt
            prev=curr
            curr=nxt
        return ans
        
        
        