class Solution:
    def sortByLength(self, arr):
       # code here
       arr.sort(key=len)
       