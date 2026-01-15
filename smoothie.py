def smoothie(ingredients: list[str], base: str = "water", ice: bool = True) -> str:
    """
    Create a smoothie!

    Returns a description of the smoothie with ingredients listed in alphabetical order.

    Args:
        ingredients (list of str): List of ingredients (must be non-empty).
        base (str): The liquid base for the smoothie (default: water).
        ice (bool): Whether to include ice.

    Returns:
        str: A description of the smoothie.
    """
    base_str = base.strip().lower()
    if base_str == "":
        base_str = "water"
        #Leaving base blank inputs the default value water 

    if not ingredients:
        return f"{'Icy' if ice else 'Just'} {base_str.title()}!"
    #if no ingredients are entered then it produces Icy water if there is ice, else it is just water

    if not all(isinstance(i, str) for i in ingredients):
        return "I don't know how to make that smoothie!"
    #I do not know how to get to this 

    unique_ingredients = sorted(set(ingredient.strip().lower() for ingredient in ingredients))
    #im assuming it sorts the ingredient in alphabetical order and also forces lower case lettering 

    smoothie = f"{'Icy ' if ice else ''}{base_str.title()} smoothie with " + ", ".join(unique_ingredients)
    #putting it all together
    return smoothie

print(smoothie([" "]," ", False ))



#sjfkdsjkfndsj ksdjfkdsjkjjdjksjgsd
#random comment