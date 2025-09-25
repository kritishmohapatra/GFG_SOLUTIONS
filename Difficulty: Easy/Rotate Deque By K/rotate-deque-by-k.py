from collections import deque
class Solution:    
    def rotateDeque(self, dq, type, k):
        #code here
        if type==2:
            for _ in range(k):
                e=dq.popleft()
                dq.append(e)
        else:
            for _ in range(k):
                e=dq.pop()
                dq.appendleft(e)
        