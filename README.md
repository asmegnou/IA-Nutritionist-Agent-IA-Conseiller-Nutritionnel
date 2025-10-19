# Smart NourishBot

Après avoir suivi le cours **IBM AI Agentic**, j'ai développé cette application sous forme de **projet guidé**. L'objectif initial était de créer un assistant capable d'analyser des images de plats, extraire les ingrédients, filtrer selon des restrictions alimentaires, analyser la valeur nutritionnelle et proposer des recettes.

Le projet original utilisait **CrewAI**, qui est une solution payante. Pour rendre le projet **accessible et gratuit**, j'ai recréé cette application en utilisant uniquement des **API et bibliothèques gratuites**, tout en conservant la logique et les fonctionnalités du projet original.

---

## Fonctionnalités

### 1. Extraction des ingrédients depuis une image
L'application utilise un modèle de classification d’images pré-entraîné (via Hugging Face Transformers) pour détecter les ingrédients présents sur une photo de plat.

### 2. Filtrage selon les restrictions alimentaires
Les ingrédients extraits peuvent être filtrés selon des régimes spécifiques (ex. vegan, gluten-free) grâce à un système simple de dictionnaire d’interdictions.

### 3. Analyse nutritionnelle
L'application récupère les informations nutritionnelles des ingrédients via l’**API gratuite USDA FoodData Central**. Elle fournit un aperçu des macronutriments et des calories estimées.

### 4. Suggestion de recettes (à venir)
La fonctionnalité de **suggestion de recettes** n'est pas encore implémentée et sera ajoutée dans une version future. Elle permettra de générer des recettes simples à partir des ingrédients filtrés, avec instructions et estimation calorique.

---

## Structure du projet

SmartNourishBot/
├─ main.py # Point d'entrée de l'application
├─ tools.py # Fonctions pour extraction, filtrage, analyse et recettes
├─ models.py # Modèles Pydantic pour structurer les données
├─ app_gradio.py # Interface utilisateur graphique
├─ requirements.txt # Librairies nécessaires
├─ README.md
├─ examples/ # Images de test
└─ .env # Clés API et configuration

## Execution
### 1. Créer un environnement virtuel et l’activer 
python -m venv venv
source venv/bin/activate    # Linux/macOS
# ou
venv\Scripts\activate       # Windows

### 3.Installer les dépendances :
pip install -r requirements.txt

### 4.Configurer la clé API USDA dans le fichier
USDA_API_KEY=VOTRE_CLE_USDA_ICI (ma clé est insérer ici)

## Uilisation
### 1. Via le terminal :
python main.py examples/food-1.jpg vegan

### 2. Via l'app Gradio :
python app_gradio.py
Ouvre ton navigateur sur http://127.0.0.1:7860

Uploader une image de plat et entrer une restriction alimentaire (facultatif)

Résultats affichés directement : ingrédients détectés, filtrés et analyse nutritionnelle