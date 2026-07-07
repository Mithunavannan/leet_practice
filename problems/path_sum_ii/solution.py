# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, currentSum, path):
            if not node:
                return
            currentSum += node.val
            path.append(node.val)

            if not node.left and not node.right:
                if currentSum == targetSum:
                    result.append(path[:])
            dfs(node.left, currentSum, path)
            dfs(node.right, currentSum, path)

            path.pop()
        dfs(root, 0, [])
        return result