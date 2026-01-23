import sys


def main():
    print("=== Command Quest ===\n")
    try:
        print(f"Argument 1: {sys.argv[1]}")
        print(f"Argument 2: {sys.argv[2]}")
        print(f"Argument 3: {sys.argv[3]}")
        try:
            print(f"Program Name: {sys.argv[0]}")
            print(f"Arguments received {len(sys.argv)}")        

            print(f"Total Arguments {len(sys.argv)}")
        except IndexError:
            print("No arguments provided!")
    except IndexError:
        print("No arguments provided!")
         


if __name__ == "__main__":
    main()
