"""
Script pour télécharger Mistral-7B-Instruct-v0.2 depuis Hugging Face
"""
import sys
from pathlib import Path

# Ajouter backend au path
sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from huggingface_hub import hf_hub_download
except ImportError:
    print("❌ huggingface-hub n'est pas installé")
    print("Installation: pip install huggingface-hub")
    sys.exit(1)

from utils.config import GGUF_DIR

def download_mistral():
    """Télécharge Mistral 7B Instruct"""
    
    model_id = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
    filename = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"
    
    destination = GGUF_DIR / filename
    
    # Vérifier si déjà téléchargé
    if destination.exists():
        print(f"✅ {filename} est déjà téléchargé dans models/gguf/")
        size_gb = destination.stat().st_size / (1024**3)
        print(f"   Taille: {size_gb:.2f} GB")
        return
    
    print("="*70)
    print("📥 TÉLÉCHARGEMENT MISTRAL 7B INSTRUCT")
    print("="*70)
    print(f"\nModèle: {model_id}")
    print(f"Fichier: {filename}")
    print(f"Taille: ~4.37 GB")
    print(f"Destination: {destination}")
    print("\n⚠️  Cela peut prendre 10-30 minutes selon votre connexion...")
    print("\nDémarrage du téléchargement...\n")
    
    try:
        # Télécharger
        downloaded_path = hf_hub_download(
            repo_id=model_id,
            filename=filename,
            local_dir=str(GGUF_DIR),
            local_dir_use_symlinks=False,
            resume_download=True  # Reprend si interrompu
        )
        
        print("\n" + "="*70)
        print("✅ TÉLÉCHARGEMENT TERMINÉ !")
        print("="*70)
        print(f"\nFichier: {downloaded_path}")
        
        # Afficher taille
        size_gb = Path(downloaded_path).stat().st_size / (1024**3)
        print(f"Taille: {size_gb:.2f} GB")
        
        print("\n🎯 Prochaine étape: Tester le modèle")
        print("   python backend/scripts/test_model.py")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Téléchargement interrompu")
        print("   Vous pouvez relancer ce script pour reprendre")
        sys.exit(1)
        
    except Exception as e:
        print(f"\n❌ Erreur lors du téléchargement: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_mistral()
