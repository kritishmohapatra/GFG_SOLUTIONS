# Node class
class Node:

    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# Queue class template
class myQueue:

    def __init__(self):
        # Initialize your data members
        self.s=None
        self.e=None
        self.sz=0
        

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.s==None
        

    def enqueue(self, x):
        # Add element x to the rear
        ele=Node(x)
        if self.isEmpty():
            self.s=self.e=ele
        else:
            self.e.next=ele
            self.e=ele
        self.sz+=1
        

    def dequeue(self):
        # Remove the front element
        if self.isEmpty():
            return -1
  
        temp=self.s
        self.s=self.s.next
        if self.s==None:
            self.e=None
        self.sz-=1
        


    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.isEmpty():
            return -1
        return self.s.data
        


    def size(self):
        # Return current size
        return self.sz
