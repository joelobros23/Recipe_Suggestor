class Ingredients:
    """
    A class for managing a list of ingredients.
    """

    def __init__(self, ingredients=None):
        """
        Initializes the Ingredients object with an optional list of ingredients.

        Args:
            ingredients (list, optional): A list of ingredient names. Defaults to None (empty list).
        """
        if ingredients is None:
            self.ingredients = []
        else:
            self.ingredients = ingredients

    def add_ingredient(self, ingredient):
        """
        Adds an ingredient to the list.

        Args:
            ingredient (str): The name of the ingredient to add.
        """
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        """
        Removes an ingredient from the list.

        Args:
            ingredient (str): The name of the ingredient to remove.
        """
        try:
            self.ingredients.remove(ingredient)
        except ValueError:
            print(f"{ingredient} not found in the ingredient list.")

    def get_ingredients(self):
        """
        Returns the list of ingredients.

        Returns:
            list: The list of ingredient names.
        """
        return self.ingredients

    def clear_ingredients(self):
        """
        Clears the list of ingredients.
        """
        self.ingredients = []

    def __str__(self):
        """
        Returns a string representation of the Ingredients object.

        Returns:
            str: A comma-separated string of ingredient names.
        """
        return ", ".join(self.ingredients)