class Solution:
    def removeChars(self, s: str) -> str:
        # code here
        a=""
        for i in s:
            if i.isalpha():
                a+=i
        return a