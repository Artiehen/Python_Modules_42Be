def check_plant_health(plant_name, water_level, sunlight_hours):
    """This function sets the limits for water and sunlight values as
    well as assures no empty string is added as plant name"""
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level < 1:
        raise ValueError(f"{water_level} is too low (min 1)\n")
    if water_level > 10:
        raise ValueError(f"{water_level} is too high(max 10)\n")
    if sunlight_hours < 2:
        raise ValueError(f"{sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f"{sunlight_hours} is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks():
    """
    This function test the various values for plant health
    """
    print("=== Garden Plant Health Checker ===\n")
    print("testing good values...")
    try:
        res = check_plant_health("Tomato", 5, 6)
        print(res)
    except ValueError as error:
        print(f"Error: {error}\n")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 5, 6)
    except ValueError as error:
        print(f"Error: {error}\n")

    print("Testing bad water level...")
    try:
        check_plant_health("Tomato", 20, 6)
    except ValueError as error:
        print(f"Error: Water level {error}\n")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("Tomato", 5, 1)
    except ValueError as error:
        print(f"Error: Sunlight hours {error}")


test_plant_checks()
