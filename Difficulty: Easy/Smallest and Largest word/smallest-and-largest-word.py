class Solution:
    def smallerAndLarge(self, s):
        # code here
        a=s.split()
        a.sort(key=lambda x: len(x))
        return (a[0], a[-1])
        