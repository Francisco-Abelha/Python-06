import alchemy.transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")
    transmut_1: str = alchemy.transmutation.lead_to_gold()
    print(f"Testing lead to gold: {transmut_1}")


if __name__ == "__main__":
    main()
