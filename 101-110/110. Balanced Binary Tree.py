# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(root):
            if not root:
                return 0
            # nonlocal res
            
            left = dfs(root.left)
            right = dfs(root.right)

            diff = abs(left - right)
            if diff > 1:
                res = False

            return 1 + max(left, right)
        
        dfs(root)

        return res