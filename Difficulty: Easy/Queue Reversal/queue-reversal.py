class Solution:
    def reverseQueue(self, q):
        # code here
        if not q:
            return q
        
        # pop front element
        front = q.popleft()
        
        # recursive call on remaining queue
        self.reverseQueue(q)
        
        # push popped element at the rear
        q.append(front)
        
        return q