class Solution:
    def countSubarrays(self, arr):
        # code here
        st = []
        ans = 0
        n = len(arr)
    
        for i in range(n - 1, -1, -1):
            while (len(st) != 0 and arr[st[-1]] >= arr[i]):
                st.pop()
                
            # The index of next smaller element
            # starting from i'th index
            if (len(st) == 0):
                last = n
            else:
                last = st[-1]
    
            # Adding the number of subarray which
            # can be formed in the range [i, last]
            ans += (last - i)
            st.append(i)
    
        return ans