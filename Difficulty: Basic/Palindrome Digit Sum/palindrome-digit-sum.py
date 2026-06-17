#User function Template for python3


class Solution:
    def isDigitSumPalindrome(self, n):
        #code here
        su=0
        rev=0
        while(n!=0):
            remainder=n%10
            su+=remainder
            n=n//10
        org=su
        while(su!=0):
            re=su%10
            rev=rev*10+re
            su=su//10
        if(rev==org):
            return 1
        else:
            return 0