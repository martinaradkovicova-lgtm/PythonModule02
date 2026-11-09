def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        int("abc")  # ValueError
    elif operation_number == 1:
        1 / 0  # ZeroDivisionError
    elif operation_number == 2:
        open('/non/existent/file')  # FileNotFoundError
    elif operation_number == 3:
        "string" + 42  # type: ignore
    else:
        return


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    operations = [0, 1, 2, 3, 4]

    for op in operations:
        print(f"Testing operation {op}...")
        try:
            garden_operations(op)
            print("Operation completed successfully")
        except ValueError as ERROR:
            print(f"Caught ValueError: {ERROR}")
        except ZeroDivisionError as ERROR:
            print(f"Caught ZeroDivisionError: {ERROR}")
        except FileNotFoundError as ERROR:
            print(f"Caught FileNotFoundError: {ERROR}")
        except TypeError as ERROR:
            print(f"Caught TypeError: {ERROR}")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
