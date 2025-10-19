from pydantic import BaseModel, Field
from typing import List, Optional

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    instructions: str
    calorie_estimate: int

class RecipeSuggestionOutput(BaseModel):
    recipes: List[Recipe]

class NutrientBreakdown(BaseModel):
    protein: Optional[str] = None
    carbohydrates: Optional[str] = None
    fats: Optional[str] = None

class NutrientAnalysisOutput(BaseModel):
    dish: Optional[str] = None
    portion_size: Optional[str] = None
    estimated_calories: Optional[int] = None
    nutrients: NutrientBreakdown = NutrientBreakdown()
    health_evaluation: Optional[str] = None
