def check_temperature(temp_str):
    """
    This function determines weather the temperature
    is within range or not
    """
    try:
        temp = float(temp_str)
        if temp > 0 and temp < 40:
            print(f"Temperature {temp}°C is perfect for plants!")

        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants(min 0°C)")

        elif temp > 40:
            (print(f"Error: {temp_str}°C is too hot for plants(max 40°C)"))
        return temp

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None


def test_temperature_input():
    """This functions calls check_temperature and inputs values"""
    print("=== Garden Temperature Checker ===")
    test_inputs = ["25", "abc", "100", "-50"]
    for value in test_inputs:
        print(f"\nTesting temperature: {value}")
        check_temperature(value)
    print("\nAll test completed - program didn't crash!")


# test_temperature_input()
