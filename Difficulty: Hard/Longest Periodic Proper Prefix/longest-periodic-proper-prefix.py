class Solution:
    def getLongestPrefix(self, s):
        # code here
        n = len(s)

        for k in range(n - 1, 0, -1):
            valid = True
            for i in range(k, n):
                if s[i] != s[i % k]:
                    valid = False
                    break
            if valid:
                return k
    
        return -1

        
