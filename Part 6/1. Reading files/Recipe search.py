def search_by_name(filename: str, word: str):
    recipes = read_recipes(filename)
    searched_word = word.lower()
    found_recipes = []

    for recipe in recipes:
        recipe_name = recipe[0]
        if searched_word in recipe_name.lower():
            found_recipes.append(recipe_name)
    
    return found_recipes


def search_by_time(filename: str, prep_time: int):
    recipes = read_recipes(filename)
    found_recipes = []

    for recipe in recipes:
        recipe_name = recipe[0]
        recipe_time = int(recipe[1])
        if recipe_time <= prep_time:
            found_recipes.append(f"{recipe_name}, preparation time {recipe_time} min")

    return found_recipes


def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_recipes(filename)
    found_recipes = []

    for recipe in recipes:
        recipe_name = recipe[0]
        recipe_time = int(recipe[1])
        ingredients = recipe[2:]
        for item in ingredients:
            if ingredient.lower() in item:
                found_recipes.append(f"{recipe_name}, preparation time {recipe_time} min")
    
    return found_recipes


def read_recipes(filename):
    recipes = []
    recipe = []

    with open(filename) as recipe_file:
        for line in recipe_file:
            line = line.strip()
            if line == "":
                if recipe:
                    recipes.append(recipe)
                recipe = []
            else:
                recipe.append(line)
    if recipe:
        recipes.append(recipe)

    return recipes


if __name__ == "__main__":
    found_recipes = search_by_name("recipes1.txt", "cake")
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_time("recipes1.txt", 20)
    for recipe in found_recipes:
        print(recipe)

    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)