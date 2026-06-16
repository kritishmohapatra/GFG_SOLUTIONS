#User function Template for python3

class Solution:

    def Count(self, S):
        # code here
        c=0
        for i in S:
            if i.isalpha():
                c+=1
        return c
        