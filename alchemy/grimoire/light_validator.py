allowed_ingredients_list: list[str] = ["air", "water", "earth", "fire"]


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = allowed_ingredients_list
    status: str = " — INVALID"
    ingredients_list: list[str] = ingredients.split()
    full_str: str = ""
    for element in ingredients_list:
        lower = element.lower()
        if lower in allowed:
            status = " — VALID"
    full_str = ", ".join(ingredients_list[:-1])
    full_str += " and " + ingredients_list[-1]
    full_str += status
    return full_str
