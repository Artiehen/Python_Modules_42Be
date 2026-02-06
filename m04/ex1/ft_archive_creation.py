def main() -> None:
    try:
        f = open("new_discovery.txt", "w")
        nl0 = "[ENTRY 001] New quantum algorithm discovered"
        nl1 = "\n[ENTRY 002] Efficiency increased by 347%"
        nl2 = "\n[ENTRY 003] Archived by Data Archivist trainee"
        print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
        print("Initializing new storage unit:", f.name)
        print("Storage unit created successfully...\n")
        print("Inscribing preservation data...")
        f.write(nl0)
        print(nl0, end="")
        f.write(nl1)
        print(nl1, end="")
        f.write(nl2)
        print(nl2, end="")
        print()
        f.close()
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive '{f.name}' ready for long-term preservation.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found")


if __name__ == "__main__":
    main()
