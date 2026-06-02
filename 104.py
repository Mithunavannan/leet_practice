root = [3,9,20,None,None,15,7]

def maxDepth(root):
    
    if root is None:
        return 0
    left_maxDepth = maxDepth(root.left)
    right_maxDepth = maxDepth(root.right)
    return max(left_maxDepth, right_maxDepth) + 1