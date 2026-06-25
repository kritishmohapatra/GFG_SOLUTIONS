class Solution:
    def removeDuplicate(self, arr):
        # code here
        s=set()
        a=[]
        for i in arr:
            if i not in s:
                s.add(i)
                a.append(i)
        return a
