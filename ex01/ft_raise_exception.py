def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    test_input_val = ["25", "abc", "100", "-50"]
    for temperature in test_input_val:
        print(f"Input data is '{temperature}'")
        try:
            temp = input_temperature(temperature)
            print(f"Temperature is now {temp}°C")
            print()
        except ValueError as Error:
            print(f"Caught input_temperature error: {Error}")
            print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
