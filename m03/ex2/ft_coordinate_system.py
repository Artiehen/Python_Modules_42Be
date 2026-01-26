import sys
import math


class GeneralError(Exception):
    pass


def coordinate_system():
    try:
        error_occured = False
        if len(sys.argv) == 2:
            xyz0 = "0, 0, 0"
            xyz1 = sys.argv[1]
            splitpos1 = xyz1.split(",")
            splitpos0 = xyz0.split(",")
            numbers1 = tuple(int(p) for p in splitpos0)
            numbers2 = tuple(int(p) for p in splitpos1)
            x01, y01, z01 = numbers2

            pos0 = tuple(float(v) for v in splitpos0)
            pos1 = tuple(float(v) for v in splitpos1)
            x0, y0, z0 = pos0
            x1, y1, z1 = pos1
            dist = math.sqrt((x1 - x0) ** 2 +
                             (y1 - y0) ** 2 +
                             (z1 - z0) ** 2)
            print(f'Parsing coordinates: "{sys.argv[1]}"')
            print(f"Distance between {numbers1} and {numbers2}: {dist:.2f}")
        else:
            error_occured = True
            raise IndexError
    except ValueError as e:
        error_occured = True
        print(f'Parsing invalid coordinates: "{sys.argv[1]}"')
        print(f"Error parsing coordinate: {e}")
        print(f'Error details - Type: ValueError, Args:("{e}")')
    except IndexError:
        print("Too many arguments")
    finally:
        if error_occured is False:
            print("Unpacking demonstration")
            print(f"Player at x={x01}, y={y01}, z={z01}")
            print(f"Coordinates: X={x01}, Y={y01}, Z={z01}")


def main():
    print("=== Game Coordinate System ===\n")
    try:
        coordinate_system()
    except GeneralError:
        print("teswt")


if __name__ == "__main__":
    main()
