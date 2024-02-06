# created by me

import colorama as c

size = 10

maze = [
    ['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' '],
    [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    [' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    [' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#'],
    [' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#'],
    [' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    [' ', '#', 'F', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    [' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#']
]

maze2 = [
    ['S', '#', '#', ' ', 'F'],
    [' ', ' ', '#', '#', ' '],
    ['#', ' ', ' ', '#', ' '],
    ['#', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ']
]


def input_maze():
    global maze, size
    print("Hello! It's maze solver. I can solve square mazes and find optimal ways from start to finish.")
    print(f"""There are symbols that I use and understand:

1. {c.Fore.RED + "#" + c.Fore.RESET} (barrier)
2. {c.Fore.YELLOW + "S" + c.Fore.RESET} (start)
3. {c.Fore.YELLOW + "F" + c.Fore.RESET} (finish)
4. {c.Fore.GREEN + "@" + c.Fore.RESET} (part of path from start to finish, don't use while entering your maze)
    """)
    guess = input("Do you want me to solve your maze or my default? (enter 1 or 2): ")
    if guess[0] == "1":
        maze.clear()
        print()

        size = int(input("How many strings/columns will be in your maze? "))
        print("\nEnter symbols in every string, but don't separate them (you can write '.' instead of spaces). Example: S##.#F \n")
        for string in range(size):
            print(f"{string+1}.", end=' ')
            new_str = [i if i != '.' else ' ' for i in input()]
            maze.append(new_str)


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
            elif sym == "@":
                print(c.Fore.GREEN + sym, end=' ')
                continue
            print(c.Fore.RESET + sym, end=' ')
        print(c.Fore.RESET + "|")
    print(c.Fore.RESET + "_ " * (size+2))


def main():
    input_maze()

    print(c.Fore.CYAN + "Initial maze: ")
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
        new_node = q[len(q)-1]

        q.pop()

        for ch in range(len(graph[new_node[0]][new_node[1]])):
            new_child = graph[new_node[0]][new_node[1]][ch]
            if not used[new_child[0]][new_child[1]]:
                used[new_child[0]][new_child[1]] = True
                q.append(new_child)
                dists[new_child[0]][new_child[1]] = dists[new_node[0]][new_node[1]] + 1
                parents[new_child[0]][new_child[1]] = new_node

    if not used[target[0]][target[1]]:
        print(used)
        print("It's impossible to solve this maze!")
        return

    print()
    print(c.Fore.CYAN + "Minimal length of path from start to finish for this maze:", c.Fore.LIGHTMAGENTA_EX + str(dists[target[0]][target[1]]),
          c.Fore.RESET)

    path = list()
    v = target
    while v != -1:
        path.append(v)
        v = parents[v[0]][v[1]]

    path.reverse()

    for elm in path:
        maze[elm[0]][elm[1]] = "@"

    print()
    print(c.Fore.LIGHTMAGENTA_EX + "The way from start to finish: ")
    print_maze()


if __name__ == "__main__":
    main()
