class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n=len(prices)
        mini=0
        i, end=0, n-1
        while i<=end:
            mini+=prices[i]
            i+=1
            
            end-=k
        maxi=0
        i, start=n-1, 0
        while i>=start:
            maxi+=prices[i]
            i-=1
            
            start+=k 
        return [mini, maxi]
        