class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        left = 0
        right = 0
        count = 0
        freq_map = {}

        while right < len(arr):
            
            freq_map[arr[right]] = freq_map.get(arr[right], 0) + 1

        
            while len(freq_map) > k:
                freq_map[arr[left]] -= 1
                if freq_map[arr[left]] == 0:
                    del freq_map[arr[left]]
                left += 1

            count += right - left + 1
            right += 1

        return count
        