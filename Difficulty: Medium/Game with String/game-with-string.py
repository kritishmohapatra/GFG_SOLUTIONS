class Solution:
    def minValue(self, s, k):
        #code here
        arr = [0] * 26
        for c in s:
            arr[ord(c) - ord("a")] += 1
        
        maxi = max(arr)
        mp = {}
        for freq in arr:
            if freq > 0:
                mp[freq] = mp.get(freq, 0) + 1
        
        while k > 0 and maxi > 0:
            rem = min(k, mp[maxi])
            mp[maxi] -= rem
            mp[maxi - 1] = mp.get(maxi - 1, 0) + rem
            if mp[maxi] == 0:
                del mp[maxi]
                maxi -= 1
            k -= rem
        
        result = 0
        for freq, count in mp.items():
            result += (freq ** 2) * count
        
        return result