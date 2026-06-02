def updateMatrix(self, mat):
    if not self.mat:
        return self.mat
    rows, cols = len(self.mat), len(self.mat[0])
    queue = []
    for i in range(rows):
        for j in range(cols):
            if self.mat[i][j] == 0:
                queue.append((i, j))
            else:
                self.mat[i][j] = float('inf')
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and self.mat[new_x][new_y] > self.mat[x][y] + 1:
                self.mat[new_x][new_y] = self.mat[x][y] + 1
                queue.append((new_x, new_y))
    return self.mat
