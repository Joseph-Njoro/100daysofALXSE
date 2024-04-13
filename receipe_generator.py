import random

# Define lists of ingredients and recipes
ingredients = {
    'vegetables': ['carrots', 'broccoli', 'spinach', 'bell peppers', 'onions','tomatoes', 'zucchini', 'mushrooms'],
    'protein': ['chicken', 'beef', 'tofu', 'salmon', 'shrimp', 'eggs', 'beans']
    'carbs': ['pasta', 'rice', 'quinoa', 'potatoes', 'bread', 'couscous', 'tortillas'],    'spices': ['salt', 'pepper', 'garlic powder', 'paprika', 'cumin', 'oregano', 'curry powder', 'chili flakes'],
   'sauces': ['soy sauce', 'tomato sauce', 'pesto', 'barbecue sauce', 'sriracha', 'honey mustard', 'vinaigrette']
}
recipes = 
    'Stir-Fry': ['protein', 'vegetables', 'soy sauce', 'rice']
    'Pasta Primavera': ['pasta', 'vegetables', 'garlic', 'olive oil']
    'Grilled Chicken Salad': ['chicken', 'vegetables', 'vinaigrette', 'greens']
    'Vegetable Curry': ['vegetables', 'protein', 'curry powder', 'coconut milk', 'rice'],    'Bean Burritos': ['protein', 'tortillas', 'beans', 'vegetables', 'salsa'],
   'Salmon with Roasted Vegetables': ['salmon', 'vegetables', 'olive oil', 'spices']
}
# Define a function to geneate a random recipe
def generate_random_recipe()
    recipe_name = random.choice(list(reipes.keys()))
    ingredients_needed = recipes[recipe_ame]
    random_ingredients = {category: rando.choice(ingredients[category]) for category in ingredients_needed}
    return recipe_name, random_ingredients
# Main prgram loop
while True
    print("Welcome to the Random Recipe Geneator!")
    print("Let's see what's cooking today..."
    input("Press Enter to generate a random recipe!")
    # Generate a random recip
    recipe_name, random_ingredients = generate_random_recipe()
    # Printthe generated recipe
    print("\ recipe_name)
    print("Ingredients:"
    for category, ingredient in random_ingredients.item():
        print("- " + ingredient + " (" + category + ")")
    # Ask he user if they want to generate another recipe
    print("nEnjoy your meal!")
    again = nput("Would you like to generate another random recipe? (yes/no): ")
    if again.ower() != 'yes':
        print(Thanks for using the Random Recipe Generator. Bon appétit!")
        break