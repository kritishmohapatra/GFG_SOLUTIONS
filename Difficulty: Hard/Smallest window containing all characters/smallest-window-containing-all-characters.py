class Solution:
    def smallestWindow(self, s, p):
        # code here
        if len(s)<len(p):
            return ""
        forp=[0]*26
        fors=[0]*26
        start=-1
        end=-1
        length=99999999
        c=0
        c2=0
        j=0
        for i in range(0, len(p)):
            forp[ord(p[i])-ord("a")]+=1
            if forp[ord(p[i])-ord("a")]==1:
                c+=1
        for i in range(0, len(s)):
            fors[ord(s[i])-ord("a")]+=1
            if fors[ord(s[i])-ord("a")]==forp[ord(s[i])-ord("a")]:
                c2+=1
            if c2==c:
                while fors[ord(s[j])-ord("a")]>forp[ord(s[j])-ord("a")]:
                    fors[ord(s[j])-ord("a")]-=1
                    j+=1
                if length>i-j+1:
                    start=j
                    end=i
                    length=i-j+1
        if start==-1:
            return ""
        else:
            return s[start:start + length]