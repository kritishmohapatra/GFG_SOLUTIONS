class Solution:
    def catchThieves(self, arr, k):
        #code  here
        p=0
        t=0
        while (p<len(arr) and arr[p]!="P"):
            p+=1
        while (t<len(arr) and arr[t]!="T"):
            t+=1
        c=0
        while p<len(arr) and t<len(arr):
            if abs(p-t)<=k:
                c+=1
                p+=1
                t+=1
            elif p<len(arr) and p<t:
                p+=1
            elif t<len(arr) and t<p:
                t+=1
            while (p<len(arr) and arr[p]!="P"):
                p+=1
            while (t<len(arr) and arr[t]!="T"):
                t+=1
        return c
            

