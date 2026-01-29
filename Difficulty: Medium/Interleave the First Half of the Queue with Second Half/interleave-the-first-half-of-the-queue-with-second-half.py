from collections import deque

class Solution:
    def rearrangeQueue(self, q):
        #code here 
        n = len(q)
    
        # copy elements to temporary array
        arr = list(q) 
        q.clear()     
    
        # Interleave elements back into the queue
        for i in range(n // 2):
            q.append(arr[i])         
            q.append(arr[i + n // 2])