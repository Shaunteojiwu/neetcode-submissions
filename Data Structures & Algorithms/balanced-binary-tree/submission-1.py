# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        def dfs(node):
            # Base case: an empty tree has a height of 0
            if not node:
                return 0
            
            # Get the height of the left subtree
            left_height = dfs(node.left)
            if left_height == -1: 
                return -1
            
            # Get the height of the right subtree
            right_height = dfs(node.right)
            if right_height == -1: 
                return -1
            
            # If the difference in heights is strictly greater than 1, it's unbalanced
            if abs(left_height - right_height) > 1:
                return -1
                
            # If balanced, return the actual height of this subtree
            return 1 + max(left_height, right_height)
        
        # The tree is balanced if the dfs does not return our -1 error code
        return dfs(root) != -1