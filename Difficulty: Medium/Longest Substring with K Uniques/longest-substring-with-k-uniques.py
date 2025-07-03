class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n = len(s)
        i = 0
        j = 0
        cnt = 0
        maxi = -1
        fre = [0] * 26
        
        # cnt represents the number of
        # unique characters in the current window
    
        while j < n:
    
            # include s[j] into the window
            fre[ord(s[j]) - ord('a')] += 1
    
            # it is the first occurrence of 
            # this character in the window
            if fre[ord(s[j]) - ord('a')] == 1:
                cnt += 1
    
            # shrink the window if the number of
            # unique character is more than k
            while cnt > k:
                fre[ord(s[i]) - ord('a')] -= 1
    
                # one unique character removed
                if fre[ord(s[i]) - ord('a')] == 0:
                    cnt -= 1
                i += 1
    
            # we have exactly k unique characters
            if cnt == k:
                maxi = max(maxi, j - i + 1)
    
            j += 1
    
        return maxi
        
        