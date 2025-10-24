def findPath(maze, n):
    res = []
    dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

    def dfs(x, y, path):
        if x == n - 1 and y == n - 1:
            res.append(path)
            return
        maze[x][y] = 0

        for dx, dy, move in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 1:
                dfs(nx, ny, path + move)

        maze[x][y] = 1

    if maze[0][0] == 1:
        dfs(0, 0, "")

    return sorted(res) if res else ["-1"]
