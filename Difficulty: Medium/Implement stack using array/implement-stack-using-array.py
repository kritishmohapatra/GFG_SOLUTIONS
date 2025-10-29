class myStack:
    def __init__(self, n):
        # Define Data Structures
        self.st=[0]*n
        self.top=-1
    
    def isEmpty(self):
        # Check if stack is empty
        return self.top==-1

    
    def isFull(self):
        # Check if stack is full
        return self.top+1==len(self.st)

    
    def push(self, x):
        # Insert x at the top of the stack
        self.top+=1
        self.st[self.top]=x

    
    def pop(self):
        # Removes an element from the top of the stack
        if self.isEmpty():
            return None
        x=self.st[self.top]
        self.top-=1
        return x
    
    def peek(self):
        # Returns the top element of the stack
        if self.top!=-1:
            return self.st[self.top]
        else:
            return -1