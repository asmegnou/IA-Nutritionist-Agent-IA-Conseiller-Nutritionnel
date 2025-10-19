import gradio as gr
from tools import extract_ingredients, filter_ingredients, analyze_nutrients, suggest_recipes

def run_smartbot(image, dietary_restrictions=None):
    # Extraction des ingrédients
    ingredients = extract_ingredients(image)

    # Filtrage selon restrictions alimentaires
    filtered = filter_ingredients(ingredients, dietary_restrictions)

    # Analyse nutritionnelle
    nutrients = {i: analyze_nutrients(i) for i in filtered}

    # Suggestions de recettes
    recipes = suggest_recipes(filtered)

    # Préparer les affichages
    ingredients_text = ", ".join(ingredients) if ingredients else "Aucun ingrédient détecté."
    filtered_text = ", ".join(filtered) if filtered else "Aucun ingrédient après filtrage."

    nutrient_text = ""
    if nutrients:
        for ingredient, nutri in nutrients.items():
            nutrient_text += f"{ingredient}:\n"
            for k, v in nutri.items():
                nutrient_text += f"  - {k}: {v}\n"
    else:
        nutrient_text = "Aucune information nutritionnelle disponible."

    recipes_text = ""
    if recipes:
        for r in recipes:
            recipes_text += f"Recette: {r['title']}\n"
            recipes_text += f"Ingrédients: {', '.join(r['ingredients'])}\n"
            recipes_text += f"Instructions: {r['instructions']}\n"
            recipes_text += f"Calories estimées: {r['calorie_estimate']}\n\n"
    else:
        recipes_text = "Aucune recette disponible."

    return ingredients_text, filtered_text, nutrient_text, recipes_text

# Interface Gradio
iface = gr.Interface(
    fn=run_smartbot,
    inputs=[
        gr.Image(type="filepath", label="Upload your food image"),
        gr.Textbox(lines=1, placeholder="Optional dietary restriction (e.g., vegan)", label="Dietary restriction")
    ],
    outputs=[
        gr.Textbox(label="Detected Ingredients"),
        gr.Textbox(label="Filtered Ingredients"),
        gr.Textbox(label="Nutritional Analysis"),
        gr.Textbox(label="Recipe Suggestions")
    ],
    title="Smart NourishBot",
    description="Upload a food image to extract ingredients, filter by dietary restrictions, analyze nutrients, and suggest recipes.",
    theme="default"
)

if __name__ == "__main__":
    # Lancer localement sans tunnel
    iface.launch(share=False)
