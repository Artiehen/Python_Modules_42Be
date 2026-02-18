def validate_ingredients(ingredients: str) -> str:
    if ('fire' in ingredients or 'water' in ingredients):
        return f"{ingredients} - VALID"
    elif ('earth' in ingredients or 'air' in ingredients):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
