import sys
from typing import Any
from mazegen.writer import write_maze

RESET = "\033[0m"
EMPTY = "  "

# ---------------------------
# Color Themes
# Each theme: (wall, entry, exit, path/solution)
# Using ANSI background colors for wall, foreground for cells
# ---------------------------
THEMES = [
    {
        # "name":  "Classic",
        "wall":  "\033[43m  \033[0m",   # yellow background
        "entry": "\033[32m██\033[0m",   # green
        "exit":  "\033[31m██\033[0m",   # red
        "path":  "\033[34m██\033[0m",   # blue
        "logo":  "\033[47m  \033[0m",   # white background
    },
    {
        # "name":  "Night",
        "wall":  "\033[46m  \033[0m",   # cyan background
        "entry": "\033[35m██\033[0m",   # magenta
        "exit":  "\033[31m██\033[0m",   # red
        "path":  "\033[32m██\033[0m",   # green
        "logo":  "\033[47m  \033[0m",
    },
    {
        # "name":  "Sunset",
        "wall":  "\033[41m  \033[0m",   # red background
        "entry": "\033[33m██\033[0m",   # yellow
        "exit":  "\033[35m██\033[0m",   # magenta
        "path":  "\033[36m██\033[0m",   # cyan
        "logo":  "\033[47m  \033[0m",
    },
    {
        # "name":  "Forest",
        "wall":  "\033[42m  \033[0m",   # green background
        "entry": "\033[36m██\033[0m",   # cyan
        "exit":  "\033[33m██\033[0m",   # yellow
        "path":  "\033[35m██\033[0m",   # magenta
        "logo":  "\033[47m  \033[0m",
    },
]

# Active theme index (module-level state)
theme_index: int = 0


def theme() -> dict:
    return THEMES[theme_index % len(THEMES)]


def get_path_cells(entry: tuple[int, int], path: str) -> set[tuple[int, int]]:
    x, y = entry
    cells = [(x, y)]
    moves = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    for step in path:
        dx, dy = moves[step]
        x += dx
        y += dy
        cells.append((x, y))
    return set(cells)


def render_maze_base(maze: Any) -> list[list[str]]:
    t = theme()
    canvas = []

    for y in range(maze.height):
        row_top = []
        row_mid = []

        for x in range(maze.width):
            # --- Top walls ---
            top_wall = t["wall"] if maze.grid[y][x] & 1 else EMPTY
            row_top.append(t["wall"] + top_wall)

            # --- Left wall ---
            left_wall = t["wall"] if maze.grid[y][x] & 8 else EMPTY

            # --- Cell content ---
            if (x, y) == maze.value_entry:
                cell = t["entry"]
            elif (x, y) == maze.value_exit:
                cell = t["exit"]
            elif (x, y) in maze.logo:
                cell = t["logo"]
            else:
                cell = EMPTY

            row_mid.append(left_wall + cell)

        row_top.append(t["wall"])
        row_mid.append(t["wall"] if maze.grid[y][-1] & 2 else EMPTY)

        canvas.append(row_top)
        canvas.append(row_mid)

    bottom = []
    for x in range(maze.width):
        bottom_wall = t["wall"] if maze.grid[-1][x] & 4 else EMPTY
        bottom.append(t["wall"] + bottom_wall)
    bottom.append(t["wall"])
    canvas.append(bottom)

    return canvas


def overlay_path(canvas: list[list[str]], maze: Any,
                 path_cells: set[tuple[int, int]]) -> list[list[str]]:
    t = theme()
    path_block = t["path"]

    for (x, y) in path_cells:
        canvas_y = y * 2 + 1
        canvas_x = x
        # Is preventing from writing the firs path of the block to the left
        # if (x, y) == maze.value_entry or
        # (x, y) == maze.value_exit or (x, y) in maze.logo:
        #    continue
        if (x, y) in maze.logo:
            continue

        if (x, y) == maze.value_exit:
            has_left_wall = maze.grid[y][x] & 8
            if (x - 1, y) in path_cells and not has_left_wall:
                canvas[canvas_y][canvas_x] = path_block + t["exit"]
            continue

        has_left_wall = maze.grid[y][x] & 8

        # Horizontal connection
        if (x - 1, y) in path_cells and not has_left_wall:
            left_wall = path_block
        else:
            left_wall = t["wall"] if has_left_wall else EMPTY
        # Prevents missing blocks to the left
        if (x, y) == maze.value_entry:
            canvas[canvas_y][canvas_x] = left_wall + t["entry"]
        else:
            canvas[canvas_y][canvas_x] = left_wall + path_block

        # Vertical connection
        if (x, y - 1) in path_cells and not (maze.grid[y][x] & 1):
            canvas[canvas_y - 1][canvas_x] = t["wall"] + path_block
        if (x, y + 1) in path_cells and not (maze.grid[y][x] & 4):
            canvas[canvas_y + 1][canvas_x] = t["wall"] + path_block
    return canvas


def print_canvas(canvas: list[list[str]]) -> None:
    for row in canvas:
        print("".join(row))


def display_maze(maze: Any, solution: bool) -> None:
    print("\033[3J\033[2J\033[H", end="")  # cancella cronologia
    print("\033[2J\033[H", end="")  # pulisce tutto lo schermo iniziale

    if not maze.logo:
        print(
                "[INFO] Maze too small for pattern ‘42’.\n"
                "The height and width must be greater than 10.\n"
                "Pattern omitted."
                )
    canvas = render_maze_base(maze)

    if solution is True:
        path_cells = get_path_cells(maze.value_entry, maze.solution)
        canvas = overlay_path(canvas, maze, path_cells)

    print_canvas(canvas)


def get_user_choice() -> int:
    while True:
        try:
            choice = int(input("Choice? (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("[ERROR] Please enter a number between 1 and 4.")
        except ValueError:
            print("[ERROR] Invalid input. Please enter a number.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)


def run_interface(maze: Any) -> None:
    # global _theme_index -> unused variables, ask marco about it
    show_solution = False

    while True:
        theme()  # controlla perche mai usata
        print(
            "\n=== A-Maze-ing === \n"
            "1. Re-generate a new maze\n"
            "2. Show/hide path from entry to EXIT\n"
            "3. Rotate maze colors\n"
            "4. Quit"
        )

        choice = get_user_choice()

        if choice == 1:
            write_maze(maze.output_file, maze.grid, maze.value_entry,
                       maze.value_exit, maze.solution)
            maze.generate_maze()
            display_maze(maze, show_solution)
        elif choice == 2:
            show_solution = not show_solution
            display_maze(maze, show_solution)
        elif choice == 3:
            global theme_index
            theme_index = (theme_index + 1) % len(THEMES)
            display_maze(maze, show_solution)
        elif choice == 4:
            print("Goodbye!")
            break
