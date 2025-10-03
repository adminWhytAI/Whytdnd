# WhytDD - Architecture Complète du Projet

## Vue d'Ensemble

**WhytDD** est un système de personnages D&D 5e vivants utilisant RAG (Retrieval-Augmented Generation) et un modèle GGUF local pour créer des personnages persistants, évolutifs et capables de converser de manière immersive.

## Stack Technologique

### Backend
- **Python 3.10+**
- **FastAPI** - API REST
- **ChromaDB** - Base de données vectorielle
- **sentence-transformers** - Génération embeddings
- **llama-cpp-python** - Interface GGUF
- **Pydantic** - Validation données

### Frontend
- **React 18** + **Vite**
- **TailwindCSS** - Styling
- **shadcn/ui** - Composants UI
- **React Router** - Navigation
- **Zustand** - State management
- **React Query (TanStack)** - API calls

## Arborescence Complète du Projet

```
WhytDD/
├── README.md
├── ARCHITECTURE.md
├── TODO.md
├── discussion.md
├── .gitignore
├── requirements.txt
│
├── gguf/                              [Modèles GGUF]
│   └── your_model.gguf
│
├── Documentation/
│   ├── Technical/                     [Règles D&D - Pour système]
│   │   ├── 00_Guide_Demarrage_Rapide.md
│   │   ├── 01_Creation_Personnage.md
│   │   ├── 02_Races.md
│   │   ├── 03_Classes_Resume.md
│   │   ├── 04_Systeme_Jeu.md
│   │   ├── 05_Combat_Magie.md
│   │   ├── 06_Guide_Maitre_Donjon.md
│   │   └── README.md
│   │
│   └── Immersive/                     [Expérience 1ère personne - Pour GGUF]
│       ├── Races/
│       │   ├── Being_A_Dwarf_Mountain.md
│       │   ├── Being_An_Elf_High.md
│       │   └── ... (13 races)
│       ├── Classes/
│       │   ├── Being_A_Fighter.md
│       │   ├── Being_A_Wizard.md
│       │   └── ... (12 classes)
│       ├── Stats/
│       │   ├── Having_High_Strength.md
│       │   ├── Having_Low_Intelligence.md
│       │   └── ... (12 fichiers)
│       └── Alignments/
│           ├── Living_Lawful_Good.md
│           └── ... (9 alignements)
│
├── backend/
│   ├── __init__.py
│   │
│   ├── knowledge_parser/              [Parse documentation]
│   │   ├── __init__.py
│   │   ├── rule_parser.py
│   │   │   Classes: RaceParser, ClassParser, RuleExtractor
│   │   │   Imports: pathlib, json, re
│   │   ├── immersive_parser.py
│   │   │   Classes: ImmersiveDocParser, FragmentExtractor
│   │   │   Imports: pathlib, markdown
│   │   └── data_validator.py
│   │       Classes: RuleValidator
│   │       Imports: pydantic
│   │
│   ├── character_creator/             [Génération personnage]
│   │   ├── __init__.py
│   │   ├── creator_logic.py
│   │   │   Classes: CharacterGenerator
│   │   │   Imports: rules_database, uuid, random
│   │   │   Liaisons: → rules_database.json, → behavioral_translator
│   │   ├── behavioral_translator.py
│   │   │   Classes: BehavioralProfileBuilder
│   │   │   Imports: json
│   │   │   Liaisons: → stats_calculator, → rules_database
│   │   ├── stats_calculator.py
│   │   │   Classes: StatsManager, DiceRoller
│   │   │   Imports: random
│   │   └── equipment_manager.py
│   │       Classes: EquipmentBuilder
│   │       Imports: rules_database
│   │
│   ├── rag_engine/                    [Système RAG]
│   │   ├── __init__.py
│   │   ├── embeddings/
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   │   Classes: EmbeddingModel
│   │   │   │   Imports: sentence_transformers
│   │   │   └── character_embedder.py
│   │   │       Classes: CharacterKnowledgeEmbedder
│   │   │       Imports: model.py
│   │   │       Liaisons: → model.py
│   │   │
│   │   ├── vectorstore/
│   │   │   ├── __init__.py
│   │   │   ├── chromadb_manager.py
│   │   │   │   Classes: ChromaDBManager, UniversalKnowledge, CharacterKnowledge
│   │   │   │   Imports: chromadb
│   │   │   └── query_engine.py
│   │   │       Classes: VectorQueryEngine
│   │   │       Imports: chromadb_manager
│   │   │       Liaisons: → chromadb_manager
│   │   │
│   │   ├── knowledge_builder/
│   │   │   ├── __init__.py
│   │   │   ├── universal_indexer.py
│   │   │   │   Classes: UniversalKnowledgeIndexer
│   │   │   │   Imports: immersive_parser, embeddings
│   │   │   │   Liaisons: → Documentation/Immersive/, → chromadb_manager
│   │   │   ├── character_indexer.py
│   │   │   │   Classes: CharacterKnowledgeIndexer
│   │   │   │   Imports: embeddings, json
│   │   │   │   Liaisons: → chromadb_manager, → behavioral_translator
│   │   │   └── fragment_builder.py
│   │   │       Classes: KnowledgeFragmenter, MetadataEnricher
│   │   │       Imports: datetime
│   │   │
│   │   └── retriever.py
│   │       Classes: RAGRetriever, FragmentPrioritizer
│   │       Imports: query_engine, datetime
│   │       Liaisons: → query_engine, → chromadb_manager
│   │
│   ├── llm_interface/                 [Interface GGUF]
│   │   ├── __init__.py
│   │   ├── model_loader.py
│   │   │   Classes: GGUFModelLoader
│   │   │   Imports: llama_cpp
│   │   ├── prompt_builder.py
│   │   │   Classes: DynamicPromptBuilder, TemplateManager
│   │   │   Imports: jinja2
│   │   │   Liaisons: → retriever, → behavioral_translator
│   │   └── inference.py
│   │       Classes: CharacterConversationEngine
│   │       Imports: model_loader, prompt_builder
│   │       Liaisons: → model_loader, → prompt_builder, → retriever
│   │
│   ├── conversation_manager/          [Gestion conversation]
│   │   ├── __init__.py
│   │   ├── memory.py
│   │   │   Classes: ConversationMemory, ShortTermMemory, LongTermMemory
│   │   │   Imports: datetime, json
│   │   └── enrichment.py
│   │       Classes: ConversationEnricher, EventExtractor
│   │       Imports: memory
│   │       Liaisons: → character_indexer, → journal_generator
│   │
│   ├── journal_system/                [Système journal]
│   │   ├── __init__.py
│   │   ├── event_detector.py
│   │   │   Classes: EventDetector, EventClassifier
│   │   │   Imports: re
│   │   ├── journal_generator.py
│   │   │   Classes: JournalEntryGenerator
│   │   │   Imports: llm_interface, behavioral_translator
│   │   │   Liaisons: → llm_interface, → behavioral_translator
│   │   └── journal_indexer.py
│   │       Classes: JournalIndexer
│   │       Imports: character_indexer
│   │       Liaisons: → character_indexer
│   │
│   ├── character_evolution/           [Évolution personnage]
│   │   ├── __init__.py
│   │   ├── level_up.py
│   │   │   Classes: LevelUpManager
│   │   │   Imports: rules_database
│   │   │   Liaisons: → character_indexer, → behavioral_translator
│   │   ├── class_change.py
│   │   │   Classes: ClassChangeHandler
│   │   │   Imports: rules_database
│   │   │   Liaisons: → behavioral_translator, → timeline_manager
│   │   └── timeline_manager.py
│   │       Classes: CharacterTimeline, PhaseManager
│   │       Imports: datetime, json
│   │
│   ├── api/                           [API REST]
│   │   ├── __init__.py
│   │   ├── main.py
│   │   │   Imports: fastapi, uvicorn, routes
│   │   │   App: FastAPI
│   │   │   Liaisons: → routes
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── character_routes.py
│   │   │   │   Endpoints: POST /character/create, GET /character/{id}
│   │   │   │   Imports: character_creator, character_indexer
│   │   │   │   Liaisons: → character_creator, → character_indexer
│   │   │   ├── chat_routes.py
│   │   │   │   Endpoints: POST /chat, GET /chat/history/{id}
│   │   │   │   Imports: inference, conversation_manager
│   │   │   │   Liaisons: → inference, → conversation_manager
│   │   │   ├── journal_routes.py
│   │   │   │   Endpoints: GET /journal/{id}, POST /journal/{id}/entry
│   │   │   │   Imports: journal_system
│   │   │   └── evolution_routes.py
│   │   │       Endpoints: POST /character/{id}/levelup
│   │   │       Imports: character_evolution
│   │   │
│   │   └── models/                    [Pydantic models]
│   │       ├── __init__.py
│   │       ├── character_schema.py
│   │       │   Models: CharacterCreate, CharacterResponse, Stats
│   │       ├── chat_schema.py
│   │       │   Models: ChatRequest, ChatResponse, Message
│   │       └── journal_schema.py
│   │           Models: JournalEntry, Timeline
│   │
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│       │   Config: DATABASE_PATH, MODEL_PATH, API_CONFIG
│       ├── logger.py
│       │   Setup: logging configuration
│       └── exceptions.py
│           Classes: Custom exceptions
│
├── data/                              [Données persistantes]
│   ├── chromadb/
│   │   ├── universal/                 [Base universelle D&D]
│   │   │   └── chroma.sqlite3
│   │   └── characters/                [Bases individuelles]
│   │       ├── {character_id_1}/
│   │       └── {character_id_2}/
│   │
│   ├── rules_database.json            [Règles D&D parsées]
│   │   Structure: { races: {}, classes: {}, mechanics: {} }
│   │
│   └── characters/                    [Données personnages]
│       ├── {character_id}/
│       │   ├── core_identity.json
│       │   ├── behavioral_profile.json
│       │   ├── stats.json
│       │   ├── timeline.json
│       │   └── journal/
│       │       ├── entry_001.json
│       │       └── entry_002.json
│       └── index.json                 [Index personnages]
│
└── frontend/
    ├── package.json
    ├── vite.config.js
    ├── tailwind.config.js
    ├── index.html
    │
    ├── public/
    │   ├── dice/
    │   ├── icons/
    │   └── textures/
    │       └── parchment-texture.png
    │
    └── src/
        ├── main.jsx
        │   Imports: React, ReactDOM, App, globals.css
        ├── App.jsx
        │   Imports: Router, QueryClient, routes
        │   Liaisons: → pages
        │
        ├── components/
        │   ├── character/
        │   │   ├── CharacterSheet.jsx
        │   │   │   Imports: Card, StatsDisplay, AbilityCard
        │   │   │   Liaisons: → useCharacter hook
        │   │   ├── StatsDisplay.jsx
        │   │   │   Props: stats object
        │   │   ├── AbilityCard.jsx
        │   │   │   Props: ability object
        │   │   └── InventoryList.jsx
        │   │       Props: items array
        │   │
        │   ├── creator/
        │   │   ├── RaceSelector.jsx
        │   │   │   State: selectedRace
        │   │   │   Liaisons: → characterApi.getRaces
        │   │   ├── ClassSelector.jsx
        │   │   │   State: selectedClass
        │   │   ├── StatsRoller.jsx
        │   │   │   Hook: useDiceRoller
        │   │   │   Liaisons: → utils/diceRoller
        │   │   ├── BackgroundForm.jsx
        │   │   │   State: personality traits
        │   │   └── CreationStepper.jsx
        │   │       State: currentStep, formData
        │   │       Liaisons: → all creator components
        │   │
        │   ├── chat/
        │   │   ├── ChatInterface.jsx
        │   │   │   Hook: useChat
        │   │   │   Liaisons: → chatApi, → MessageBubble
        │   │   ├── MessageBubble.jsx
        │   │   │   Props: message, role
        │   │   ├── TypingIndicator.jsx
        │   │   │   Animation: dots
        │   │   └── CharacterAvatar.jsx
        │   │       Props: character
        │   │
        │   ├── journal/
        │   │   ├── JournalViewer.jsx
        │   │   │   Hook: useJournal
        │   │   │   Liaisons: → journalApi
        │   │   ├── JournalEntry.jsx
        │   │   │   Props: entry object
        │   │   └── Timeline.jsx
        │   │       Props: phases array
        │   │
        │   └── ui/                    [shadcn/ui]
        │       ├── button.jsx
        │       ├── card.jsx
        │       ├── dialog.jsx
        │       ├── form.jsx
        │       └── tabs.jsx
        │
        ├── pages/
        │   ├── Home.jsx
        │   │   Hook: useCharacterList
        │   │   Liaisons: → characterApi.list
        │   ├── CharacterCreator.jsx
        │   │   Component: CreationStepper
        │   │   Liaisons: → characterApi.create
        │   ├── CharacterView.jsx
        │   │   Components: CharacterSheet, ChatInterface
        │   │   Liaisons: → characterApi, → chatApi
        │   └── JournalPage.jsx
        │       Component: JournalViewer
        │
        ├── hooks/
        │   ├── useCharacter.js
        │   │   Returns: character, isLoading, error
        │   │   Liaisons: → React Query, → characterApi
        │   ├── useChat.js
        │   │   Returns: messages, sendMessage, isTyping
        │   │   Liaisons: → chatStore, → chatApi
        │   └── useDiceRoller.js
        │       Returns: roll, result, isRolling
        │       Liaisons: → utils/diceRoller
        │
        ├── stores/
        │   ├── characterStore.js
        │   │   Zustand: currentCharacter, setCharacter
        │   └── chatStore.js
        │       Zustand: messages, addMessage
        │
        ├── api/
        │   ├── client.js
        │   │   Axios instance: baseURL, interceptors
        │   ├── characterApi.js
        │   │   Functions: create, get, list, update
        │   │   Liaisons: → backend/api/character_routes
        │   ├── chatApi.js
        │   │   Functions: sendMessage, getHistory
        │   │   Liaisons: → backend/api/chat_routes
        │   └── journalApi.js
        │       Functions: getJournal, getTimeline
        │       Liaisons: → backend/api/journal_routes
        │
        ├── utils/
        │   ├── statCalculator.js
        │   │   Functions: calculateModifier, calculateHP
        │   ├── diceRoller.js
        │   │   Functions: roll, rollStats
        │   └── validators.js
        │       Functions: validateCharacter, validateStats
        │
        └── styles/
            └── globals.css
                Tailwind: @layer base, components, utilities
                Custom: parchment-bg, leather-texture, etc.
```

## Flux de Données Principal

### 1. Création de Personnage

```
Frontend (CharacterCreator)
  ↓ FormData
API (POST /character/create)
  ↓
CharacterGenerator
  ├→ RuleParser (charges races/classes)
  ├→ StatsManager (calcule stats)
  └→ BehavioralProfileBuilder (traduit en directives)
  ↓
CharacterKnowledgeIndexer
  ├→ Parse character data en fragments
  ├→ Génère embeddings
  └→ Stocke dans ChromaDB (collection personnage)
  ↓
Response: { character_id, character_data }
  ↓
Frontend (redirect to CharacterView)
```

### 2. Conversation

```
Frontend (ChatInterface)
  ↓ Message utilisateur
API (POST /chat)
  ↓
RAGRetriever
  ├→ Transforme message en embedding
  ├→ Query ChromaDB universal (lore D&D)
  ├→ Query ChromaDB character (expériences)
  └→ Priorise fragments (critical toujours inclus)
  ↓
DynamicPromptBuilder
  ├→ Behavioral profile (toujours inclus)
  ├→ Fragments pertinents
  ├→ Historique conversation
  └→ Construit prompt complet
  ↓
GGUFModelLoader
  ├→ Charge modèle
  └→ Génère réponse
  ↓
ConversationEnricher (optionnel)
  ├→ Détecte événements importants
  └→ Crée nouveaux fragments
  ↓
Response: { character_name, response, timestamp }
  ↓
Frontend (affiche message)
```

### 3. Génération Journal

```
EventDetector (après conversation)
  ↓ Événement détecté (ex: "tué dragon")
JournalGenerator
  ├→ Récupère behavioral profile
  ├→ Construit prompt spécial
  └→ GGUF génère entrée journal
  ↓
JournalIndexer
  ├→ Crée fragment journal
  ├→ Génère embedding
  └→ Stocke dans ChromaDB character
  ↓
Timeline mise à jour
```

## Liaisons Inter-Modules Critiques

### Backend

```
knowledge_parser
  ↓ rules_database.json
character_creator ← rules_database
  ↓ behavioral_profile.json
rag_engine/knowledge_builder ← behavioral_profile
  ↓ ChromaDB collections
rag_engine/retriever ← ChromaDB
  ↓ fragments
llm_interface/prompt_builder ← fragments + behavioral_profile
  ↓ prompt
llm_interface/inference ← GGUF model
  ↓ response
conversation_manager ← response
  ↓ new fragments
rag_engine/knowledge_builder (boucle enrichissement)
```

### Frontend → Backend

```
Frontend Components
  ↓
API Client Functions
  ↓ HTTP Requests
Backend API Routes
  ↓
Backend Services
  ↓ Data
API Routes
  ↓ HTTP Response
API Client
  ↓
React Query Cache
  ↓
Components (re-render)
```

## Configuration Requise

### Backend

**requirements.txt** :
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
chromadb==0.4.18
sentence-transformers==2.2.2
llama-cpp-python==0.2.20
pydantic==2.5.0
python-multipart==0.0.6
jinja2==3.1.2
markdown==3.5.1
```

### Frontend

**package.json** :
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "@tanstack/react-query": "^5.12.0",
    "zustand": "^4.4.7",
    "axios": "^1.6.2",
    "lucide-react": "^0.294.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "tailwindcss": "^3.3.6",
    "@vitejs/plugin-react": "^4.2.0"
  }
}
```

## Points d'Entrée

### Backend
```bash
cd backend
python -m uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## URLs

- **Frontend** : http://localhost:5173
- **Backend API** : http://localhost:8000
- **API Docs** : http://localhost:8000/docs

---

**Version** : 1.0.0
**Last Updated** : 2025-10-04
