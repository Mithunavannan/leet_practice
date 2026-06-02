def finCircleNum(self, isConnected):
    if not isConnected:
        return 0
    visited = set()
    count = 0

    def dfs(isConnected, visited, i):
        visited.add(i)
        for j in range(len(isConnected)):
            if isConnected[i][j] == 1 and j not in visited:
                dfs(isConnected, visited, j)
    for i in range(len(isConnected)):
        if i not in visited:
            dfs(isConnected, visited, i)
            count += 1
    return count
