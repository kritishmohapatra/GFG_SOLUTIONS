class Solution:

    def __init__(self):
        # code here
        self.s=[]
        self.mini=float("inf")
        
    # Add an element to the top of Stack
    def push(self, x):
        # code here
        if len(self.s)==0:
            self.mini=x
            self.s.append(x)
        else:
            if x<self.mini:
                self.s.append(2*x-self.mini)
                self.mini=x
            else:
                self.s.append(x)
    # Remove the top element from the Stack
    def pop(self):
        # code here
        if len(self.s)==0:
            return -1
        else:
            val=self.s.pop()
            if val<self.mini:
                self.mini=2*self.mini-val

    # Returns top element of Stack
    def peek(self):
        if not self.s:
            return -1
        val=self.s[-1]
        if val<self.mini:
            return self.mini
        else:
            return val
        # code here

    # Finds minimum element of Stack
    def getMin(self):
        if not self.s:
            return -1
        return self.mini
        # code here



