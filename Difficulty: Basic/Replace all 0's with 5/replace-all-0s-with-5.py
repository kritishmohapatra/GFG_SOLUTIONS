# Function should return an integer value
class Solution:
    def convertFive(self, n):
        # Code here
        s=int(str(n).replace("0", "5"))
        return s