class Solution:
    def removeSpaces(self, s):
        # code here
        st=""
        for i in s:
            if i!=" ":
                st+=i 
        return st