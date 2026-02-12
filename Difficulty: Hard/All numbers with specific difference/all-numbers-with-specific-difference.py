class Solution:
    def getCount(self, n, d):
        # code here 
        l=1
        r=N
        while(l<=r):
           mid=(l+r)//2
           c=0
           while(mid>0):
               c+=mid%10
               mid = mid//10
           mid = (l+r)//2
           if(mid-c)<D:
               l=mid+1
           else:
               r=mid-1
        return N-r
        