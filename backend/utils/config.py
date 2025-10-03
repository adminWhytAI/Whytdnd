"""
Configuration centrale du projet WhytDD
"""
import os
from pathlib import Path
import json

# Chemins de base
BASE_DIR = Path(__file__).resolve().parent.parent.parent
MODELS_DIR = BASE_DIR / "models"
GGUF_DIR = MODELS_DIR / "gguf"
EMBEDDINGS_DIR = MODELS_DIR / "embeddings"
CONFIG_DIR = MODELS_DIR / "config"
DATA_DIR = BASE_DIR / "data"
CHROMADB_DIR = DATA_DIR / "chromadb"
CHARACTERS_DIR = DATA_DIR / "characters"
DOCUMENTATION_DIR = BASE_DIR / "Documentation"

# Chemins configuration
MODEL_CONFIG_PATH = CONFIG_DIR / "model_config.json"
RULES_DATABASE_PATH = DATA_DIR / "rules_database.json"

def load_model_config():
    """Charge la configuration du modèle"""
    if not MODEL_CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration modèle non trouvée: {MODEL_CONFIG_PATH}\n"
            f"Créer le fichier models/config/model_config.json"
        )
    
    with open(MODEL_CONFIG_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

# Charger config
MODEL_CONFIG = load_model_config()

# Configuration GGUF (production = Mistral 7B)
GGUF_CONFIG = MODEL_CONFIG['gguf_model']
GGUF_MODEL_PATH = BASE_DIR / GGUF_CONFIG['path']
CONTEXT_SIZE = GGUF_CONFIG['context_size']
N_THREADS = GGUF_CONFIG['threads']
N_GPU_LAYERS = GGUF_CONFIG['gpu_layers']
GGUF_PARAMS = GGUF_CONFIG['default_params']
SPECIAL_TOKENS = GGUF_CONFIG.get('special_tokens', {})

# Configuration Embeddings
EMBEDDING_CONFIG = MODEL_CONFIG['embedding_model']
EMBEDDING_MODEL_NAME = EMBEDDING_CONFIG['name']
EMBEDDING_DEVICE = EMBEDDING_CONFIG['device']

# Configuration API
API_HOST = os.getenv('WHYTDD_API_HOST', '0.0.0.0')
API_PORT = int(os.getenv('WHYTDD_API_PORT', 8000))
API_RELOAD = os.getenv('WHYTDD_API_RELOAD', 'true').lower() == 'true'

# Configuration CORS
CORS_ORIGINS = os.getenv('WHYTDD_CORS_ORIGINS', 'http://localhost:5173,http://localhost:3000').split(',')

# Configuration ChromaDB
CHROMADB_UNIVERSAL_PATH = str(CHROMADB_DIR / "universal")
CHROMADB_CHARACTERS_PATH = str(CHROMADB_DIR / "characters")

# Logging
LOG_LEVEL = os.getenv('WHYTDD_LOG_LEVEL', 'INFO')
LOG_FILE = BASE_DIR / "whytdd.log"

# Vérifications
def verify_setup():
    """Vérifie que le setup est correct"""
    issues = []
    
    # Vérifier modèle GGUF
    if not GGUF_MODEL_PATH.exists():
        issues.append(f"❌ Modèle GGUF non trouvé: {GGUF_MODEL_PATH}")
    
    # Vérifier dossiers
    required_dirs = [MODELS_DIR, DATA_DIR, CHROMADB_DIR, CHARACTERS_DIR]
    for dir_path in required_dirs:
        if not dir_path.exists():
            issues.append(f"❌ Dossier manquant: {dir_path}")
    
    if issues:
        return False, issues
    
    return True, ["✅ Configuration valide"]

if __name__ == "__main__":
    # Test configuration
    print("="*60)
    print("WHYTDD - Vérification Configuration")
    print("="*60)
    print(f"\n📂 Chemins:")
    print(f"  BASE_DIR: {BASE_DIR}")
    print(f"  MODELS_DIR: {MODELS_DIR}")
    print(f"  DATA_DIR: {DATA_DIR}")
    print(f"\n🤖 Modèle GGUF:")
    print(f"  Nom: {GGUF_CONFIG['name']}")
    print(f"  Path: {GGUF_MODEL_PATH}")
    print(f"  Exists: {GGUF_MODEL_PATH.exists()}")
    print(f"  Context: {CONTEXT_SIZE}")
    print(f"  GPU Layers: {N_GPU_LAYERS}")
    print(f"\n📊 Embeddings:")
    print(f"  Model: {EMBEDDING_MODEL_NAME}")
    print(f"  Device: {EMBEDDING_DEVICE}")
    print(f"\n🌐 API:")
    print(f"  Host: {API_HOST}:{API_PORT}")
    print(f"  CORS: {CORS_ORIGINS}")
    
    print(f"\n{'='*60}")
    valid, messages = verify_setup()
    for msg in messages:
        print(msg)
    print("="*60)
