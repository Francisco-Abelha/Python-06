import alchemy.transmutation.recipes


def main() -> None:
    print("=== Transmutation 0 ===")
    print("Using file alchemy/transmutation/recipes.py directly")
    transmut_0: str = alchemy.transmutation.recipes.lead_to_gold()
    print(f"Testing lead to gold: {transmut_0}")


if __name__ == "__main__":
    main()
