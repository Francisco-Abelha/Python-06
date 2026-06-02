from alchemy.elements import create_air


def main() -> None:
    print("=== Alembic 3 ===")
    print("Accessing alchemy/elements.py using'from ... import ...' structure")
    string: str = create_air()
    print(f"Testing create_air: {string}")


if __name__ == "__main__":
    main()