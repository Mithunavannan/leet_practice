root = [3,9,20,None,None,15,7]

def averageOfLevels(root):
    if not root:
        return []
    for level in root:
        average = sum(level) / len(level)
    return average
    