#!/usr/bin/env python3

import sys
import os
import site
import platform


def is_virtual_environment():
    """
    Detect if running inside a virtual environment.
    """
    # Method 1: venv detection
    if hasattr(sys, 'real_prefix'):
        return True

    # Method 2: compare base_prefix and prefix
    return sys.prefix != getattr(sys, "base_prefix", sys.prefix)


def print_environment_info():
    """
    Display information about the current Python environment.
    """
    print("=" * 60)
    print("PYTHON ENVIRONMENT INFORMATION")
    print("=" * 60)
    print(f"Python version      : {platform.python_version()}")
    print(f"Python executable   : {sys.executable}")
    print(f"Platform            : {platform.system()} {platform.release()}")
    print(f"sys.prefix          : {sys.prefix}")
    print(f"sys.base_prefix     : {getattr(sys, 'base_prefix', 'N/A')}")
    print()


def print_package_locations():
    """
    Show global vs virtual environment package locations.
    """
    print("=" * 60)
    print("PACKAGE LOCATIONS")
    print("=" * 60)

    # Global site-packages
    try:
        global_site = site.getsitepackages()
    except AttributeError:
        global_site = ["Not available on this platform"]

    print("Global site-packages:")
    for path in global_site:
        print(f"  - {path}")

    print()

    # Virtual environment site-packages
    venv_site = site.getusersitepackages()
    print("User site-packages:")
    print(f"  - {venv_site}")
    print()


def print_venv_instructions():
    """
    Provide instructions to create and activate a virtual environment.
    """
    print("=" * 60)
    print("NO VIRTUAL ENVIRONMENT DETECTED")
    print("=" * 60)
    print("To create a virtual environment, run:")
    print("  python -m venv venv")
    print()
    print("To activate it:")
    print("  On macOS/Linux:")
    print("    source venv/bin/activate")
    print("  On Windows:")
    print("    venv\\Scripts\\activate")
    print()
    print("After activation, re-run this script.")
    print()


def main():
    print_environment_info()

    if is_virtual_environment():
        print("✅ You are running inside a VIRTUAL ENVIRONMENT.\n")
    else:
        print("⚠️  You are running in the GLOBAL Python environment.\n")
        print_venv_instructions()

    print_package_locations()


if __name__ == "__main__":
    main()
