#Function to delete a node from BST.

def helper(root):
    if root.left==None:
        return root.right
    if root.right==None:
        return root.left
    rightchild=root.right
    lastright=findlastright(root.left)
    lastright.right=rightchild
    return root.left
def findlastright(root):
    if root.right==None:
        return root
    return findlastright(root.right)
def deleteNode(root, X):
    # code here.
    if root==None:
        return None
    if root.data==X:
        return helper(root)
    dummy=root
    while root!=None:
        if root.data>x:
            if root.left!=None and root.left.data==X:
                root.left=helper(root.left)
                break
            else:
                root=root.left
        else:
            if root.right!=None and root.right.data==X:
                root.right=helper(root.right)
                break
            else:
                root=root.right
    return dummy