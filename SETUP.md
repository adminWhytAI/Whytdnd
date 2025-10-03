# WhytDD - Guide de Setup

## ✅ État Actuel du Setup

### Complété
- ✅ Arborescence backend créée
- ✅ Structure models/ créée
- ✅ TinyLlama déplacé dans models/gguf/
- ✅ Configuration (config.py, logger.py, exceptions.py)
- ✅ .gitignore créé
- ✅ requirements.txt mis à jour
- ✅ Installation dépendances Python en cours

### En Attente
- ⏳ Téléchargement Mistral-7B-Instruct
- ⏳ Setup frontend (React + Vite)
- ⏳ Documentation immersive

## 🚀 Prochaines Étapes

### 1. Vérifier Installation Dépendances

Attendre que l'installation se termine, puis vérifier :

```bash
python backend/utils/config.py
```

Devrait afficher la configuration et vérifier que tout est OK.

### 2. Télécharger Mistral 7B (Recommandé)

**Option A : Téléchargement Manuel**
1. Aller sur https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
2. Télécharger `mistral-7b-instruct-v0.2.Q4_K_M.gguf` (4.37 GB)
3. Placer dans `models/gguf/`

**Option B : Via Script Python**

```bash
python backend/scripts/download_mistral.py
```

### 3. Tester le Modèle

```bash
python backend/scripts/test_model.py
```

### 4. Créer Documentation Immersive (Phase 1)

Créer les fichiers dans `Documentation/Immersive/` :
- Races/ : Being_A_Dwarf_Mountain.md, etc.
- Classes/ : Being_A_Fighter.md, etc.
- Stats/ : Having_High_Strength.md, etc.
- Alignments/ : Living_Lawful_Good.md, etc.

Voir TODO.md Phase 1 pour la liste complète.

## 📂 Structure Actuelle

```
WhytDD/
├── backend/              ✅ Créé
│   ├── knowledge_parser/
│   ├── character_creator/
│   ├── rag_engine/
│   ├── llm_interface/
│   ├── api/
│   └── utils/            ✅ Config créée
│
├── models/               ✅ Créé
│   ├── gguf/
│   │   └── tinyllama-1.1b-chat-q4_k_m.gguf  ✅
│   └── config/
│       └── model_config.json  ✅
│
├── Documentation/        ✅ Existe
│   ├── Technical/        ✅ Guides D&D
│   └── Immersive/        ✅ Structure créée
│
└── data/                 ✅ Créé
    ├── chromadb/
    └── characters/
```

## ⚙️ Configuration Actuelle

**Modèle Production** : Mistral-7B-Instruct-v0.2 (à télécharger)
**Modèle Dev** : TinyLlama-1.1B (déjà présent)

Pour basculer entre les deux, éditer `models/config/model_config.json` :
- Mistral 7B : Meilleure qualité, plus lent
- TinyLlama : Rapide, qualité limitée

## 🐛 Résolution Problèmes

### Erreur "Modèle non trouvé"
→ Télécharger Mistral 7B ou utiliser TinyLlama temporairement

### Erreur "ChromaDB"
→ Installation en cours, patienter

### Erreur "llama-cpp-python"
→ Installation en cours, si échec :
```bash
pip install llama-cpp-python --force-reinstall
```

## 📝 Notes

- Les modèles GGUF sont dans .gitignore (trop gros)
- TinyLlama OK pour dev, Mistral 7B pour prod
- Context Mistral : 8192 tokens vs TinyLlama : 2048 tokens

---

**Voir TODO.md pour la roadmap complète** 🎯
