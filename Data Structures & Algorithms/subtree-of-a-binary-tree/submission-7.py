# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root,subRoot):
            return True

        return isSubtree(root.left,subroot) or isSubtree(root.right,subroot)

        def isSameTree(self,root,subroot):
            if not root and subroot:
                return True
            if not p or q:
                return False
            if root.val!=subroot.val:
               return False
            return isSameTree(root.left,subroot.left) and isSameTree(root.right,subroot.right)

        