import os


def write_maze(file_path: str, maze: list, entry: tuple[int, int],
               exit_: tuple[int, int], path: str) -> None:
    """Writes the Output_file using one hexadecimal digit per cell and
    the closest path to the solution.

    Keyword arguments:
    file_path -- Shortest path between entry/exit
    maze -- maze information
    entry -- Starting point in the maze
    exit -- Exit point in the maze
    """
    protected_files = {"a_maze_ing.py", "config.txt"}

    # Prevent overwriting protected files
    if os.path.basename(file_path) in protected_files:
        raise FileExistsError(f"File already exists: {file_path}")

    with open(file_path, "w") as f:
        for row in maze:
            f.write("".join(f"{cell:X}" for cell in row) + "\n")

        f.write("\n")
        f.write(f"{entry}\n")
        f.write(f"{exit_}\n")
        f.write(f"{path}\n")
