from .elements import create_air, create_earth
from elements import create_fire, create_water


def healing_potion() -> str:
    earth: str = create_earth()
    air: str = create_air()
    health: str = f"Healing potion brewed with '{earth}' and '{air}'"
    return health


def strength_potion() -> str:
    fire: str = create_fire()
    water: str = create_water()
    strength: str = f"Strength potion brewed with '{fire}' and '{water}'"
    return strength
