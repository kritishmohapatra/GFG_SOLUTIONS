class Solution:
	def minJumps(self, arr):
	    # code here
	    n=len(arr)
	    if arr[0]==0:
	        return -1
	    maxi=0
	    curr=0
	    j=0
	    for i in range(n):
	        maxi=max(maxi, i+arr[i])
	        if maxi>=n-1:
	            return j+1
	        if i==curr:
	            if i==maxi:
	                return -1
	            else:
	                j+=1
	                curr=maxi 
	    return -1
	    