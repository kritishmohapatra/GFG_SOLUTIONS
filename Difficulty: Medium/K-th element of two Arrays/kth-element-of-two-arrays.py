class Solution:
    def kthElement(self, a, b, k):
        # code here
        arr3 = []
        m=len(a)
        n=len(b)
        i, j = 0, 0
        while i < m and j < n:
            if a[i] < b[j]:
                arr3.append(a[i])
                i += 1
            else:
                arr3.append(b[j])
                j += 1
            
        arr3.extend(a[i:])
        arr3.extend(b[j:])
        return arr3[k - 1]