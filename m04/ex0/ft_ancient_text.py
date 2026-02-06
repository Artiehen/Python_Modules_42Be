
def main() -> None:
    try:
        f = open("ancient_fragment.txt", "r")
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        print("Accessing Storage Vault:", f.name)
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(f.read())
        f.close()
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    main()
