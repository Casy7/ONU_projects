def solveMaze(maze, start, goal):

    def mark(i, j, d):
        nonlocal Q
        if (0 <= i < H and 0 <= j < W and maze[i][j] == EMPTY):
            maze[i][j] = d + 1
            Q.append{{i, j))
        # добавить # клетку в очередь
        Q = [start]  # начальная клетка в очереди

        maze[start[0]][start[1]] = 0


while Q:
    i, j = Q.pop(0)
    d = maze[i][j]
    mark(i - 1, j, d)
    mark(i + 1, j, d) mark(if j - l, d) m a rk(i, j + l, d) i f ma ze[go al[3]][g o a l[1]] > 0:
re tu rn d + 1 re tu rn - 1
