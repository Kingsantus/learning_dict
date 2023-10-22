recipes_dict = {
    "Chicken and chips": {"chicken": 100, "potatoes": 3, "salt": 1, "malt vinegar": 5}
}

for recipe, ingredients in recipes_dict.items():
    print(f"Ingredients for {recipe}")
    for ingredient, quantity in ingredients.items():
        print(ingredient, quantity, sep=", ")
