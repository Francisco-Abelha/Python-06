import alchemy


def main() -> None:
    print("=== Transmutation 2 ===")
    print("Import alchemy module only")
    transmut_2: str = alchemy.lead_to_gold()
    print(f"Testing lead to gold: {transmut_2}")


if __name__ == "__main__":
    main()
