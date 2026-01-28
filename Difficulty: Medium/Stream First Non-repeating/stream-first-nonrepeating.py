class Solution:
	def firstNonRepeating(self, s):
		# code here
		n = len(s)
        freq = [0] * 26
        firstPos = [-1] * 26
        
        # record first occurrence for each character
        for i in range(n):
            if firstPos[ord(s[i]) - ord('a')] == -1:
                firstPos[ord(s[i]) - ord('a')] = i
    
        result = ""
        for i in range(n):
            freq[ord(s[i]) - ord('a')] += 1
    
            chosen = '#'
            earliest = n + 1
    
            # find earliest character with frequency 1
            for j in range(26):
                if freq[j] == 1 and earliest > firstPos[j]:
                    chosen = chr(j + ord('a'))
                    earliest = firstPos[j]
            result += chosen
    
        return result