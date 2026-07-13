class Solution:
    def find(self, arr):
        # code here
        need = 0
    
        # Process the array from right to left
        for i in range(len(arr) - 1, -1, -1):
            # Minimum value required before processing arr[i]
            need = (need + arr[i] + 1) // 2
        return need