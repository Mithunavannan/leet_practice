root = [1,2,3,null,5,null,4]

def rightSideView(root):
    if not root:
        return []
    rightside = []
    for level in root:
        rightside.append(level[-1])
    return rightside