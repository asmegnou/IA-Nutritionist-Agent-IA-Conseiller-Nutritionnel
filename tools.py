import os
import requests
from PIL import Image
from transformers import pipeline
from typing import List
from dotenv import load_dotenv

load_dotenv()
USDA_API_KEY = os.environ.get("USDA_API_KEY")

# 1Extraction des ingrédients
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

def extract_ingredients(image_path: str) -> List[str]:
    image = Image.open(image_path)
    results = classifier(image)
    return [r['label'] for r in results[:5]]

# Filtrage selon restrictions alimentaires
DIETARY_RESTRICTIONS = {
    "vegan": ["chicken", "beef", "egg", "milk", "cheese", "fish"],
    "gluten-free": ["wheat", "barley", "rye", "pasta", "bread"]
}

def filter_ingredients(ingredients: List[str], restriction: str = None) -> List[str]:
    if not restriction:
        return ingredients
    forbidden = DIETARY_RESTRICTIONS.get(restriction.lower(), [])
    return [i for i in ingredients if i.lower() not in forbidden]

# 3 Analyse nutritionnelle via USDA
def analyze_nutrients(ingredient_name: str) -> dict:
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={ingredient_name}&api_key={USDA_API_KEY}"
    response = requests.get(url).json()
    if response.get("foods"):
        food = response["foods"][0]
        nutrients = {n["nutrientName"]: n["value"] for n in food.get("foodNutrients", [])}
        return nutrients
    return {}

# 4Suggestions de recette simples
def suggest_recipes(filtered_ingredients: List[str]) -> List[dict]:
    recipe = {
        "title": "Simple Dish",
        "ingredients": filtered_ingredients,
        "instructions": f"Combine {' ,'.join(filtered_ingredients)} and cook for 10 minutes.",
        "calorie_estimate": 300
    }
    return [recipe]
