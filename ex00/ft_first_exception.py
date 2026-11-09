def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    test_input_val = ["25", "abc"]
    for temperature in test_input_val:
        print(f"Input data is '{temperature}'")
        try:
            temp = input_temperature(temperature)
            print(f"Temperature is now {temp}°C")
        except ValueError:
            print(f"Caught input_temperature error: "
                  f"invalid literal for int() with base 10: '{temp}'")
    print("All tests completed - program didn't crash!")
