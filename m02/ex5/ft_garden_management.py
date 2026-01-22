class GardenError(Exception):
    """This class manages generic error message with the garden"""
    def __init__(self, message="There is a problem in the garden"):
        super().__init__(message)


class PlantNameError(GardenError):
    """This class manages the error message for plant name"""
    def __init__(self, message="Plant name cannot be empty!"):
        super().__init__(message)


class PlantNotFoundError(GardenError):
    """
    This class manages the errors for the plants in the garden
    """
    pass


class WaterError(GardenError):
    """This class manages the errors for the water tank levels"""
    pass


class PlantHealthError(GardenError):
    """This class manages the errors for the Plant health status"""
    pass


class GardenManager:
    """This class manages the garden plants, watering and health"""
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

    def water_plants(self):
        """This function handles try, except and finally for plant watering"""
        print("Waterring plants\n")
        try:
            for plant in self.plants:
                print(f"Watering {plant} - success")

        except Exception:
            print(f"Error: Cannot water {plant} - invalid plant!")

        finally:
            print("Closing watering system (cleanup)\n")
            print("Watering completed successfully!\n")

    def check_plant_health(self, plant_name, water_level, sunlight_hours):
        """This function check the plant health"""
        print("Checking plant health...")
        error_flag = False
        try:
            if plant_name not in self.plants:
                error_flag = True
                raise PlantNotFoundError(f"Error: {plant_name} not in garden")
            if water_level < 1:
                error_flag = True
                raise WaterError(f"{water_level} is too low (min 1)\n")
            if water_level > 10:
                error_flag = True
                raise WaterError(f"{water_level} is too high(max 10)\n")
            if sunlight_hours < 2:
                error_flag = True
                raise PlantHealthError(f"{sunlight_hours} is too low (min 2)")
            if sunlight_hours > 12:
                error_flag = True
                raise PlantHealthError(f"{sunlight_hours} is too high(max 12)")
            print(f"Plant '{plant_name}' is healthy!\n")
        except PlantNotFoundError as error:
            print(f"Health check error: {error}")
        except WaterError as error:
            print(f"Health check error: {error}")
        finally:
            if error_flag is True:
                print("There is a health issue in your garden.")
            else:
                print("Garden management system test completed!")


def test_garden_manager():
    """This function is used to test GardenManager"""
    print("=== Garden Management System ===\n")

    print("adding plants to garden...")
    garden = GardenManager()
    garden.add_plant("Tomato")
    garden.add_plant("Pina")
    garden.add_plant("")
    garden.water_plants()
    garden.check_plant_health("Tomato", 3, 6)


# test_garden_manager()
