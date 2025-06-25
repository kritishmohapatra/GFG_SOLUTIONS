class Solution:
    def sameFreq(self, s: str) -> bool:
        #code here
        arr=[0]*26
        for c in s:
            arr[ord(c)-ord("a")]+=1
        mp={}
        for char in arr:
            if char>0:
                mp[char]=mp.get(char, 0)+1
        if len(mp)==1:
            return True
        if len(mp)!=2:
            return False
        mp=list(mp.items())
        f1=mp[0][0]
        f2=mp[1][0]
        c1=mp[0][1]
        c2=mp[1][1]
        if f1==1 and c1==1:
            return True
        if f2==1 and c2==1:
            return True
        if (abs(f1-f2)==1) and ((f1>f2 and c1==1) or (f2>f1 and c2==1)):
            return True 
        return False