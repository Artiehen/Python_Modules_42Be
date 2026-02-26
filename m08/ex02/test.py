#!/usr/bin/env python3

import os
import sys
import logging
from dataclasses import dataclass

# Load .env in development only
try:
    from dotenv import load_dotenv
except ImportError:
    print("Missing dependency: python-dotenv")
    print("Install with: pip install python-dotenv")
    sys.exit(1)


# --------------------------------------------------
# Configuration Dataclass
# --------------------------------------------------

@dataclass
class Config:
    MATRIX_MODE: str
    DATABASE_URL: str
    API_KEY: str
    LOG_LEVEL: str
    ZION_ENDPOINT: str


# --------------------------------------------------
# Load Environment Variables
# --------------------------------------------------

def load_configuration() -> Config:
    mode = os.getenv("MATRIX_MODE", "development")

    # Load .env only in development
    if mode == "development":
        load_dotenv()

    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    missing = [var for var in required_vars if not os.getenv(var)]

    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing)}"
        )

    return Config(
        MATRIX_MODE=os.getenv("MATRIX_MODE"),
        DATABASE_URL=os.getenv("DATABASE_URL"),
        API_KEY=os.getenv("API_KEY"),
        LOG_LEVEL=os.getenv("LOG_LEVEL"),
        ZION_ENDPOINT=os.getenv("ZION_ENDPOINT"),
    )


# --------------------------------------------------
# Logging Setup
# --------------------------------------------------

def configure_logging(level: str):
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )


# --------------------------------------------------
# Secure Secret Display
# --------------------------------------------------

def mask_secret(secret: str) -> str:
    return secret[:4] + "*" * (len(secret) - 8) + secret[-4:]


# --------------------------------------------------
# Main Oracle Execution
# --------------------------------------------------

def main():
    print("🔮 ORACLE INITIALIZING...\n")

    try:
        config = load_configuration()
    except EnvironmentError as e:
        print(f"CONFIG ERROR: {e}")
        sys.exit(1)

    configure_logging(config.LOG_LEVEL)

    logging.info(f"Matrix mode: {config.MATRIX_MODE}")

    if config.MATRIX_MODE == "development":
        logging.debug("Running in development mode.")
        logging.debug(f"Database: {config.DATABASE_URL}")
    elif config.MATRIX_MODE == "production":
        logging.info("Running in production mode.")
    else:
        logging.error("Invalid MATRIX_MODE value.")
        sys.exit(1)

    print("\n--- CONFIGURATION SUMMARY ---")
    print(f"MATRIX_MODE   : {config.MATRIX_MODE}")
    print(f"DATABASE_URL  : {config.DATABASE_URL}")
    print(f"API_KEY       : {mask_secret(config.API_KEY)}")
    print(f"LOG_LEVEL     : {config.LOG_LEVEL}")
    print(f"ZION_ENDPOINT : {config.ZION_ENDPOINT}")

    logging.info("Oracle connected to Zion endpoint.")
    logging.info("Oracle execution complete.")


if __name__ == "__main__":
    main()