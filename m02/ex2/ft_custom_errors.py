class GardenError(Exception):
    """This class handles the generic error message in Garden"""
    def __init__(self, message="There is a problem in the garden"):
        super().__init__(message)


class PlantError(GardenError):
    """This class handles specific error message with a plant"""
    def __init__(self, message="is wilting!"):
        super().__init__(message)


class WaterError(GardenError):
    """This class handles error messages with the water tank"""
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


def days_without_water(days):
    """This function simulates the most amount of days without water"""
    if days > 2:
        raise PlantError()


def water_level(lts):
    """This function determines the lower limit for the water tank"""
    if lts < 50:
        raise WaterError()


def test_custom_errors():
    """This functions test the custom error messages"""
    plant1 = "tomato"
    print("=== Custom Garden Errors Demo ===\n")

    try:
        print("Testing Plant Error...")
        days_without_water(5)
    except PlantError as e:
        print(f"Caught PlantError: The {plant1} {e}\n")

    try:
        print("Testing WaterError...")
        water_level(20)
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("All custom error types work correctly!")


# test_custom_errors()
