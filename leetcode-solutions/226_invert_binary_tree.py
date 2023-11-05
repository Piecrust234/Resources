# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def invertTree(self, root: [TreeNode]) -> [TreeNode]:
        
        def invert(node): # Recursive function to swap the nodes.
            if node is not None: #check if the input node is None

                # make placeholders for the current left and right
                left = node.left 
                right = node.right

                # swap left and right of the current node using the placeholders
                node.left = right
                node.right = left    
                
                # call the function recursively twice, for each side of the node
                invert(left)
                invert(right)
                
        # initial function call
        invert(root)

        # return the inverted rootnode
        return root
        
        
        
