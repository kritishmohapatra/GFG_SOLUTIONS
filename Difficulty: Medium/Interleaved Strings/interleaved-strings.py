class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
        i=0
        j=0
        n=len(s3)
        #print(n,"length of s3")
        #print(len(s1)+len(s2))
       
        
        mp={}
        for item in s3:
            if item not in mp:
                mp[item]=1
            else:
                mp[item]+=1
        
        if len(s1)+len(s2)!=len(s3):
            return False
        
        while(i<len(s1) and j<len(s3)):
            
            if s1[i]==s3[j] and mp[s1[i]]>0:
                mp[s1[i]]-=1
                i+=1
                j+=1
            else:
                j+=1
        if i<len(s1):
            return False
        #print(i)
        
        i=0
        j=0
        #print(trace)
        while(i<len(s2) and j<len(s3)):
            
            if s2[i]==s3[j] and mp[s2[i]]>0:
                mp[s2[i]]-=1
                i+=1
                j+=1
            else:
                j+=1
        #print(i,"second iteration")        
                
        if i==len(s2):
            return True
            
        
        return False