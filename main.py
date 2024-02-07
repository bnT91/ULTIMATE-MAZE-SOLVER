# created by me

import colorama as c

size = 10

template = [
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

maze = template

maze2 = [
    ['S', '#', '#', ' ', 'F'],
    [' ', ' ', '#', '#', ' '],
    ['#', ' ', ' ', '#', ' '],
    ['#', '#', ' ', '#', ' '],
    [' ', ' ', ' ', ' ', ' ']
]


def print_rules():
    print("Hello! It's maze solver. I can solve square mazes and find optimal ways from start to finish.")
    print(f"""There are symbols that I use and understand:

    1. {c.Fore.RED + "#" + c.Fore.RESET} (barrier)
    2. {c.Fore.YELLOW + "S" + c.Fore.RESET} (start)
    3. {c.Fore.YELLOW + "F" + c.Fore.RESET} (finish)
    4. {c.Fore.GREEN + "@" + c.Fore.RESET} (part of path from start to finish, don't use while entering your maze)

You can write your own mazes for me. There are two ways to do it: using keyboard or creating new file.

For coders: my main algorithm is modified BFS. That uses queue to process all the node points of graph.
        """)


def input_maze():
    global maze, size

    user_guess = input("Do you want me to solve your maze or my default? (enter 1 or 2): ")

    if user_guess[0] == "1":
        maze.clear()

        input_type = input("Do you want to type every line in maze using keyboard or create file with maze? (enter 1 or 2): ")

        if input_type[0] != "2":
            size = int(input("How many line/columns will be in your maze? "))
            print("Enter symbols in every line, but don't separate them (you can write '.' instead of spaces). Example: S##.#F \n")
            for string in range(size):
                print(f"{string+1}.", end=' ')
                new_str = [i if i != '.' else ' ' for i in input()]
                maze.append(new_str)
            return

        print("OK, now you need to create new file with the maze in the folder that called \"mazes\".\nFirst string of the file has to be a number of lines/columns in the maze. After it, "
              "type the maze in my format, \nseparating lines by ENTER. Then, tell me the name of your file. Enter it here: ", end="")
        filename = input()
        try:
            with open("mazes/" + filename, "r") as f:
                data = f.readlines()
                size = int(data[0].rstrip())
                for line in data[1:]:
                    line = line.rstrip()
                    new_str = [i if i != '.' else ' ' for i in line]
                    maze.append(new_str)
        except FileNotFoundError:
            print(f"I can't find {filename} in the \"mazes\" folder.")
    else:
        maze = [['S', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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
        size = 10


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

    if not maze:
        return

    print()

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
        new_node = q[0]
        q.pop(0)

        for ch in range(len(graph[new_node[0]][new_node[1]])):
            new_child = graph[new_node[0]][new_node[1]][ch]
            if not used[new_child[0]][new_child[1]]:
                q.append(new_child)
                if dists[new_node[0]][new_node[1]] + 1 < dists[new_child[0]][new_child[1]] or not used[new_child[0]][new_child[1]]:
                    dists[new_child[0]][new_child[1]] = dists[new_node[0]][new_node[1]] + 1
                    parents[new_child[0]][new_child[1]] = new_node
                used[new_child[0]][new_child[1]] = True

    if not used[target[0]][target[1]]:
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

    for elm in path[1:-1]:
        maze[elm[0]][elm[1]] = "@"

    print()
    print(c.Fore.LIGHTMAGENTA_EX + "The way from start to finish: ")
    print_maze()


if __name__ == "__main__":
    print_rules()
    main()
    guess = True
    while guess:
        print()
        new_launch = input("Would you like me to solve another maze? (type yes or no): ")
        if new_launch.lower()[0] == "n":
            guess = False
        else:
            print()
            main()

    input()
