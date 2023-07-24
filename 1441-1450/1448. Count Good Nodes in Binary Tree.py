# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, curMax):
            nonlocal res
            if not root:
                return None
            if root.val >= curMax:
                res += 1
                curMax = max(curMax, root.val)
            dfs(root.left, curMax)
            dfs(root.right, curMax)

        dfs(root, root.val)
        
        return res
