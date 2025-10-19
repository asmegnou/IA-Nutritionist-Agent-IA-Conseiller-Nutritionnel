import sys
from tools import extract_ingredients, filter_ingredients, analyze_nutrients, suggest_recipes

def run(image_path: str, dietary_restrictions: str = None):
    print("## Welcome to Smart NourishBot")
    print("------------------------------")

    # 1er Extraction
    ingredients = extract_ingredients(image_path)
    print("Ingredients:", ingredients)

    # 2️éem  Filtrage
    filtered = filter_ingredients(ingredients, dietary_restrictions)
    print("Filtered Ingredients:", filtered)

    # 3em Analyse nutritionnelle
    nutrients = {i: analyze_nutrients(i) for i in filtered}
    print("Nutrients:", nutrients)

    # 4em Suggestions de recettes
    recipes = suggest_recipes(filtered)
    print("Recipe Suggestions:", recipes)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <image_path> [dietary_restrictions]")
    else:
        image_path = sys.argv[1]
        dietary_restrictions = sys.argv[2] if len(sys.argv) > 2 else None
        run(image_path, dietary_restrictions)
