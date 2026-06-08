import alchemy


def main() -> None:
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using'import alchemy'")
    try:
        air: str = alchemy.create_air()
        print(f"Testing create_air: {air}")
    except Exception as e:
        print(f"Caught Something: {e}")
    print("Now show that not all functions can be reached")
    print("This will raise an exception!")
    try:
        earth: str = alchemy.create_earth()
        print(f"Testing the hidden create_earth: {earth}")
    except Exception as e:
        print(f"Caught Something: {e}")


if __name__ == "__main__":
    main()
