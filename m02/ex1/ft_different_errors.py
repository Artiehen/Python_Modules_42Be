def garden_operations():
    """ This function will test 4 error handling operations individually"""
    try:
        print("\nTesting ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    try:
        print("\nTesting ZeroDivisionError ...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    try:
        print("\nTesting FileNotFoundError...")
        open("test.txt", "r")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")

    try:
        print("\nKeyError example:")
        garden = {"roses": 5, "tulips": 3}
        print(garden["sunflowers"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")

    print("\nGarden operations completed!\n")


def test_error_types():
    """This function will test 2 error at the same time"""
    print("=== Garden Error Types Demo ===")
    garden_operations()
    print("Testing multiple errors together...")

    try:
        int("abc")
        10 / 0

    except (ValueError, ZeroDivisionError):
        print("Caught multiple error, but program continues!\n")
        print("All error types tested successfully!")


# test_error_types()
