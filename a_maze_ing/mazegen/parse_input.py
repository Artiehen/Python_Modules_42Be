

class InvalidConfiguration(Exception):
    pass


class Configuration:
    def __init__(self) -> None:
        self.width = 0
        self.height = 0
        self.value_entry = (0, 0)
        self.value_exit = (1, 1)
        self.output_file = "maze.txt"
        self.perfect = True
        self.seed: int | None = None

    def read_configuration(self, filepath: str) -> None:
        try:
            with open(filepath, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(
                f"[ERROR] selfuration file not found: '{filepath}'"
            )
        except IOError as e:
            raise IOError(f"[ERROR] Cannot read file '{filepath}': {e}")
        except MemoryError as e:
            raise MemoryError(f"Error: {e}")

        found_keys: set[str] = set()
        required_keys: set[str] = {"WIDTH", "HEIGHT", "ENTRY",
                                   "EXIT", "OUTPUT_FILE", "PERFECT"}

        # lnbr -> line number
        for lnbr, line in enumerate(lines, start=1):
            line = line.strip()

            if line.startswith("#"):
                continue

            if not line:
                raise ValueError(
                    f"[ERROR] Line {lnbr} is an empty line"
                )

            if "=" not in line:
                raise ValueError(
                    f"[ERROR] Line {lnbr} is "
                    f"invalid (missing '='): '{line}'"
                )

            key, _, value = line.partition("=")
            if value.startswith("="):
                raise ValueError(f"[ERROR] Line {lnbr} "
                                 f"too many '=' after {key}")

            try:
                dup_err_msg = f"Error at line {lnbr}, duplicate key '{key}'"
                if key == "WIDTH":
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    self.width = self.parse_positive_integer(value, "WIDTH")
                    found_keys.add("WIDTH")

                elif key == "HEIGHT":
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    self.height = self.parse_positive_integer(value, "HEIGHT")
                    found_keys.add("HEIGHT")

                elif key == "ENTRY":
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    self.value_entry = self.parse_coordinate(value, "ENTRY")
                    found_keys.add("ENTRY")

                elif key == "EXIT":
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    self.value_exit = self.parse_coordinate(value, "EXIT")
                    found_keys.add("EXIT")

                elif key == "OUTPUT_FILE":
                    if not value:
                        raise ValueError("OUTPUT_FILE cannot be empty.")
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    for character in value:
                        if not (character.isalnum() or
                                character in ['_', '-', '.']):
                            raise ValueError(
                                "OUTPUT_FILE name cannot contain "
                                f"the character: '{character}'"
                                )
                    self.output_file = value
                    found_keys.add("OUTPUT_FILE")

                elif key == "PERFECT":
                    if key in found_keys:
                        raise ValueError(dup_err_msg)
                    self.perfect = self.parse_boolean(value, "PERFECT")
                    found_keys.add("PERFECT")

                elif key == "SEED":
                    self.seed = int(value)
                # (IMPORTANT) do we want to add more keys like
                # "ALGORITHM", "DISPLAY MODE",...?
                else:
                    raise ValueError(
                        "[ERROR] Unknown key "
                        f"at line {lnbr}: '{key}'"
                        )

            except ValueError as e:
                raise ValueError(f"[ERROR] Line {lnbr} — {e}")

        missing_keys = required_keys - found_keys
        if missing_keys:
            raise ValueError(
                f"[ERROR] Missing required keys in selfuration file: "
                f"{', '.join(sorted(missing_keys))}"
            )

        self.validate_configuration()

    def parse_positive_integer(self, value: str, key_name: str) -> int:
        try:
            # what to do with +9?
            for digit in value:
                if digit not in ["0", "1", "2", "3", "4",
                                 "5", "6", "7", "8", "9"]:
                    raise ValueError
            n = int(value)
        except ValueError:
            raise ValueError(f"{key_name} must be an integer without "
                             f"space or other characters. Received: '{value}'")
        if n <= 0:
            raise ValueError(f"{key_name} must be greater "
                             f"than zero, received: {n}")
        return n

    def parse_coordinate(self, value: str, key_name: str) -> tuple[int, int]:
        parts = value.split(",")
        if len(parts) != 2:
            raise ValueError(
                f"{key_name} must be in the format 'x,y', received: '{value}'"
            )
        # what to do with +9?
        for part in parts:
            for digit in part:
                if digit not in ["0", "1", "2", "3", "4",
                                 "5", "6", "7", "8", "9"]:
                    raise ValueError(
                        f"{key_name}: coordinates must be "
                        "two digits from '0' to '9', "
                        f"separated by a comma, with no spaces. "
                        f"Received: '{value}'"
                    )
        try:
            x = int(parts[0])
            y = int(parts[1])
        except ValueError:
            raise ValueError(
                f"{key_name}: coordinates must be integers, "
                f"received: '{value}'"
            )
        if x < 0 or y < 0:
            raise ValueError(
                f"{key_name}: coordinates cannot be negative, "
                f"received: ({x}, {y})"
            )
        return (x, y)

    def parse_boolean(self, value: str, key_name: str) -> bool:
        if value == "True":
            return True
        elif value == "False":
            return False
        else:
            raise ValueError(
                f"{key_name} must be 'True' or 'False', received: '{value}'"
            )

    def validate_configuration(self) -> None:
        entry_x, entry_y = self.value_entry
        exit_x, exit_y = self.value_exit
        if not (4 <= self.width <= 30) or not (4 <= self.height <= 30):
            raise ValueError(
                f"[ERROR] The maze size must be between 7 and 30. "
                f"Received: {self.width}x{self.height}"
            )
        if entry_x >= self.width or entry_y >= self.height:
            raise ValueError(
                f"[ERROR] ENTRY ({entry_x},{entry_y}) is outside "
                "the maze boundaries "
                f"({self.width}x{self.height})."
            )
        if exit_x >= self.width or exit_y >= self.height:
            raise ValueError(
                f"[ERROR] EXIT ({exit_x},{exit_y}) is outside "
                "the maze boundaries "
                f"({self.width}x{self.height})."
            )
        if self.value_entry == self.value_exit:
            raise ValueError(
                f"[ERROR] ENTRY and EXIT cannot be the same:"
                f" both are ({entry_x},{entry_y})."
            )
