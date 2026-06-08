import alchemy.grimoire


def main() -> None:
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    test1: str = alchemy.grimoire.light_spellbook.light_spell_record(
        "Fantasy", "Earth Wind Fire"
    )
    print(f"Testing record light spell: {test1}")


if __name__ == "__main__":
    main()
