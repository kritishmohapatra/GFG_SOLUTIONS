class Solution:
    def isBinaryPalindrome(self, n):
        # code here
        s=bin(n).replace("0b", "")
        return s==s[::-1]