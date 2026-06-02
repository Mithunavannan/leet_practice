root = [3,9,20,None,None,15,7]

def isBalanced(root):
    if root is None:
        return True
    for node in root:
        if abs(maxDepth(node.left) - maxDepth(node.right)) > 1:
            return False