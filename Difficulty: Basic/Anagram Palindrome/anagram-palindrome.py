class Solution:
    def canFormPalindrome(self, s):
        # code here
        k=set()
        for i in s:
            if i in k:
                k.remove(i)
            else:
                k.add(i)
        if len(k)<=1:
            return 1
        else:
            return 0
                