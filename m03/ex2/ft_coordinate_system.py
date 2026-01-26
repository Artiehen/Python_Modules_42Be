import math


class GeneralError(Exception):
    pass


def distance_calculator(pos0, pos1):
    x0, y0, z0 = pos0
    x1, y1, z1 = pos1
    dist = math.sqrt((x1 - x0) ** 2 +
                     (y1 - y0) ** 2 +
                     (z1 - z0) ** 2)
    return dist


def coordinate_system():
    try:
        xyz0 = "0, 0, 0"
        xyz1 = "3,4,0"
        xyz2 = (10, 20, 5)
        xyz3 = "abc,def,ghi"

        splitpos0 = xyz0.split(",")
        splitpos1 = xyz1.split(",")
        splitpos3 = xyz3.split(",")

        numbers1 = tuple(int(p) for p in splitpos0)
        numbers2 = tuple(int(p) for p in splitpos1)
        x01, y01, z01 = numbers2

        pos0 = tuple(float(v) for v in splitpos0)
        pos1 = tuple(float(v) for v in splitpos1)
        pos2 = tuple(float(v) for v in xyz2)

        dist0 = distance_calculator(pos0, pos1)
        dist1 = distance_calculator(pos0, pos2)
        print(f"Position created: {xyz2}")
        print(f"Distance between {numbers1} and {xyz2}: {dist1:.2f}\n")

        print(f'Parsing coordinates: "{xyz1}"')
        print(f"Parsed position: {numbers2}")
        print(f"Distance between {numbers1} and {numbers2}: {dist0}\n")
        numbers3 = tuple(int(p) for p in splitpos3)
        int(numbers3)
    except ValueError as e:
        print(f'Parsing invalid coordinates: "{xyz3}"')
        print(f"Error parsing coordinate: {e}")
        print(f'Error details - Type: ValueError, Args:("{e}",)')
    except IndexError:
        print("Too many arguments")
    finally:
        print("\nUnpacking demonstration\n")
        print(f"Player at x={x01}, y={y01}, z={z01}")
        print(f"Coordinates: X={x01}, Y={y01}, Z={z01}")


def main():
    print("=== Game Coordinate System ===\n")
    try:
        coordinate_system()
    except GeneralError:
        print("\n")


if __name__ == "__main__":
    main()
