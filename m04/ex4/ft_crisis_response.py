def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'")
        with open("lost_archive.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        print("CRISIS ALERT: Attempting access to 'classified_vault.txt'")
        with open("classified_vault.txt", "r") as file:
            print(file.read())
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    try:
        print("CRISIS ALERT: Attempting access to 'standard_archive.txt")
        with open("standard_archive.txt", "r") as file:
            print(f"SUCCESS: Archive recovered -``{file.read()}''")
            print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    finally:
        print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
