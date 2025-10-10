'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import deque

class Solution:
    def zigZagTraversal(self, root):
        result, left_to_right, queue = [root.data], True, deque([root])
        
        while queue:
            temp_queue, level_values = deque(), []
            
            for node in queue:
                if node.left:
                    temp_queue.append(node.left)
                    level_values.append(node.left.data)
                if node.right:
                    temp_queue.append(node.right)
                    level_values.append(node.right.data)
            
            result.extend(level_values[::-1] if left_to_right else level_values)
            queue, left_to_right = temp_queue, not left_to_right
        
        return result