import random
from collections import deque

N = 1
E = 2
S = 4
W = 8
ALL_WALLS = 15

DX = {N: 0, E: 1, S: 0, W: -1}
DY = {N: -1, E: 0, S: 1, W: 0}
OPPOSITE = {N: S, S: N, E: W, W: E}


class Maze:
    def __init__(self, config):
        self.width = int(config["WIDTH"])
        self.height = int(config["HEIGHT"])
        self.entry = tuple(map(int, config["ENTRY"].split(",")))
        self.exit = tuple(map(int, config["EXIT"].split(",")))
        self.output_file = config["OUTPUT_FILE"]
        self.perfect = config["PERFECT"].upper() == "T"
        self.seed = int(config.get("SEED", 0))

        random.seed(self.seed)

        self._validate()

        self.grid = [
            [ALL_WALLS for _ in range(self.width)]
            for _ in range(self.height)
        ]

    def _validate(self):
        ex, ey = self.entry
        xx, xy = self.exit

        if not (0 <= ex < self.width and 0 <= ey < self.height):
            raise ValueError("Entry out of bounds")

        if not (0 <= xx < self.width and 0 <= xy < self.height):
            raise ValueError("Exit out of bounds")

        if self.entry == self.exit:
            raise ValueError("Entry and Exit must differ")

    def generate(self):
        self._generate_perfect()

        if not self.perfect:
            self._add_extra_openings()

        self._embed_42()
        self._fix_large_open_areas()
        self.path = self._bfs_shortest_path()

    def _remove_wall(self, x, y, direction):
        nx = x + DX[direction]
        ny = y + DY[direction]

        self.grid[y][x] &= ~direction
        self.grid[ny][nx] &= ~OPPOSITE[direction]

    def _generate_perfect(self):
        visited = set()
        stack = [self.entry]
        visited.add(self.entry)

        while stack:
            x, y = stack[-1]
            neighbors = []

            for direction in [N, E, S, W]:
                nx = x + DX[direction]
                ny = y + DY[direction]

                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) not in visited:
                        neighbors.append((direction, nx, ny))

            if neighbors:
                direction, nx, ny = random.choice(neighbors)
                self._remove_wall(x, y, direction)
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

    def _add_extra_openings(self):
        attempts = (self.width * self.height) // 4

        for _ in range(attempts):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            direction = random.choice([N, E, S, W])
            nx = x + DX[direction]
            ny = y + DY[direction]

            if 0 <= nx < self.width and 0 <= ny < self.height:
                self._remove_wall(x, y, direction)

    def _embed_42(self):
        pattern = [
            "11110",
            "00010",
            "11110",
            "10000",
            "11111"
        ]

        start_x = self.width // 2 - 2
        start_y = self.height // 2 - 2

        for y in range(5):
            for x in range(5):
                if pattern[y][x] == "1":
                    gx = start_x + x
                    gy = start_y + y
                    if 0 <= gx < self.width and 0 <= gy < self.height:
                        if (gx, gy) not in (self.entry, self.exit):
                            self.grid[gy][gx] = ALL_WALLS

    def _fix_large_open_areas(self):
        for y in range(self.height - 2):
            for x in range(self.width - 2):
                if self._is_3x3_open(x, y):
                    self.grid[y + 1][x + 1] = ALL_WALLS

    def _is_3x3_open(self, x, y):
        for dy in range(3):
            for dx in range(3):
                if self.grid[y + dy][x + dx] != 0:
                    return False
        return True

    def _bfs_shortest_path(self):
        queue = deque([self.entry])
        visited = {self.entry}
        came_from = {}

        while queue:
            x, y = queue.popleft()

            if (x, y) == self.exit:
                break

            for direction in [N, E, S, W]:
                if not (self.grid[y][x] & direction):
                    nx = x + DX[direction]
                    ny = y + DY[direction]

                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        came_from[(nx, ny)] = (x, y, direction)
                        queue.append((nx, ny))

        path = []
        current = self.exit

        while current != self.entry:
            x, y, direction = came_from[current]
            path.append(direction)
            current = (x, y)

        path.reverse()

        mapping = {N: "N", E: "E", S: "S", W: "W"}
        return "".join(mapping[d] for d in path)

    def save(self):
        with open(self.output_file, "w") as f:
            for row in self.grid:
                f.write("".join(format(cell, "X") for cell in row) + "\n")

            f.write("\n")
            f.write(f"{self.entry[0]},{self.entry[1]}\n")
            f.write(f"{self.exit[0]},{self.exit[1]}\n")
            f.write(self.path + "\n")