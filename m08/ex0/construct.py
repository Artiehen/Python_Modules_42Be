import sys


def is_matrix():
    if hasattr(sys, 'real_prefix'):
        return True
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def instructions_in_matrix():
    pythonv = f"{sys.version_info.major}.{sys.version_info.minor}"
    print("MATRIX STATUS: Welcome to the construct")
    print(f"\nCurrent Python: Python {pythonv}.{sys.version_info.micro}")


def instructions_of_matrix():
    pythonv = f"{sys.version_info.major}.{sys.version_info.minor}"
    print("Not running virtual Environment")
    print(f"\nCurrent Python: Python {pythonv}.{sys.version_info.micro}")
    print("Virtual Environment: None")
    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("to enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate # On Windows")
    print("\nThen run this program again.")


def main():

    if is_matrix():
        instructions_in_matrix()
    else:
        instructions_of_matrix()


if __name__ == "__main__":
    main()
