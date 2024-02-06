# created by me

import colorama as c

size = 5
maze = [
    ['S', '#', '#', ' ', 'F'],
    [' ', ' ', '#', '#', ' '],
    ['#', ' ', ' ', '#', ' '],
    ['#', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ']
]


def print_maze():
    print(c.Fore.RESET + "_ " * (size+2))
    print()
    for string in maze:
        print(c.Fore.RESET + "|", end=' ')
        for sym in string:
            if sym == "#":
                print(c.Fore.RED + sym, end=' ')
                continue
            elif sym in ["S", "F"]:
                print(c.Fore.YELLOW + sym, end=' ')
                continue
            print(c.Fore.RESET + sym, end=' ')
        print(c.Fore.RESET + "|")
    print(c.Fore.RESET + "_ " * (size+2))


def main():
    print_maze()

    start, target = 0, 0
    graph = [[[] for _ in range(size)] for _ in range(size)]
    used, dists, parents, q = ([[False for _ in range(size)] for _ in range(size)], [[0 for _ in range(size)] for _ in range(size)],
                               [[-1 for _ in range(size)] for _ in range(size)], [])

    for string in range(size):
        for sym in range(size):
            if maze[string][sym] != "#":
                if maze[string][sym] == "S":
                    start = [string, sym]
                elif maze[string][sym] == "F":
                    target = [string, sym]

                for possible_pos in [[string, sym-1], [string, sym+1], [string-1, sym], [string+1, sym]]:
                    if 0 <= possible_pos[0] < size and 0 <= possible_pos[1] < size and maze[possible_pos[0]][possible_pos[1]] != "#":
                        graph[string][sym].append(possible_pos)

    q.append(start)
    used[start[0]][start[1]] = True

    while len(q) > 0:
        new_node = q[-1]
        q.pop(0)

        for ch in range(len(graph[new_node[0]][new_node[1]])):
            new_child = graph[new_node[0]][new_node[1]][ch]
            if not used[new_child[0]][new_child[1]]:
                used[new_child[0]][new_child[1]] = True
                q.append(new_child)
                dists[new_child[0]][new_child[1]] = dists[new_node[0]][new_node[1]] + 1
                parents[new_child[0]][new_child[1]] = new_node

    if not used[target[0]][target[1]]:
        print("It's impossible to solve this maze!")
        return

    print(dists[target[0]][target[1]])


if __name__ == "__main__":
    main()
