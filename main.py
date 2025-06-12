# main.py - Created by AI Programmer
import json

def load_recipes(file_path="recipes.json"):
    """Loads recipes from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing recipes.

    Returns:
        list: A list of recipe dictionaries. Returns an empty list if the file
              doesn't exist or there's an error loading the JSON.
    """
    try:
        with open(file_path, 'r') as f:
            recipes = json.load(f)
        return recipes
    except FileNotFoundError:
        print(f"Error: Recipe file '{file_path}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return []

def search_recipes(ingredients, recipes):
    """Searches for recipes that can be made with the given ingredients.

    Args:
        ingredients (list): A list of available ingredients.
        recipes (list): A list of recipe dictionaries.

    Returns:
        list: A list of recipe dictionaries that can be made with the
              given ingredients.
    """
    suggested_recipes = []
    for recipe in recipes:
        missing_ingredients = [ingredient for ingredient in recipe['ingredients'] if ingredient not in ingredients]
        if not missing_ingredients:
            suggested_recipes.append(recipe)
        else:
            # Add recipes that require at most 2 missing ingredients (prioritize those with fewer)
            if len(missing_ingredients) <= 2:
                recipe['missing_ingredients'] = missing_ingredients
                suggested_recipes.append(recipe)

    # Sort the suggested recipes: first by whether they require missing ingredients, then by number of missing ingredients
    suggested_recipes.sort(key=lambda x: (
        'missing_ingredients' in x,  # Prioritize recipes without missing ingredients
        len(x.get('missing_ingredients', []))  # Then prioritize fewer missing ingredients
    ))
    return suggested_recipes

def display_menu():
    print("Recipe Suggestion App")
    print("-----------------------")
    print("1. Enter available ingredients")
    print("2. Get recipe suggestions")
    print("3. Exit")

def main():
    available_ingredients = []
    recipes = load_recipes()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Enter ingredients (separated by commas):")
            ingredients_str = input()
            available_ingredients = [ingredient.strip() for ingredient in ingredients_str.split(',')]
            print(f"Ingredients added: {available_ingredients}")

        elif choice == '2':
            if not recipes:
                print("No recipes loaded. Please check your recipes.json file.")
            elif not available_ingredients:
                print("Please enter available ingredients first.")
            else:
                suggested_recipes = search_recipes(available_ingredients, recipes)
                if suggested_recipes:
                    print("Suggested Recipes:")
                    for recipe in suggested_recipes:
                        if 'missing_ingredients' in recipe:
                            print(f"- {recipe['name']} (Missing: {', '.join(recipe['missing_ingredients'])})")
                        else:
                            print(f"- {recipe['name']}")
                else:
                    print("No recipes found that can be made with the given ingredients.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()