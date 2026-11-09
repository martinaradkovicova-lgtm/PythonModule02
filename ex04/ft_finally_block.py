class GardenError(Exception):
    def __init__(self, error_message="Unknown garden error"):
        Exception.__init__(self, error_message)


class PlantError(GardenError):
    def __init__(self, error_message="Unknown plant error"):
        GardenError.__init__(self, error_message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")

    test_cases = [
        ("Testing valid plants...", ["Tomato", "Lettuce", "Carrots"]),
        ("Testing invalid plants...", ["Tomato", "lettuce", "Carrots"])
    ]

    for test_title, plants in test_cases:
        print(f"\n{test_title}")
        try:
            print("Opening watering system")
            for plant in plants:
                water_plant(plant)
        except PlantError as ERROR:
            print(f"Caught PlantError: {ERROR}")
            print(".. ending tests and returning to main")
        finally:
            print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
