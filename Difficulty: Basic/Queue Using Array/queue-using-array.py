class myQueue:
    def __init__(self, n):
        # Define Data Structures
        self.q=[0]*n
        self.c=0
        self.s=-1
        self.e=-1
    
    def isEmpty(self):
        # Check if queue is empty
        return self.s==-1

    
    def isFull(self):
        # Check if queue is full
        return self.c==len(self.q)

    
    def enqueue(self, x):
        # Enqueue
        if self.isFull():
            return -1
        if self.c==0:
            self.s=0
            self.e=0
        else:
            self.e=(self.e+1)%len(self.q)
        self.q[self.e]=x
        self.c+=1
            
        

    
    def dequeue(self):
        # Dequeue
        if self.c==0:
            return -1
        p=self.q[self.s]
        if self.c==1:
            self.s=self.e=-1
        else:
            self.s=(self.s+1)%len(self.q)
        self.c-=1
        return p
            

    
    def getFront(self):
        # Get front element
        if self.c!=0:
            return self.q[self.s]
        return -1
       
    
    def getRear(self):
        # Get rear element 
        if self.c!=0:
            return self.q[self.e]
        return -1
        
        