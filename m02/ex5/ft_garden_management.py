class GardenError(Exception):
    def __init__(self, message="There is a problem in the garden"):
        super().__init__(message)


class PlantNameError(GardenError):
    def __init__(self, message="Plant name cannot be empty!"):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message="Not enough water in the tank!"):
        super().__init__(message)


class GardenManager:
    def __init__(self):
        self.plants = []

    def add_plant(self, plant_name):
        try:
            if plant_name == "":
                raise PlantNameError()

            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")

        except PlantNameError as error:
            print(f"Error adding plant: {error}")

    def water_plants(plant_list):
        """This function handles try, except and finally"""
        error_occurred = False
        try:
            for plant in plant_list:
                if plant == "" or plant is None:
                    raise ValueError("Invalid plant name")
                print(f"Watering {plant} - success")

        except Exception:
            error_occurred = True
            print(f"Error: Cannot water {plant} - invalid plant!")

        finally:
            if error_occurred:
                print("Closing watering system (cleanup)")
                print("Cleanup always happens, even with errors\n")
            else:
                print("Closing watering system (cleanup)\n")
                print("Watering completed successfully!\n")

    def check_plant_health(plant_name, water_level, sunlight_hours):
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


def test_garden_manager():
    print("=== Garden Management System ===\n")

    print("adding plants to garden...")
    garden = GardenManager()
    garden.add_plant("Tomato")
    garden.add_plant("")


test_garden_manager()
