class Solution:
    def lcmTriplets(self, n):
        #code here
        if n<3:
            return n
        if n%2!=0:
            return n*(n-1)*(n-2)
        if n%3!=0:
            return n*(n-1)*(n-3)
        return (n-1)*(n-2)*(n-3)