class Solution:
    def mycmp(self, s1, s2):
        if s1+s2>s2+s1:
            return -1
        else:
            return 1
            

	   
    def findLargest(self, arr):
        # code here
        nums=[str(ele) for ele in arr]
        nums.sort(key=cmp_to_key(self.mycmp))
        if nums[0]=="0":
            return "0"
        return "".join(nums)