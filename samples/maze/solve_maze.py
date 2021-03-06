import sys

def find_start(maze):
    for r, row in enumerate(maze):
        for c, v in enumerate(row):
            if v == 'S':
                return r, c
    return None


def find_goal(m):
    for x, row in enumerate(m):
        for y, v in enumerate(row):
            if v == 'G':
                return x, y
    return None


def move(x, y, s, maze):
    if maze[x][y] == '*':
        return
    if maze[x][y] == 'G':
        return
    if maze[x][y] == ' ':
        maze[x][y] = s+1
        solve_maze(x, y, s+1, maze)


def solve_maze(x, y, s, maze):
    move(x+1, y, s, maze)
    move(x-1, y, s, maze)
    move(x, y+1, s, maze)
    move(x, y-1, s, maze)


def draw_move(x, y, s, maze):
    if not isinstance(maze[x][y], int):
        return
    if s == 0 or maze[x][y] == s-1:
        s = maze[x][y]
        maze[x][y] = '+'
        draw_path(x, y, s, maze)


def draw_path(x, y, s, maze):
    draw_move(x+1, y, s, maze)
    draw_move(x-1, y, s, maze)
    draw_move(x, y+1, s, maze)
    draw_move(x, y-1, s, maze)


def erase_numbers(maze):
    for x, row in enumerate(maze):
        for y in range(len(row)):
            if isinstance(maze[x][y], int):
                maze[x][y] = ' '


def show_maze_debug(maze):
    for row in maze:
        print(",".join([str(s) for s in row]))


def show_maze(maze):
    for row in maze:
        print("".join(row))


def read_maze(filename):
    maze = []
    with open(filename) as f:
        for line in f:
            maze.append(list(line.strip()))
    sr, sc = find_start(maze)
    solve_maze(sr, sc, 0, maze)
    gr, gc = find_goal(maze)
    draw_path(gr, gc, 0, maze)
    erase_numbers(maze)
    show_maze(maze)

if len(sys.argv) == 1:
    print("usage: python solve_maze.py inputfile")
else:
    read_maze(sys.argv[1])
