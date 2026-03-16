class Solution:
    def rotateArr(self, arr, d):
        #Your code here
        d%=len(arr)
        arr[:d]=reversed(arr[:d])
        arr[d:]=reversed(arr[d:])
        arr[:]=arr[::-1]