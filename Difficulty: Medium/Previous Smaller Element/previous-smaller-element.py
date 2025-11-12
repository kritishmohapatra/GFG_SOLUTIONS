class Solution:
	def prevSmaller(self, arr):
		# code here
		n=len(arr)
		st=[]
		ans=[-1]*n
		for i in range(n):
		    while st and st[-1]>=arr[i]:
		        st.pop()
		    if st:
		        ans[i]=st[-1]
		    st.append(arr[i])
		return ans
		      