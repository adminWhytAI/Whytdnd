# 🎲 WhytDD - Dungeons & Dragons Character AI System

**Create living D&D 5e characters that converse immersively using RAG and local GGUF models.**

## 🌟 Overview

WhytDD transforms D&D character creation into an interactive experience where each character:
- **Truly becomes themselves** (not just "plays a role")
- **Remembers everything** from their past and experiences
- **Evolves over time** (level up, changes, journal)
- **Responds consistently** thanks to the RAG system

## 🏗️ Architecture

### Backend
- **Python 3.10+** with FastAPI
- **ChromaDB**: Vector database for memory
- **sentence-transformers**: Multilingual embeddings
- **llama-cpp-python**: Local GGUF model interface
- **Mistral 7B Instruct**: Conversational generation

### Frontend
- **React 18** + Vite
- **TailwindCSS**: Medieval D&D design
- **shadcn/ui**: UI components
- **React Query**: API management

## 📂 Documentation

- **ARCHITECTURE.md**: Complete directory structure and data flows
- **TODO.md**: Detailed roadmap (20 weeks)
- **SETUP.md**: Setup guide
- **discussion.md**: Architecture decisions

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the project
git clone <repo>
cd WhytDD

# Install Python dependencies
pip install -r requirements.txt

# Download Mistral 7B (4.37 GB)
python backend/scripts/download_mistral.py
```

### 2. Test the Model

```bash
python backend/scripts/test_model.py
```

### 3. Verify Configuration

```bash
python backend/utils/config.py
```

## 📋 Project Status

**Current Phase**: Phase 0 - Initial Setup

### ✅ Completed
- Complete backend structure
- Model configuration (Mistral 7B)
- Utilities (config, logger, exceptions)
- TinyLlama for quick dev

### 🚧 In Progress
- Python dependencies installation
- Immersive documentation (Phase 1)

### ⏳ Upcoming
- Complete RAG system
- GGUF interface
- React frontend
- REST API

## 🎯 Key Features

### Character Creation
- Follow official D&D 5e rules
- 13 races, 12 classes
- Stats generation (3 methods)
- Personality and background

### RAG System
- **Universal Database**: Shared D&D lore
- **Character Database**: Individual memory
- **Dynamic Retrieval**: Only relevant info
- **Behavioral Profile**: Stats → Narrative directives

### Immersive Conversation
- Character "becomes" their role
- Long-term memory
- Auto-generated journal
- Temporal evolution

## 🛠️ Development

### Project Structure

```
WhytDD/
├── backend/           # Python API + RAG
├── frontend/          # React webapp
├── models/            # GGUF + embeddings
├── data/              # ChromaDB + characters
└── Documentation/     # D&D guides
    ├── Technical/     # Rules (for system)
    └── Immersive/     # First-person (for GGUF)
```

### Run Tests

```bash
# Test config
python backend/utils/config.py

# Test model
python backend/scripts/test_model.py

# Complete test (coming)
pytest backend/tests/
```

## 📖 D&D Documentation

The project includes complete D&D 5e documentation:
- Quick start guide
- Character creation
- 13 detailed races
- 12 classes
- Game system
- Combat and magic
- Dungeon Master's guide

**+ Immersive Documentation** (to create):
- Lived experience of each race/class
- First-person perspective
- For GGUF to "become" the character

## 🤝 Contribution

See TODO.md for complete roadmap.

**Current priorities**:
1. Immersive documentation (Phase 1)
2. RAG system (Phase 2-4)
3. GGUF interface (Phase 5)
4. REST API (Phase 8)
5. Frontend (Phase 9-13)

## 📝 License

To be defined

## 🙏 Acknowledgments

- Wizards of the Coast for D&D 5e
- Mistral AI for Mistral 7B
- Open-source community

---

**Version**: 0.1.0-alpha
**Last updated**: 2025-10-04
