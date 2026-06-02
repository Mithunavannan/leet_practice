root = [3,9,20,None,None,15,7]

def levelOrder(root):
    if root is None:
        return []
    result = []
    queue = [root]
    while queue:
        Level = []
        for i in range(len(queue)):
            node = queue.pop(0)
            Level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(Level)
    return result
    print(levelOrder(root))