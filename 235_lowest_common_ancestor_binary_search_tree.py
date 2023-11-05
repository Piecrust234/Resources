# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# note: this solution relies on the fact that BSTs have smaller nodes to left, and larger to right.


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root: # start your loop (root is replaced as the next node we are checking against)
            if (p.val < root.val) and (q.val < root.val): # if both the input values are smaller than the current node, check the left.
                root = root.left
            elif (p.val > root.val) and (q.val > root.val): # OTHERWISE if both are greater than current, check the right.
                root = root.right
            else: # If one of the nodes is smaller and one is larger, you have your Lowest Common Ancestor
                return root
        