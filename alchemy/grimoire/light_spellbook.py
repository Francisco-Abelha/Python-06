from .light_validator import *


def light_spell_allowed_ingredients() -> list[str]:
    return allowed_ingredients_list


def light_spell_record(spell_name: str, ingredients: str) -> str:
    spell_record: str = ""
    spell_validation: str = validate_ingredients(ingredients)
    if "INVALID" not in spell_validation:
        spell_record = "Spell recorded: "
    else:
        spell_record = "Spell rejected: "
    spell_record += f"{spell_name} ({spell_validation})"
    return spell_record
