from alchemy.potions import healing_potion, strength_potion


def main() -> None:
    print("=== Distillation 0 ===")
    print("Direct access to alchemy/potions.py")
    health: str = healing_potion()
    strength: str = strength_potion()
    print(f"Testing strength_potion: {strength}")
    print(f"Testing healing_potion: {health}")


if __name__ == "__main__":
    main()
