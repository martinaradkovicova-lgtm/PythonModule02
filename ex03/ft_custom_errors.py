class GardenError(Exception):
    def __init__(self, error="Unknown garden error"):
        Exception.__init__(self, error)


class PlantError(GardenError):
    def __init__(self, error="Unknown plant error"):
        Exception.__init__(self, error)


class WaterError(GardenError):
    def __init__(self, error="Unknown water error"):
        Exception.__init__(self, error)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as ERROR:
        print(f"Caught PlantError: {ERROR}")

    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as ERROR:
        print(f"Caught WaterError: {ERROR}")

    print("\nTesting catching all garden errors...")

    errors_to_test = [
        PlantError("The tomato plant is wilting!"),
        WaterError("Not enough water in the tank!")
    ]

    for err in errors_to_test:
        try:
            raise err
        except GardenError as ERROR:
            print(f"Caught GardenError: {ERROR}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
