class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	s=set()
        for i in arr:
            s.add(i*i)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if ((arr[i]*arr[i])+(arr[j]*arr[j])) in s:
                    return True
        return False