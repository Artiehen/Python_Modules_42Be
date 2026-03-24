from typing import Optional
import sys


class InvalidConfiguration(Exception):
    pass


class Configuration:
    width = 0
    height = 0
    value_entry = (0, 0)
    value_exit = (1, 1)
    output_file = "maze.txt"
    perfect = True
    seed = None


def read_configuration(filepath: str) -> Configuration:
    try:
        with open(filepath, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(
            f"[ERROR] Configuration file not found: '{filepath}'"
        )
    except IOError as e:
        raise IOError(f"[ERROR] Cannot read file '{filepath}': {e}")
    except MemoryError as e:
        raise f"Error: {e}"

    config = Configuration()
    found_keys = set()
    required_keys = {"WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"}

    for line_number, line in enumerate(lines, start=1):
        line = line.strip()

        if line.startswith("#"):
            continue

        if not line:
            raise ValueError(
                f"[ERROR] Line {line_number} is an empty line"
            )

        if "=" not in line:
            raise ValueError(
                f"[ERROR] Line {line_number} is invalid (missing '='): '{line}'"
            )

        key, _, value = line.partition("=")
        if value.startswith("="):
            raise ValueError(f"[ERROR] Line {line_number} too many '=' after {key}")

        try:
            duplicate_error_msg = f"Error at line {line_number}, duplicate key '{key}'"
            if key == "WIDTH":
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                config.width = parse_positive_integer(value, "WIDTH")
                found_keys.add("WIDTH")

            elif key == "HEIGHT":
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                config.height = parse_positive_integer(value, "HEIGHT")
                found_keys.add("HEIGHT")

            elif key == "ENTRY":
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                config.value_entry = parse_coordinate(value, "ENTRY")
                found_keys.add("ENTRY")

            elif key == "EXIT":
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                config.value_exit = parse_coordinate(value, "EXIT")
                found_keys.add("EXIT")

            elif key == "OUTPUT_FILE":
                if not value:
                    raise ValueError("OUTPUT_FILE cannot be empty.")
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                for character in value:
                    if not (character.isalnum() or character in ['_', '-', '.']):
                        raise ValueError(f"OUTPUT_FILE name cannot contain the character: '{character}'")
                config.output_file = value
                found_keys.add("OUTPUT_FILE")

            elif key == "PERFECT":
                if key in found_keys:
                    raise ValueError(duplicate_error_msg)
                config.perfect = parse_boolean(value, "PERFECT")
                found_keys.add("PERFECT")

            elif key == "SEED":
                config.seed = int(value)
            # (IMPORTANT) do we want to add more keys like "ALGORITHM", "DISPLAY MODE",...?
            else:
                raise ValueError(f"[ERROR] Unknown key at line {line_number}: '{key}'")

        except ValueError as e:
            raise ValueError(f"[ERROR] Line {line_number} — {e}")

    missing_keys = required_keys - found_keys
    if missing_keys:
        raise ValueError(
            f"[ERROR] Missing required keys in configuration file: "
            f"{', '.join(sorted(missing_keys))}"
        )
    validate_configuration(config)
    return config


def parse_positive_integer(value: str, key_name: str) -> int:
    try:
        # what to do with +9?
        for digit in value:
            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise ValueError
        n = int(value)
    except ValueError:
        raise ValueError(f"{key_name} must be an integer without space or other characters. Received: '{value}'")
    if n <= 0:
        raise ValueError(f"{key_name} must be greater than zero, received: {n}")
    return n


def parse_coordinate(value: str, key_name: str) -> tuple:
    parts = value.split(",")
    if len(parts) != 2:
        raise ValueError(
            f"{key_name} must be in the format 'x,y', received: '{value}'"
        )
    # what to do with +9?
    for part in parts:
        for digit in part:
            if digit not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                raise ValueError(
                    f"{key_name}: coordinates must be two digits from '0' to '9', "
                    f"separated by a comma, with no spaces. Received: '{value}'"
                )
    try:
        x = int(parts[0])
        y = int(parts[1])
    except ValueError:
        raise ValueError(
            f"{key_name}: coordinates must be integers, received: '{value}'"
        )
    if x < 0 or y < 0:
        raise ValueError(
            f"{key_name}: coordinates cannot be negative, received: ({x}, {y})"
        )
    return (x, y)


def parse_boolean(value: str, key_name: str) -> bool:
    if value == "True":
        return True
    elif value == "False":
        return False
    else:
        raise ValueError(
            f"{key_name} must be 'True' or 'False', received: '{value}'"
        )


def validate_configuration(config: Configuration) -> bool:
    entry_x, entry_y = config.value_entry
    exit_x, exit_y = config.value_exit
    if config.width < 2 or config.height < 2:
        raise ValueError(
            f"[ERROR] The maze must be at least 2x2. "
            f"Received: {config.width}x{config.height}"
        )
    if entry_x >= config.width or entry_y >= config.height:
        raise ValueError(
            f"[ERROR] ENTRY ({entry_x},{entry_y}) is outside the maze boundaries "
            f"({config.width}x{config.height})."
        )
    if exit_x >= config.width or exit_y >= config.height:
        raise ValueError(
            f"[ERROR] EXIT ({exit_x},{exit_y}) is outside the maze boundaries "
            f"({config.width}x{config.height})."
        )
    if config.value_entry == config.value_exit:
        raise ValueError(
            f"[ERROR] ENTRY and EXIT cannot be the same: both are ({entry_x},{entry_y})."
        )



def main():
    # KeyboardInterrupt (how can I measure it?)
    default_config = "default_config.txt"

    try:
        if len(sys.argv) != 2:
            raise InvalidConfiguration("[COMMAND ERROR] Usage: python3 a_maze_ing.py config.txt")
    except InvalidConfiguration as e:
        print(f"Error: {e}")
        config = read_configuration(default_config)
        print("\nStarting DEMO demonstration")
        print("Data ready for the maze generator")
        print(
            config.width,
            config.height,
            config.value_entry,
            config.value_exit,
            config.output_file,
            config.perfect,
            config.seed
        )
        sys.exit(1)

    try:
        config_file = sys.argv[1]
        config = read_configuration(config_file)
        print("Data ready for the maze generator")
        print(
            config.width,
            config.height,
            config.value_entry,
            config.value_exit,
            config.output_file,
            config.perfect,
            config.seed
        )
    except Exception as e:
        print(f"Error: {e}")
        config = read_configuration(default_config)
        print("\nStarting DEMO demonstration")
        print("Data ready for the maze generator")
        print(
            config.width,
            config.height,
            config.value_entry,
            config.value_exit,
            config.output_file,
            config.perfect,
            config.seed
        )
        sys.exit(1)

if __name__ == "__main__":
    main()

