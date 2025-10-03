# WhytDD - Complete Project Architecture

## Overview

**WhytDD** is a living D&D 5e character system using RAG (Retrieval-Augmented Generation) and a local GGUF model to create persistent, evolving characters capable of conversing in an immersive manner.

## Technology Stack

### Backend
- **Python 3.10+**
- **FastAPI** - REST API
- **ChromaDB** - Vector database
- **sentence-transformers** - Embeddings generation
- **llama-cpp-python** - GGUF interface
- **Pydantic** - Data validation

### Frontend
- **React 18** + **Vite**
- **TailwindCSS** - Styling
- **shadcn/ui** - UI components
- **React Router** - Navigation
- **Zustand** - State management
- **React Query (TanStack)** - API calls

## Complete Project Directory Structure

```
WhytDD/
├── README.md
├── ARCHITECTURE.md
├── TODO.md
├── discussion.md
├── .gitignore
├── requirements.txt
│
├── gguf/                              [GGUF Models]
│   └── your_model.gguf
│
├── Documentation/
│   ├── Technical/                     [D&D Rules - For system]
│   │   ├── 00_Guide_Demarrage_Rapide.md
│   │   ├── 01_Creation_Personnage.md
│   │   ├── 02_Races.md
│   │   ├── 03_Classes_Resume.md
│   │   ├── 04_Systeme_Jeu.md
│   │   ├── 05_Combat_Magie.md
│   │   ├── 06_Guide_Maitre_Donjon.md
│   │   └── README.md
│   │
│   └── Immersive/                     [First-person experience - For GGUF]
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
│       │   └── ... (12 files)
│       └── Alignments/
│           ├── Living_Lawful_Good.md
│           └── ... (9 alignments)
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
│   ├── character_creator/             [Character generation]
│   │   ├── __init__.py
│   │   ├── creator_logic.py
│   │   │   Classes: CharacterGenerator
│   │   │   Imports: rules_database, uuid, random
│   │   │   Links: → rules_database.json, → behavioral_translator
│   │   ├── behavioral_translator.py
│   │   │   Classes: BehavioralProfileBuilder
│   │   │   Imports: json
│   │   │   Links: → stats_calculator, → rules_database
│   │   ├── stats_calculator.py
│   │   │   Classes: StatsManager, DiceRoller
│   │   │   Imports: random
│   │   └── equipment_manager.py
│   │       Classes: EquipmentBuilder
│   │       Imports: rules_database
│   │
│   ├── rag_engine/                    [RAG System]
│   │   ├── __init__.py
│   │   ├── embeddings/
│   │   │   ├── __init__.py
│   │   │   ├── model.py
│   │   │   │   Classes: EmbeddingModel
│   │   │   │   Imports: sentence_transformers
│   │   │   └── character_embedder.py
│   │   │       Classes: CharacterKnowledgeEmbedder
│   │   │       Imports: model.py
│   │   │       Links: → model.py
│   │   │
│   │   ├── vectorstore/
│   │   │   ├── __init__.py
│   │   │   ├── chromadb_manager.py
│   │   │   │   Classes: ChromaDBManager, UniversalKnowledge, CharacterKnowledge
│   │   │   │   Imports: chromadb
│   │   │   └── query_engine.py
│   │   │       Classes: VectorQueryEngine
│   │   │       Imports: chromadb_manager
│   │   │       Links: → chromadb_manager
│   │   │
│   │   ├── knowledge_builder/
│   │   │   ├── __init__.py
│   │   │   ├── universal_indexer.py
│   │   │   │   Classes: UniversalKnowledgeIndexer
│   │   │   │   Imports: immersive_parser, embeddings
│   │   │   │   Links: → Documentation/Immersive/, → chromadb_manager
│   │   │   ├── character_indexer.py
│   │   │   │   Classes: CharacterKnowledgeIndexer
│   │   │   │   Imports: embeddings, json
│   │   │   │   Links: → chromadb_manager, → behavioral_translator
│   │   │   └── fragment_builder.py
│   │   │       Classes: KnowledgeFragmenter, MetadataEnricher
│   │   │       Imports: datetime
│   │   │
│   │   └── retriever.py
│   │       Classes: RAGRetriever, FragmentPrioritizer
│   │       Imports: query_engine, datetime
│   │       Links: → query_engine, → chromadb_manager
│   │
│   ├── llm_interface/                 [GGUF Interface]
│   │   ├── __init__.py
│   │   ├── model_loader.py
│   │   │   Classes: GGUFModelLoader
│   │   │   Imports: llama_cpp
│   │   ├── prompt_builder.py
│   │   │   Classes: DynamicPromptBuilder, TemplateManager
│   │   │   Imports: jinja2
│   │   │   Links: → retriever, → behavioral_translator
│   │   └── inference.py
│   │       Classes: CharacterConversationEngine
│   │       Imports: model_loader, prompt_builder
│   │       Links: → model_loader, → prompt_builder, → retriever
│   │
│   ├── conversation_manager/          [Conversation management]
│   │   ├── __init__.py
│   │   ├── memory.py
│   │   │   Classes: ConversationMemory, ShortTermMemory, LongTermMemory
│   │   │   Imports: datetime, json
│   │   └── enrichment.py
│   │       Classes: ConversationEnricher, EventExtractor
│   │       Imports: memory
│   │       Links: → character_indexer, → journal_generator
│   │
│   ├── journal_system/                [Journal system]
│   │   ├── __init__.py
│   │   ├── event_detector.py
│   │   │   Classes: EventDetector, EventClassifier
│   │   │   Imports: re
│   │   ├── journal_generator.py
│   │   │   Classes: JournalEntryGenerator
│   │   │   Imports: llm_interface, behavioral_translator
│   │   │   Links: → llm_interface, → behavioral_translator
│   │   └── journal_indexer.py
│   │       Classes: JournalIndexer
│   │       Imports: character_indexer
│   │       Links: → character_indexer
│   │
│   ├── character_evolution/           [Character evolution]
│   │   ├── __init__.py
│   │   ├── level_up.py
│   │   │   Classes: LevelUpManager
│   │   │   Imports: rules_database
│   │   │   Links: → character_indexer, → behavioral_translator
│   │   ├── class_change.py
│   │   │   Classes: ClassChangeHandler
│   │   │   Imports: rules_database
│   │   │   Links: → behavioral_translator, → timeline_manager
│   │   └── timeline_manager.py
│   │       Classes: CharacterTimeline, PhaseManager
│   │       Imports: datetime, json
│   │
│   ├── api/                           [REST API]
│   │   ├── __init__.py
│   │   ├── main.py
│   │   │   Imports: fastapi, uvicorn, routes
│   │   │   App: FastAPI
│   │   │   Links: → routes
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── character_routes.py
│   │   │   │   Endpoints: POST /character/create, GET /character/{id}
│   │   │   │   Imports: character_creator, character_indexer
│   │   │   │   Links: → character_creator, → character_indexer
│   │   │   ├── chat_routes.py
│   │   │   │   Endpoints: POST /chat, GET /chat/history/{id}
│   │   │   │   Imports: inference, conversation_manager
│   │   │   │   Links: → inference, → conversation_manager
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
├── data/                              [Persistent data]
│   ├── chromadb/
│   │   ├── universal/                 [Universal D&D database]
│   │   │   └── chroma.sqlite3
│   │   └── characters/                [Individual databases]
│   │       ├── {character_id_1}/
│   │       └── {character_id_2}/
│   │
│   ├── rules_database.json            [Parsed D&D rules]
│   │   Structure: { races: {}, classes: {}, mechanics: {} }
│   │
│   └── characters/                    [Character data]
│       ├── {character_id}/
│       │   ├── core_identity.json
│       │   ├── behavioral_profile.json
│       │   ├── stats.json
│       │   ├── timeline.json
│       │   └── journal/
│       │       ├── entry_001.json
│       │       └── entry_002.json
│       └── index.json                 [Character index]
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
        │   Links: → pages
        │
        ├── components/
        │   ├── character/
        │   │   ├── CharacterSheet.jsx
        │   │   │   Imports: Card, StatsDisplay, AbilityCard
        │   │   │   Links: → useCharacter hook
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
        │   │   │   Links: → characterApi.getRaces
        │   │   ├── ClassSelector.jsx
        │   │   │   State: selectedClass
        │   │   ├── StatsRoller.jsx
        │   │   │   Hook: useDiceRoller
        │   │   │   Links: → utils/diceRoller
        │   │   ├── BackgroundForm.jsx
        │   │   │   State: personality traits
        │   │   └── CreationStepper.jsx
        │   │       State: currentStep, formData
        │   │       Links: → all creator components
        │   │
        │   ├── chat/
        │   │   ├── ChatInterface.jsx
        │   │   │   Hook: useChat
        │   │   │   Links: → chatApi, → MessageBubble
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
        │   │   │   Links: → journalApi
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
        │   │   Links: → characterApi.list
        │   ├── CharacterCreator.jsx
        │   │   Component: CreationStepper
        │   │   Links: → characterApi.create
        │   ├── CharacterView.jsx
        │   │   Components: CharacterSheet, ChatInterface
        │   │   Links: → characterApi, → chatApi
        │   └── JournalPage.jsx
        │       Component: JournalViewer
        │
        ├── hooks/
        │   ├── useCharacter.js
        │   │   Returns: character, isLoading, error
        │   │   Links: → React Query, → characterApi
        │   ├── useChat.js
        │   │   Returns: messages, sendMessage, isTyping
        │   │   Links: → chatStore, → chatApi
        │   └── useDiceRoller.js
        │       Returns: roll, result, isRolling
        │       Links: → utils/diceRoller
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
        │   │   Links: → backend/api/character_routes
        │   ├── chatApi.js
        │   │   Functions: sendMessage, getHistory
        │   │   Links: → backend/api/chat_routes
        │   └── journalApi.js
        │       Functions: getJournal, getTimeline
        │       Links: → backend/api/journal_routes
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

## Main Data Flow

### 1. Character Creation

```
Frontend (CharacterCreator)
  ↓ FormData
API (POST /character/create)
  ↓
CharacterGenerator
  ├→ RuleParser (loads races/classes)
  ├→ StatsManager (calculates stats)
  └→ BehavioralProfileBuilder (translates to directives)
  ↓
CharacterKnowledgeIndexer
  ├→ Parse character data into fragments
  ├→ Generate embeddings
  └→ Store in ChromaDB (character collection)
  ↓
Response: { character_id, character_data }
  ↓
Frontend (redirect to CharacterView)
```

### 2. Conversation

```
Frontend (ChatInterface)
  ↓ User message
API (POST /chat)
  ↓
RAGRetriever
  ├→ Transform message into embedding
  ├→ Query ChromaDB universal (D&D lore)
  ├→ Query ChromaDB character (experiences)
  └→ Prioritize fragments (critical always included)
  ↓
DynamicPromptBuilder
  ├→ Behavioral profile (always included)
  ├→ Relevant fragments
  ├→ Conversation history
  └→ Build complete prompt
  ↓
GGUFModelLoader
  ├→ Load model
  └→ Generate response
  ↓
ConversationEnricher (optional)
  ├→ Detect important events
  └→ Create new fragments
  ↓
Response: { character_name, response, timestamp }
  ↓
Frontend (display message)
```

### 3. Journal Generation

```
EventDetector (after conversation)
  ↓ Event detected (e.g., "killed dragon")
JournalGenerator
  ├→ Retrieve behavioral profile
  ├→ Build special prompt
  └→ GGUF generates journal entry
  ↓
JournalIndexer
  ├→ Create journal fragment
  ├→ Generate embedding
  └→ Store in ChromaDB character
  ↓
Timeline updated
```

## Critical Inter-Module Links

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
rag_engine/knowledge_builder (enrichment loop)
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

## Required Configuration

### Backend

**requirements.txt**:
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

**package.json**:
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

## Entry Points

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

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

**Version**: 1.0.0
**Last Updated**: 2025-10-04
