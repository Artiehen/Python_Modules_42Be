import os


def main():
    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(e)
    try:
        load_dotenv('.env.example')
    except FileNotFoundError as e:
        print(e)
    print("\nORACLE STATUS: Reading the Matrix...\n")
    keys = ['MATRIX_MODE', 'DATABASE_URL', 'API_KEY', 'LOG_LEVEL',
            'ZION_ENDPOINT']
    for info in keys:
        res = os.getenv(info)
        if res is None:
            print(f"Could not get the environment key for {info}.")
            print("Please check environment variables")
            exit(1)
    print("Configuration loaded:")


if __name__ == "__main__":
    main()
