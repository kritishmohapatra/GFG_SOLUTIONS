#User function Template for python3

class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        num1=[]
        num2=[]
        for i in range(len(arr)):
            if i%2==0:
                num1.append(str(arr[i]))
            else:
                num2.append(str(arr[i]))
        num1="".join(num1).lstrip("0") or "0"
        num2="".join(num2).lstrip("0") or "0"
        res=[]
        carry=0
        i=len(num1)-1
        j=len(num2)-1
        while i>=0 or j>=0 or carry>0:
            s=carry
            if i>=0:
                s+=int(num1[i])
                i-=1
            if j>=0:
                s+=int(num2[j])
                j-=1
            res.append(str(s%10))
            carry=s//10
        return "".join(res[::-1])
            
        


