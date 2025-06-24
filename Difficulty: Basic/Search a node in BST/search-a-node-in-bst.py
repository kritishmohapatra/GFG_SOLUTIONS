#Your task is to complete this function

class BST:
    
    #Function to search a node in BST.
    def search(self, node, x):
        #code here
        while node is not None and node.data!=x:
            node=node.left if x<node.data else node.right
        return node