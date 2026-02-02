import sys


def main() -> None:
    """This function takes input and prints arguments and program names"""
    print("=== Command Quest ===")
    no_arg = False
    try:
        i = 1
        if len(sys.argv) > 1:
            print(f"Program name: {sys.argv[0]}")
            print(f"Arguments received: {len(sys.argv) - 1}")
            for arg in sys.argv[1:]:
                print(f"Argument {i}: {arg}")
                i += 1
        elif len(sys.argv) == 1:
            no_arg = True
            raise IndexError("No arguments Provided!")

    except IndexError as e:
        print(f"{e}")
    finally:
        if no_arg is True:
            print(f"Program name: {sys.argv[0]}")
            print(f"Arguments received: {len(sys.argv)}")
        else:
            print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
