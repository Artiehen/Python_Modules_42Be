def main() -> None:
    try:
        print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols\n")

        print("SECURE EXTRACTION")
        with open("classified_data.txt", "r") as file:
            print(file.read())
        print("\nSECURE PRESERVATION")
        with open("security_protocols.txt", "r") as file1:
            print(file1.read())

        print("\nVault automatically sealed upon completion")
        print("All vault operations completed with maximum security.")
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
