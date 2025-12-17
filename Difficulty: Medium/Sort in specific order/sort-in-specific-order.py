class Solution:
    def sortIt(self, arr):
        # code here
        n=len(arr)
        left=0
        
        for i in range(n):
            if arr[i]%2==1:
                arr[left], arr[i]=arr[i],arr[left]
                left+=1
        arr[:left]=sorted(arr[:left], reverse=True)
        arr[left:]=sorted(arr[left:])
       
    
