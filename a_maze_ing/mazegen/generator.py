from collections import deque
import random
import sys
from typing import Optional


class MazeGenerator:
    def __init__(self, width: int, height: int, value_entry: tuple[int, int],
                 value_exit: tuple[int, int], output_file: str,
                 perfect: bool, seed: Optional[int]) -> None:
        self.width = width
        self.height = height
        self.value_entry = value_entry
        self.value_exit = value_exit
        self.output_file = output_file
        self.perfect = perfect
        self.seed = seed
        self.grid: list[list[int]] = []
        self.logo: set[tuple[int, int]] = set()
        self.solution: str = ""

        if seed is not None:
            random.seed(seed)

    def initialize_grid(self) -> None:
        """Initiates the grid for the maze.

        Keyword Argument:
        self -- Class information to store values
        """
        self.grid = [[15 for _ in range(self.width)]
                     for _ in range(self.height)]

    def remove_wall(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Performs bitwise operation to remove walls in the maze."""
        dx = x2 - x1
        dy = y2 - y1

        if dx == 1:  # East
            self.grid[y1][x1] &= ~2
            self.grid[y2][x2] &= ~8
        elif dx == -1:  # West
            self.grid[y1][x1] &= ~8
            self.grid[y2][x2] &= ~2
        elif dy == 1:  # South
            self.grid[y1][x1] &= ~4
            self.grid[y2][x2] &= ~1
        elif dy == -1:  # North
            self.grid[y1][x1] &= ~1
            self.grid[y2][x2] &= ~4

    def draw_logo(self) -> bool:
        """Determines if to write or not 42 logo"""
        if self.width < 10 or self.height < 10:
            self.logo = set()
            # print("[INFO] Maze too small for pattern ‘42’. Pattern omitted.")
            # ->creating empty spaces since it prints everytime the maze_gen
            # runs, message printed at the beginning
            # of execution and invisible to program -> ask marco
            return False

        x = (self.width // 2) - 3
        y = (self.height // 2) - 2

        number_four = [
            (x, y), (x, y + 1), (x, y + 2),
            (x + 1, y + 2),
            (x + 2, y + 2), (x + 2, y + 3), (x + 2, y + 4)
        ]

        number_two = [
            (x + 4, y), (x + 5, y), (x + 6, y),
            (x + 6, y + 1),
            (x + 4, y + 2), (x + 5, y + 2), (x + 6, y + 2),
            (x + 4, y + 3),
            (x + 4, y + 4), (x + 5, y + 4), (x + 6, y + 4)
        ]

        self.logo = set(number_four + number_two)

        if self.value_entry in self.logo or self.value_exit in self.logo:
            print("[ERROR] Entry/Exit cannot be on the '42' pattern.")
            sys.exit(1)
        return False

    def solve_maze(self) -> str:
        """Finds and writes shortest path to exit"""
        queue = deque([(self.value_entry, "")])
        visited = set([self.value_entry])

        moves = {
            "N": (0, -1, 1),
            "E": (1, 0, 2),
            "S": (0, 1, 4),
            "W": (-1, 0, 8)
        }

        while queue:
            (x, y), path = queue.popleft()

            if (x, y) == self.value_exit:
                return path

            for d, (dx, dy, wall) in moves.items():
                nx, ny = x + dx, y + dy

                if not (0 <= nx < self.width and 0 <= ny < self.height):
                    continue

                if self.grid[y][x] & wall:
                    continue

                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + d))

        return ""

    def generate_perfect_maze(self) -> None:
        """Uses DFS to generate a perfect maze."""
        self.initialize_grid()
        visited = set()

        self.draw_logo()
        if self.logo:
            visited.update(self.logo)

        def dfs(x: int, y: int) -> None:
            visited.add((x, y))

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) not in visited:
                        self.remove_wall(x, y, nx, ny)
                        dfs(nx, ny)

        dfs(0, 0)

    def creates_open_block(self) -> bool:
        """Prevents 3x3 or greater open areas."""
        for y in range(self.height - 2):
            for x in range(self.width - 2):
                open_block = True

                for dy in range(3):
                    for dx in range(3):
                        if self.grid[y + dy][x + dx] != 0:
                            open_block = False
                            break
                    if not open_block:
                        break

                if open_block:
                    return True

        return False

    def add_loops(self, probability: float = 0.08) -> None:
        """Breaks 'Tree' to create a non-perfect maze."""
        for y in range(self.height):
            for x in range(self.width):
                directions = [(0, 1), (1, 0)]

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if random.random() < probability:
                            if (x, y) in self.logo or (nx, ny) in self.logo:
                                continue

                            old1 = self.grid[y][x]
                            old2 = self.grid[ny][nx]

                            self.remove_wall(x, y, nx, ny)

                            if self.creates_open_block():
                                # rollback
                                self.grid[y][x] = old1
                                self.grid[ny][nx] = old2

    def generate_maze(self) -> None:
        """Instantiates maze and determines if perfect maze or break it."""
        self.generate_perfect_maze()

        if not self.perfect:
            self.add_loops()

        self.solution = self.solve_maze()
