from collections import deque

class SpecialQueue:
    def __init__(self):
        self.q = deque()
        self.minq = deque()
        self.maxq = deque()

    def enqueue(self, x):
        self.q.append(x)
        while self.minq and self.minq[-1] > x:
            self.minq.pop()
        self.minq.append(x)
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)

    def dequeue(self):
        val = self.q.popleft()
        if val == self.minq[0]:
            self.minq.popleft()
        if val == self.maxq[0]:
            self.maxq.popleft()

    def getFront(self):
        return self.q[0]

    def getMin(self):
        return self.minq[0]

    def getMax(self):
        return self.maxq[0]
