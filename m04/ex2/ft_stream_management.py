import sys


def main() -> None:
    """This is the main function testing all communication
    channels input, sys.stdout and sys.stderr"""
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    id = input("Input Stream activce. Enter archivist ID:")
    status_report = input("Input Stream active. Enter status report:")
    sys.stdout.write("\n[STANDARD] Archive status from ")
    sys.stdout.write(f"{id}: {status_report}\n")
    sys.stderr.write("[ALERT] System diagnostic: ")
    sys.stderr.write("Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    sys.stdout.write("\nThree-channel communication test successful.\n")


if __name__ == "__main__":
    main()
