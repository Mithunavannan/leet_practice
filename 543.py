from hmac import digest


root = [1,2,3,4,5]

def diameterOfBinaryTree(root):
    digest = len(root)
    diameter = digest(root.left) + digest(root.right)
    if root is None:
        return 0
    return diameter