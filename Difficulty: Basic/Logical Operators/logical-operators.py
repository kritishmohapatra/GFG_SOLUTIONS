class Solution:
    def boolean_operations(self, a: bool, b: bool) -> str:
        #code here
        return str(a and b).lower()+" "+str(a or b).lower()+" "+str(not a).lower()
        