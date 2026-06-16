#User function Template for python3
class Solution:
	def removeVowels(self, s):
		# code here
		a=""
		for i in s:
		    if i not in "aeiou":
		        a+=i
		return a
		
		