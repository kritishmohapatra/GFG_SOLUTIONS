class Solution:
    def findSum(self, s):
        #code here
        n=0
        su=0
        for i in s:
            if i.isdigit():
                n=n*10+int(i)
            else:
                su+=n
                n=0
        return su+n
