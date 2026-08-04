# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return None
        # if root:
        #     depth+=1
        if not root:
            return 0

        leftDepth=self.maxDepth(root.left)
        rightDepth=self.maxDepth(root.right)
            
        
        
       
        #  return   1+max(leftDepth,rightDepth)

        # leftDepth=maxDepth(root.left)
        # rightDepth=maxDepth(root.right)
            
        
    