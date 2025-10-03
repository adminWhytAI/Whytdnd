# 🎲 WhytDD - Dungeons & Dragons Character AI System

**Créez des personnages D&D 5e vivants qui conversent de manière immersive grâce au RAG et modèles GGUF locaux.**

## 🌟 Vue d'Ensemble

WhytDD transforme la création de personnages D&D en une expérience interactive où chaque personnage :
- **Devient véritablement lui-même** (pas juste "joue un rôle")
- **Se souvient de tout** son passé et expériences
- **Évolue avec le temps** (level up, changements, journal)
- **Répond de manière cohérente** grâce au système RAG

## 🏗️ Architecture

### Backend
- **Python 3.10+** avec FastAPI
- **ChromaDB** : Base vectorielle pour mémoire
- **sentence-transformers** : Embeddings multilingues
- **llama-cpp-python** : Interface modèle GGUF local
- **Mistral 7B Instruct** : Génération conversationnelle

### Frontend
- **React 18** + Vite
- **TailwindCSS** : Design médiéval D&D
- **shadcn/ui** : Composants UI
- **React Query** : Gestion API

## 📂 Documentation

- **ARCHITECTURE.md** : Arborescence complète et flux de données
- **TODO.md** : Roadmap détaillée (20 semaines)
- **SETUP.md** : Guide de setup
- **discussion.md** : Décisions d'architecture

## 🚀 Quick Start

### 1. Installation

```bash
# Cloner le projet
git clone <repo>
cd WhytDD

# Installer dépendances Python
pip install -r requirements.txt

# Télécharger Mistral 7B (4.37 GB)
python backend/scripts/download_mistral.py
```

### 2. Tester le Modèle

```bash
python backend/scripts/test_model.py
```

### 3. Vérifier Configuration

```bash
python backend/utils/config.py
```

## 📋 Statut du Projet

**Phase Actuelle** : Phase 0 - Setup Initial

### ✅ Complété
- Structure backend complète
- Configuration modèle (Mistral 7B)
- Utilitaires (config, logger, exceptions)
- TinyLlama pour dev rapide

### 🚧 En Cours
- Installation dépendances Python
- Documentation immersive (Phase 1)

### ⏳ À Venir
- Système RAG complet
- Interface GGUF
- Frontend React
- API REST

## 🎯 Fonctionnalités Clés

### Création de Personnage
- Suivre règles D&D 5e officielles
- 13 races, 12 classes
- Génération stats (3 méthodes)
- Personnalité et background

### Système RAG
- **Base Universelle** : Lore D&D partagé
- **Base Personnage** : Mémoire individuelle
- **Récupération Dynamique** : Seulement infos pertinentes
- **Profil Comportemental** : Stats → Directives narratives

### Conversation Immersive
- Personnage "devient" son rôle
- Mémoire à long terme
- Journal auto-généré
- Évolution temporelle

## 🛠️ Développement

### Structure Projet

```
WhytDD/
├── backend/           # API Python + RAG
├── frontend/          # React webapp
├── models/            # GGUF + embeddings
├── data/              # ChromaDB + personnages
└── Documentation/     # Guides D&D
    ├── Technical/     # Règles (pour système)
    └── Immersive/     # 1ère personne (pour GGUF)
```

### Lancer Tests

```bash
# Test config
python backend/utils/config.py

# Test modèle
python backend/scripts/test_model.py

# Test complet (à venir)
pytest backend/tests/
```

## 📖 Documentation D&D

Le projet inclut une documentation D&D 5e complète :
- Guide démarrage rapide
- Création personnage
- 13 races détaillées
- 12 classes
- Système de jeu
- Combat et magie
- Guide Maître du Donjon

**+ Documentation Immersive** (à créer) :
- Expérience vécue de chaque race/classe
- Perspective 1ère personne
- Pour que le GGUF "devienne" le personnage

## 🤝 Contribution

Voir TODO.md pour la roadmap complète.

**Priorités actuelles** :
1. Documentation immersive (Phase 1)
2. Système RAG (Phase 2-4)
3. Interface GGUF (Phase 5)
4. API REST (Phase 8)
5. Frontend (Phase 9-13)

## 📝 Licence

À définir

## 🙏 Remerciements

- Wizards of the Coast pour D&D 5e
- Mistral AI pour Mistral 7B
- Communauté open-source

---

**Version** : 0.1.0-alpha
**Dernière mise à jour** : 2025-10-04
