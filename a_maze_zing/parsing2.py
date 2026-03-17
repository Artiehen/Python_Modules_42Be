class ConfigError(Exception):
    pass

def parse_config(file):
    config = {}

    try:
        with open(file, "r") as f:
            for line in f:
                line = line.strip()

                if not line or line.startswith("#"):
                    continue

                if "=" not in line:
                    raise ConfigError(f"Invalid key Value: {line}")
                
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()

    except (FileNotFoundError, ConfigError):
        raise ConfigError("Config file not found")

    return validate_config(config)


def validate_config(cfg):
    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    for key in required:
        if key not in cfg:
            raise ConfigError(f"Missing key: {key}")

    width = int(cfg["WIDTH"])
    height = int(cfg["HEIGHT"])

    entry = tuple(map(int, cfg["ENTRY"].split(",")))
    exit_ = tuple(map(int, cfg["EXIT"].split(",")))

    perfect = cfg["PERFECT"].lower() == "true"

    if entry == exit_:
        raise ConfigError("Entry and exit must differ")

    return {
        "width": width,
        "height": height,
        "entry": entry,
        "exit": exit_,
        "output": cfg["OUTPUT_FILE"],
        "perfect": perfect
    }


def main():

    file = "config.txt"
    print(f"{parse_config(file)}")


if __name__ == "__main__":
    main()
