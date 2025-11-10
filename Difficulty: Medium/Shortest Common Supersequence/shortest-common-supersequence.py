class Solution:
    def minSuperSeq(self, s1, s2):
        # code here
        m, n = len(s1), len(s2)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
    
        for i in range(1, m + 1):
            for j in range(1, n + 1):
    
                # If chars match
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = 1 + prev[j - 1]
    
                # Else, take max from top or left
                else:
                    curr[j] = max(prev[j], curr[j - 1])
    
            # Move current row to previous
            prev = curr[:]
    
        lcsLen = prev[n]
    
        # SCS length = total - common part (LCS)
        return m + n - lcsLen