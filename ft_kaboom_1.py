def main() -> None:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
    import alchemy.grimoire.dark_spellbook
    test2: str = alchemy.grimoire.dark_spellbook.dark_spell_record(
        "Evil", "bats oats slime"
    )
    print(test2)


if __name__ == "__main__":
    main()
