#!/usr/bin/env python3

import sys
import importlib
import subprocess
from pathlib import Path

print("LOADING STATUS: Loading programs...")
print("Checking dependencies:")


# ---------------------------------------
# Graceful Dependency Checker
# ---------------------------------------
def check_dependency(package_name):
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "Unknown")
        print(f"[OK] {package_name} ({version}) - Ready")
        return module, version
    except ImportError:
        print(f"[MISSING] {package_name} - Not installed")
        return None, None


pandas, pandas_version = check_dependency("pandas")
numpy, numpy_version = check_dependency("numpy")
matplotlib, matplotlib_version = check_dependency("matplotlib")
requests, requests_version = check_dependency("requests")

if not all([pandas, numpy, matplotlib]):
    print("\nERROR: Required dependencies missing.")
    print("Install using one of the following:\n")
    print("Using pip:")
    print("   pip install -r requirements.txt\n")
    print("Using Poetry:")
    print("   poetry install\n")
    sys.exit(1)


# ---------------------------------------
# Version Comparison (pip vs Poetry demo)
# ---------------------------------------
def compare_versions():
    print("\nDependency Version Report:")
    print("---------------------------")
    print(f"pandas     : {pandas_version}")
    print(f"numpy      : {numpy_version}")
    print(f"matplotlib : {matplotlib_version}")
    print(f"requests   : {requests_version}")
    print("\nNote:")
    print("- pip installs from requirements.txt (manual version control).")
    print("- Poetry uses pyproject.toml + poetry.lock (automatic locking).")
    print("- Poetry guarantees reproducible environments via lock file.")
    print("- pip requires tools like pip-tools for similar locking.")


# ---------------------------------------
# Matrix Data Analysis
# ---------------------------------------
def analyze_matrix_data():
    print("\nAnalyzing Matrix data...")

    # Simulate 1000x10 matrix
    rows = 1000
    cols = 10

    print(f"Processing {rows} data points...")

    matrix = numpy.random.rand(rows, cols)

    df = pandas.DataFrame(matrix, columns=[f"Feature_{i}" for i in range(cols)])

    summary = df.mean()

    return df, summary


# ---------------------------------------
# Visualization
# ---------------------------------------
def generate_visualization(summary):
    print("Generating visualization...")

    import matplotlib.pyplot as plt

    plt.figure()
    summary.plot(kind="bar")
    plt.title("Matrix Data Feature Means")
    plt.xlabel("Features")
    plt.ylabel("Mean Value")

    output_path = Path("matrix_analysis.png")
    plt.savefig(output_path)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


# ---------------------------------------
# Main Execution
# ---------------------------------------
if __name__ == "__main__":
    compare_versions()
    df, summary = analyze_matrix_data()
    generate_visualization(summary)