class Solution:
    def findMajority(self, arr):
        # code here
        c1=0
        c2=0
        ele1=float("-inf")
        ele2=float("-inf")
        for i in range(len(arr)):
            if c1==0 and ele2!=arr[i]:
                c1=1
                ele1=arr[i]
            elif c2==0 and ele1!=arr[i]:
                c2=1
                ele2=arr[i]
            elif arr[i]==ele1:
                c1+=1
            elif arr[i]==ele2:
                c2+=1
            else:
                c1-=1
                c2-=1
        ans=[]
        c, p=0,0
        for i in range(len(arr)):
            if ele1==arr[i]:
                c+=1
            if ele2==arr[i]:
                p+=1    
        if c>(len(arr)//3):
            ans.append(ele1)
        if p>len(arr)//3:
            ans.append(ele2)
        
        ans.sort()
        return ans