from contents import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print("{} - {}".format(key, value))

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print("You have selected {}".format(selected_item))
        print("checking ingredient ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item in ingredients:
            quantity_in_pantry = pantry.get(food_item, 0)
            print("\t{} - Quantity in pantry: {}".format(food_item, quantity_in_pantry))
