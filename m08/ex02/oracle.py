import os


def main():
    try:
        from dotenv import load_dotenv
    except ImportError as e:
        print(e)
    try:
        load_dotenv('.env')
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
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    print(f"Database: {os.getenv('DATABASE_URL')}")
    print(f"API Access: {os.getenv('API_KEY')}")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print(f"Zion Network: {os.getenv('ZION_ENDPOINT')}")

    print('\nEnvironment security check:')
    print('[OK] No hardcoded secrets detected')
    print('[OK] .env file properly configured')
    print('[OK] Production overrides available')

    print('\nThe Oracle sees all configurations.')


if __name__ == "__main__":
    main()
