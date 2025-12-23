#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        org=n
        result=0
        while(org!=0):
            remainder=org%10
            result+=remainder**3
            org=org//10
        if result==n:
            return True
        else:
            return False