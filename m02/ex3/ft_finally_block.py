def water_plants(plant_list):
    """This function handles try, except and finally"""
    valid_plants = ["tomato", "lettuce", "carrot"]
    error_occurred = False
    try:
        for plant in plant_list:
            if plant not in valid_plants:
                raise ValueError("Invalid plant name")
            print(f"Watering {plant}")

    except Exception:
        error_occurred = True
        print(f"Error: Cannot water {plant} - invalid plant!")

    finally:
        if error_occurred:
            print("Closing watering system (cleanup)\n")
            print("Cleanup always happens, even with errors\n")
        else:
            print("Closing watering system (cleanup)")
            print("Watering completed successfully!\n")


def test_watering_system():
    """This function initializes water_plants and inputs data"""
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    print("Opening watering system")
    good_plants = ["tomato", "lettuce", "carrot"]
    water_plants(good_plants)

    print("Testing with error...")
    bad_plants = ["tomato", "None", "carrot"]
    water_plants(bad_plants)


# test_watering_system()
