import sys
from maze import Maze
from config_parser import parse_config
from display import MazeDisplay


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py config.txt")
        sys.exit(1)

    config = parse_config(sys.argv[1])

    maze = Maze(config)
    maze.generate()
    maze.save()

    display = MazeDisplay(maze)
    display.run()


if __name__ == "__main__":
    main()