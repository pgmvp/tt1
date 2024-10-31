def solve():
    m, n = map(int, input().split())

    a = []
    for i in range(m):
        row = list(map(int, input().split()))
        a.append(row)

    visited = [[False] * n for _ in range(m)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    def good(x, y):
        return 0 <= x < m and 0 <= y < n and not visited[x][y] and a[x][y] == 1

    def dfs(x, y):
        visited[x][y] = True
        for i in range(4):
            nex, ney = x + dx[i], y + dy[i]
            if good(nex, ney):
                dfs(nex, ney)

    comp = 0
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and a[i][j] == 1:
                dfs(i, j)
                comp += 1

    print(comp)


if __name__ == "__main__":
    solve()