class Solution():
    def longestString(self, words):
        # code here
        words.sort(key=len)
        ans = ""
        s = set([""])
        for e in words:
            if e[:-1] in s:
                if len(e) > len(ans) or len(e) == len(ans) and e < ans:
                    ans = e
                s.add(e)
        return ans
        
        