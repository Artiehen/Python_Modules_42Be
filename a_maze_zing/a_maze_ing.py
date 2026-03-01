import sys
import os
import random
from mlx import Mlx


def parse_config(filename):
    config = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=")
            config[key.strip()] = value.strip()
    return config


def main():
    # print("Amazing")
    if len(sys.argv) != 2:
        print("Missing configuration file")
    else:
        parse_config("config.txt")


if __name__ == "__main__":
    main()
