# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)

            rob_current = node.val + left[1] + right[1]
            skip_current = (max(left) + max(right))

            return (rob_current, skip_current)
        return max(dfs(root))