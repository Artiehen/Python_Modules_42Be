class MazeDisplay:
    def __init__(self, maze):
        self.maze = maze
        self.show_path = False
        self.wall_color = "\033[37m"

    def run(self):
        while True:
            self.draw()
            print("\nCommands: r=regenerate p=toggle path c=color q=quit")
            cmd = input(">> ").lower()

            if cmd == "r":
                self.maze.generate()
            elif cmd == "p":
                self.show_path = not self.show_path
            elif cmd == "c":
                self._change_color()
            elif cmd == "q":
                break

    def _change_color(self):
        colors = ["\033[31m", "\033[32m", "\033[34m", "\033[37m"]
        self.wall_color = colors[(colors.index(self.wall_color) + 1) % len(colors)]

    def draw(self):
        maze = self.maze
        grid = maze.grid

        print("\033c", end="")  # clear screen

        for y in range(maze.height):
            # top walls
            for x in range(maze.width):
                print(self.wall_color + "+", end="")
                if grid[y][x] & 1:
                    print("---", end="")
                else:
                    print("   ", end="")
            print("+")

            # side walls
            for x in range(maze.width):
                if grid[y][x] & 8:
                    print("|", end="")
                else:
                    print(" ", end="")

                if (x, y) == maze.entry:
                    print(" S ", end="")
                elif (x, y) == maze.exit:
                    print(" E ", end="")
                elif self.show_path and self._is_in_path(x, y):
                    print(" . ", end="")
                else:
                    print("   ", end="")
            print("|")

        print("+" + "---+" * maze.width)

    def _is_in_path(self, x, y):
        cx, cy = self.maze.entry
        path = self.maze.path

        for move in path:
            if (cx, cy) == (x, y):
                return True
            if move == "N":
                cy -= 1
            elif move == "S":
                cy += 1
            elif move == "E":
                cx += 1
            elif move == "W":
                cx -= 1

        return (cx, cy) == (x, y)
