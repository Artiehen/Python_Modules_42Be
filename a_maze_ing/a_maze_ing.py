# a_maze_ing.py
# import sys
# import os
# from typing import Any


def main() -> None:
    """
    Initialies the configuration and reads the config.txt file and
    writes the maze output_file
    """
    try:
        import sys
        from mazegen import MazeGenerator
        from mazegen import Configuration
        from mazegen import display_maze, run_interface
        from mazegen import write_maze

    except (ModuleNotFoundError, ImportError) as e:
        print("There missing modules"
              " please check Readme for additional instructions:"
              f"\n{e}")

    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        return

    try:
        config = Configuration()
        config.read_configuration(sys.argv[1])
    except Exception as e:
        print(e)
        sys.exit()

    maze = MazeGenerator(
        config.width,
        config.height,
        config.value_entry,
        config.value_exit,
        config.output_file,
        config.perfect,
        config.seed
    )

    maze.generate_maze()

    try:
        write_maze(maze.output_file, maze.grid, maze.value_entry,
                   maze.value_exit, maze.solution)
        display_maze(maze, False)
        run_interface(maze)
    except (FileNotFoundError, PermissionError,
            FileExistsError, IsADirectoryError) as e:
        print(f"There is a problem with the outputfile: {e}")


if __name__ == "__main__":
    main()
