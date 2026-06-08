from elements import create_fire
from ..elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    air: str = create_air()
    strength: str = strength_potion()
    fire: str = create_fire()
    gold: str = (
        "Recipe transmuting Lead to Gold: brew"
        f" '{air}' and '{strength}' mixed with '{fire}'"
    )
    return gold
