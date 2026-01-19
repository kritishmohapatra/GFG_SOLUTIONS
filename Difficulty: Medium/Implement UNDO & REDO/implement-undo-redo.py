class Solution:
    def __init__(self):
        self.doc=[]
        self.redos=[]
        
    def append(self, x):
        # append x into document
        self.doc.append(x)
        self.redos.clear()
        
        

    def undo(self):
        # undo last change
        if self.doc:
            self.redos.append(self.doc.pop())

    def redo(self):
        
        # redo changes
        if self.redos:
            self.doc.append(self.redos.pop())

    def read(self):
        # read the document
        return "".join(self.doc)