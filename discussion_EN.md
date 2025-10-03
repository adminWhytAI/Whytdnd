# WhytDD Architecture Discussion - D&D Character System with GGUF

**Date**: October 3, 2025

## Project Objective

Create a system that allows **generating D&D 5e characters** according to official rules and **conversing with them via a GGUF model**, where the character becomes truly alive through their knowledge base.

## Key Decision: RAG Architecture Instead of Static Prompt

### ❌ Rejected Approach: Predefined System Prompt

**Problem**: A static prompt containing all character info would be:
- Limited by context size
- Fixed and difficult to evolve
- Inefficient (sends everything with each message)
- Does not allow character evolution

### ✅ Chosen Approach: RAG System (Retrieval-Augmented Generation)

**Principle**: The character is a **living knowledge base** that the GGUF queries dynamically.

**How it works**:
1. All character data is fragmented and vectorially indexed
2. With each user message, the system retrieves ONLY the relevant fragments
3. The prompt is **auto-generated dynamically** with these fragments + conversation context
4. The GGUF responds by embodying the character with relevant info
5. New experiences are added in real-time to the database

## Knowledge Base Structure

### Data Types

**Immutable Data** (never changes)
- Race and racial traits
- Name
- Base characteristic values

**Semi-Static Data** (rarely changes)
- Current level
- Class and abilities
- Mastered skills
- Main equipment
- Established relationships

**Dynamic Data** (constantly evolves)
- Lived experiences
- Previous conversations
- Current quests
- Current emotional state
- Acquired objects
- NPCs encountered
- Personality evolution

### Fragment Organization

Each knowledge fragment contains:
- **Content**: The information itself
- **Type**: Identity, personality, skill, history, etc.
- **Priority**: Critical (always included) / High / Medium / Low
- **Temporality**: Distant past / Past / Recent / Present
- **Metadata**: Category, date, frequency of use

## Concrete Example: Conaosfeo the Paladin

### Character Timeline

**Phase 1: Paladin of Vengeance**
```
Knowledge base:
- "I am Conaosfeo, Paladin of Vengeance"
- "I have sworn to punish the guilty and protect the innocent"
- "Abilities: Divine Smite, Aura of Protection"
- "Alignment: Lawful Good"
```

**Phase 2: The Turning Point (Murder of Innocents)**
```
Added events:
- "I killed innocents in my quest for vengeance"
- "I betrayed my sacred oath"
- "Their blood haunts my nights"
- "Date and context of the event"
```

**Phase 3: Transformation into Oathbreaker**
```
New data:
- "I am now an Oathbreaker Paladin"
- "I lost my Vengeance powers"
- "New abilities: Dreadful Aspect, Aura of Hate"
- "Alignment: Neutral Evil"
- "Emotional state: Guilt/Rage/Denial"
```

### The System Preserves ALL History

**Important**: The character keeps in memory:
- ✅ Who they were (Vengeance Paladin)
- ✅ What they did (Killed innocents)
- ✅ How they changed (Became Oathbreaker)
- ✅ Who they are now (Oathbreaker with Dark powers)
- ✅ Their emotional state regarding their past

**Each phase has temporal metadata** allowing the RAG to retrieve relevant info based on question context.

## Technical Workflow

### With Each User Message

1. **Message received**: "Tell me about your oath"

2. **Transformation into embedding**: The message becomes a mathematical vector

3. **RAG search**: The system finds the 5-10 most relevant fragments
   - "I was a Paladin of Vengeance" [Phase 1]
   - "I betrayed my oath" [Phase 2]
   - "I am now an Oathbreaker" [Phase 3]
   - "Their blood haunts my nights" [Emotional state]

4. **Auto-Generated Prompt Construction**:
   ```
   You are Conaosfeo.
   
   Information about you:
   - You were a Paladin of Vengeance
   - You betrayed your oath by killing innocents
   - You are now an Oathbreaker Paladin
   - Their blood haunts your nights
   
   [Recent conversation exchanges]
   
   User: "Tell me about your oath"
   
   Respond as Conaosfeo:
   ```

5. **GGUF Generates Response**: Response coherent with character and their evolution

6. **Enrichment**: The system can extract and add new info from the conversation

## Advantages of This Approach

### 1. No Size Limit
The character can have an IMMENSE history, only relevant parts are sent to the GGUF.

### 2. Natural Evolution
New experiences added in real-time:
- Level up
- New magic items
- Developed relationships
- Traumas
- Personality changes

### 3. Dynamic Consistency
The character responds differently based on context:
- Question about combat → Retrieves martial skills
- Question about history → Retrieves complete backstory
- Emotional question → Retrieves personality + significant events

### 4. Long-Term Memory
Unlike a static prompt:
- The character remembers EVERYTHING
- Even conversations from months ago
- Accessible via semantic search

### 5. Efficient Multi-Characters
Each character has their own knowledge base. The system switches between them easily.

## Required Technologies

### Backend
- **Python** with FastAPI for REST API
- **Sentence-transformers**: Local embeddings generation (multilingual French)
- **ChromaDB**: Local vector database (free, fast)
- **llama-cpp-python**: Interface with GGUF model

### Frontend
- **HTML/CSS/JavaScript**: Simple interface
- Character creation page (form)
- Chat interface with character

### Project Structure

```
WhytDD/
├── Documentation/              [✅ D&D documentation created]
├── gguf/                      [GGUF models]
├── backend/
│   ├── rag_engine/            [RAG system]
│   │   ├── embeddings/        [Embeddings generation]
│   │   ├── vectorstore/       [ChromaDB]
│   │   ├── knowledge_builder/ [Database construction]
│   │   └── retriever.py       [Orchestration]
│   ├── character_creator/     [Character generator]
│   ├── llm_interface/         [GGUF interface with RAG]
│   └── api/                   [REST API]
├── frontend/
│   ├── character_creator.html [Character creation]
│   ├── chat_interface.html    [Chat with character]
│   └── js/css/
├── characters/                 [Character storage]
└── character_knowledge/        [Knowledge bases]
    └── [character_id]/
        ├── core_identity.json
        ├── personality.json
        ├── backstory.json
        ├── experiences/
        └── vector_db/          [ChromaDB embeddings]
```

## End User Workflow

1. **Creation**: Web form → Character generated according to D&D rules
2. **Indexing**: All data fragmented and vectorized (few seconds)
3. **Chat**: Discussion interface
4. **Conversation**: 
   - RAG retrieves relevant info
   - GGUF generates coherent response
   - Experiences enrich the database
5. **Evolution**: The character grows with their adventures

## Advanced Use Cases

### Level Up
Simply add new abilities and stats to the database. The character mentions them naturally if relevant.

### Magic Items
"I possess Dawnbringer, a legendary solar sword"
The character mentions their weapon when appropriate.

### Evolving Relationships
"I hate elves" → after adventures → "I respect Legolas"
RAG retrieves the most recent info with historical context.

### Traumas
"Since my friend's death, I am more wary"
Persistent impact in future responses.

## Discussion Key Points

### Confirmation: Auto-Generated Prompt

✅ **YES**: The prompt is rebuilt with each message
✅ **YES**: It updates according to character sheet, stats, history
✅ **YES**: All evolution phases are preserved
✅ **YES**: The character keeps the context of their complete background

### The Character Is Truly Alive

The RAG system allows the character to:
- Remember all their past
- Evolve with their experiences
- Respond in a coherent and contextualized manner
- Have real emotional depth
- Grow and change over time

**Without ever**:
- Overloading the GGUF context
- Forgetting their history
- Contradicting themselves
- Being limited by a fixed prompt

## Next Steps

1. Implement character generator (D&D 5e rules)
2. Create fragmentation and indexing system
3. Develop RAG interface with ChromaDB
4. Integrate GGUF with dynamic prompt system
5. Create frontend interfaces (creation + chat)
6. Tests with complete and evolving characters

---

## Architecture and Planning Additions

### Created Files

**ARCHITECTURE.md**:
- Complete project directory structure
- Lists all files with imports and classes
- Detailed inter-file links
- Complete data flows
- Required configuration

**TODO.md**:
- Exhaustive todolist (20 weeks)
- Phases structured by modules
- Identified priorities
- MVP timeline: 12 weeks
- Future features V2.0+

### Final Validated Stack

**Backend**:
- Python 3.10+ / FastAPI
- ChromaDB (vector database)
- sentence-transformers (embeddings)
- llama-cpp-python (GGUF)

**Frontend**:
- React 18 + Vite
- TailwindCSS + shadcn/ui (medieval D&D theme)
- React Query + Zustand
- React Router

### Required Documentation

**Immersive Documentation (PRIORITY)**:
- 13 races in first person (Being_A_Dwarf.md, etc.)
- 12 classes in first person (Being_A_Fighter.md, etc.)
- High/low stats (Having_High_Strength.md, etc.)
- 9 lived alignments (Living_Lawful_Good.md, etc.)

**Goal**: The GGUF must "become" the character, not "describe" them

### Confirmed Dual Documentation

**Technical (existing)**: For the system, calculations, mechanics

**Immersive (to create)**: For the GGUF, first-person experience

---

**This approach transforms a simple chatbot into a true living D&D character with memory, personality, and authentic evolution.**
