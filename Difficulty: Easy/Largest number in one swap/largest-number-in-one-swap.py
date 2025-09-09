class Solution:
    def largestSwap(self, s):
        #code here
        arr=list(s)
        maxid="0"
        maxind, l, r=-1, -1, -1
        for i in range(len(arr)-1, -1, -1):
            if arr[i]>maxid:
                maxid=arr[i]
                maxind=i
            elif arr[i]<maxid:
                l,r=i,maxind
        if l==-1:
            return s
        arr[l], arr[r]=arr[r], arr[l]
        return "".join(arr)
        