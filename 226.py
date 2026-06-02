root = [4,2,7,1,3,6,9]

def invertTree(root):
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)