class Solution:
    def divby13(self, s):
        # code here 
        rem=0
        for c in s:
            rem=(10*rem+(int(c)))%13
        return rem==0