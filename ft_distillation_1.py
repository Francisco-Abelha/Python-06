import alchemy


def main() -> None:
    print("=== Distillation 1 ===")
    print("Using:'import alchemy' structure to access potions")
    strength: str = alchemy.strength_potion()
    health: str = alchemy.heal()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing heal alias: {health}")


if __name__ == "__main__":
    main()
