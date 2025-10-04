# WhytDD - Setup Guide

## ✅ Current Setup Status

### Completed
- ✅ Backend directory structure created
- ✅ models/ structure created
- ✅ TinyLlama moved to models/gguf/
- ✅ Configuration (config.py, logger.py, exceptions.py)
- ✅ .gitignore created
- ✅ requirements.txt updated
- ✅ Python dependencies installation in progress

### Pending
- ⏳ Mistral-7B-Instruct download
- ⏳ Frontend setup (React + Vite)
- ⏳ Immersive documentation

## 🚀 Next Steps

### 1. Verify Dependencies Installation

Wait for installation to complete, then verify:

```bash
python backend/utils/config.py
```

Should display the configuration and verify everything is OK.

### 2. Download Mistral 7B (Recommended)

**Option A: Manual Download**
1. Go to https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF
2. Download `mistral-7b-instruct-v0.2.Q4_K_M.gguf` (4.37 GB)
3. Place in `models/gguf/`

**Option B: Via Python Script**

```bash
python backend/scripts/download_mistral.py
```

### 3. Test the Model

```bash
python backend/scripts/test_model.py
```

### 4. Create Immersive Documentation (Phase 1)

Create files in `Documentation/Immersive/`:
- Races/: Being_A_Dwarf_Mountain.md, etc.
- Classes/: Being_A_Fighter.md, etc.
- Stats/: Having_High_Strength.md, etc.
- Alignments/: Living_Lawful_Good.md, etc.

See TODO.md Phase 1 for complete list.

## 📂 Current Structure

```
WhytDD/
├── backend/              ✅ Created
│   ├── knowledge_parser/
│   ├── character_creator/
│   ├── rag_engine/
│   ├── llm_interface/
│   ├── api/
│   └── utils/            ✅ Config created
│
├── models/               ✅ Created
│   ├── gguf/
│   │   └── tinyllama-1.1b-chat-q4_k_m.gguf  ✅
│   └── config/
│       └── model_config.json  ✅
│
├── Documentation/        ✅ Exists
│   ├── Technical/        ✅ D&D guides
│   └── Immersive/        ✅ Structure created
│
└── data/                 ✅ Created
    ├── chromadb/
    └── characters/
```

## ⚙️ Current Configuration

**Production Model**: Mistral-7B-Instruct-v0.2 (to download)
**Dev Model**: TinyLlama-1.1B (already present)

To switch between them, edit `models/config/model_config.json`:
- Mistral 7B: Better quality, slower
- TinyLlama: Fast, limited quality

## 🐛 Troubleshooting

### "Model not found" Error
→ Download Mistral 7B or temporarily use TinyLlama

### "ChromaDB" Error
→ Installation in progress, please wait

### "llama-cpp-python" Error
→ Installation in progress, if it fails:
```bash
pip install llama-cpp-python --force-reinstall
```

## 📝 Notes

- GGUF models are in .gitignore (too large)
- TinyLlama OK for dev, Mistral 7B for prod
- Context Mistral: 8192 tokens vs TinyLlama: 2048 tokens

---

**See TODO.md for complete roadmap** 🎯
