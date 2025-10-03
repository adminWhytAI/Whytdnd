"""
Script de test du modèle GGUF (Mistral 7B ou TinyLlama)
"""
import sys
from pathlib import Path

# Ajouter backend au path
sys.path.insert(0, str(Path(__file__).parent.parent))

def test_model():
    """Test le chargement et la génération du modèle GGUF"""
    
    print("="*70)
    print("🧪 TEST MODÈLE GGUF - WhytDD")
    print("="*70)
    
    # Importer config
    try:
        from utils.config import (
            GGUF_MODEL_PATH, 
            CONTEXT_SIZE, 
            N_THREADS,
            N_GPU_LAYERS,
            GGUF_PARAMS,
            verify_setup
        )
    except Exception as e:
        print(f"\n❌ Erreur import config: {e}")
        print("\nVérifiez que models/config/model_config.json existe")
        return
    
    # Vérifier setup
    print("\n📋 Vérification configuration...")
    valid, messages = verify_setup()
    for msg in messages:
        print(f"   {msg}")
    
    if not valid:
        print("\n❌ Setup incomplet. Voir messages ci-dessus.")
        return
    
    # Afficher infos modèle
    print(f"\n🤖 Modèle GGUF:")
    print(f"   Path: {GGUF_MODEL_PATH}")
    
    if GGUF_MODEL_PATH.exists():
        size_gb = GGUF_MODEL_PATH.stat().st_size / (1024**3)
        print(f"   Taille: {size_gb:.2f} GB")
    else:
        print(f"   ❌ FICHIER NON TROUVÉ")
        print(f"\n   Pour télécharger Mistral 7B:")
        print(f"   python backend/scripts/download_mistral.py")
        return
    
    print(f"   Context size: {CONTEXT_SIZE}")
    print(f"   Threads: {N_THREADS}")
    print(f"   GPU Layers: {N_GPU_LAYERS}")
    
    # Charger modèle
    print(f"\n🔄 Chargement du modèle...")
    print(f"   (Peut prendre 30-60 secondes...)")
    
    try:
        from llama_cpp import Llama
        
        model = Llama(
            model_path=str(GGUF_MODEL_PATH),
            n_ctx=CONTEXT_SIZE,
            n_threads=N_THREADS,
            n_gpu_layers=N_GPU_LAYERS,
            verbose=False
        )
        
        print(f"   ✅ Modèle chargé avec succès !")
        
    except ImportError:
        print(f"\n❌ llama-cpp-python n'est pas installé")
        print(f"   Installation: pip install llama-cpp-python")
        return
    except Exception as e:
        print(f"\n❌ Erreur chargement modèle: {e}")
        return
    
    # Test génération simple
    print(f"\n🧪 Test 1 : Génération Simple")
    print("-"*70)
    
    prompt = """[INST] Tu es Bruenor, un nain des montagnes guerrier bourru mais loyal.

Utilisateur: Bonjour Bruenor, qui es-tu ?
[/INST]"""
    
    print("Prompt:")
    print(prompt)
    print("\nGénération...")
    
    try:
        response = model(
            prompt,
            max_tokens=GGUF_PARAMS['max_tokens'],
            temperature=GGUF_PARAMS['temperature'],
            top_p=GGUF_PARAMS['top_p'],
            top_k=GGUF_PARAMS['top_k'],
            repeat_penalty=GGUF_PARAMS['repeat_penalty'],
            stop=["User:", "\n[INST]", "###"]
        )
        
        generated_text = response['choices'][0]['text'].strip()
        
        print("\n" + "="*70)
        print("💬 RÉPONSE GÉNÉRÉE:")
        print("="*70)
        print(generated_text)
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ Erreur génération: {e}")
        return
    
    # Test 2 : Avec contexte émotionnel
    print(f"\n\n🧪 Test 2 : Réponse avec Contexte Émotionnel")
    print("-"*70)
    
    prompt2 = """[INST] Tu es Bruenor, un nain guerrier.

Contexte : Ton clan a été chassé de Mithral Hall par des orques il y a 200 ans.
Comportement : Tu détestes les orques de manière viscérale.

Utilisateur: Que penses-tu des orques ?
[/INST]"""
    
    print("Génération...")
    
    try:
        response2 = model(
            prompt2,
            max_tokens=200,
            temperature=0.9,  # Plus de créativité
            top_p=0.9,
            stop=["User:", "\n[INST]"]
        )
        
        generated_text2 = response2['choices'][0]['text'].strip()
        
        print("\n" + "="*70)
        print("💬 RÉPONSE GÉNÉRÉE:")
        print("="*70)
        print(generated_text2)
        print("="*70)
        
    except Exception as e:
        print(f"\n❌ Erreur génération: {e}")
        return
    
    # Résumé
    print("\n\n" + "="*70)
    print("✅ TESTS TERMINÉS AVEC SUCCÈS")
    print("="*70)
    print("\n📊 Résumé:")
    print(f"   • Modèle: {GGUF_MODEL_PATH.name}")
    print(f"   • Chargement: OK")
    print(f"   • Génération: OK")
    print(f"   • Roleplay: OK")
    print("\n🎯 Le modèle est prêt pour WhytDD !")
    print("\n📝 Prochaine étape: Créer la documentation immersive")
    print("   Voir TODO.md Phase 1")

if __name__ == "__main__":
    test_model()
