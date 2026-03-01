import random


class MazeGenerator:
    def __init__(self, width, height, seed, entry, exit, output_file, perfect) -> None:
        self.width = width
        self.height = height
        self.seed = seed
        self.entry = entry
        self.exit = exit
        self.output_file = output_file
        self.perfect = perfect
        self.xy_positions = []
