# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        left=diameterofBinaryTree(root.left)
        right=diameterofBinaryTree(root.right)

        return 1+max(abs(left-right))
        