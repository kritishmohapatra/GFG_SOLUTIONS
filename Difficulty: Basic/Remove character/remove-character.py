#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        s=""
        for i in str1:
            if i not in str2:
                s+=i
        return s
        