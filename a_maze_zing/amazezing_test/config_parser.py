def parse_config(filename):
    config = {}

    with open(filename) as f:
        for line in f:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            if "=" not in line:
                raise ValueError("Invalid config line")

            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]

    for r in required:
        if r not in config:
            raise ValueError(f"Missing required config key: {r}")

    return config