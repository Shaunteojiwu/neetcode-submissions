class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0

            left=dfs(node.left)
            if left is False:
                return False
            right=dfs(node.right)
            if right is False:
                return False

            if abs(left-right)>1:
                return False

            return 1+max(left,right)

        return dfs(root) is not False