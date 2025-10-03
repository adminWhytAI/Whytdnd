# WhytDD - Complete TODO List

## Legend
- ⏳ Pending
- 🚧 In Progress
- ✅ Completed
- ⚠️ Blocked
- 🔥 High Priority
- 📝 Documentation

---

## Phase 0: Initial Setup (Week 1) - 80% ✅

### Environment Setup
- [x] ✅ Create backend folder structure
- [ ] ⏳ Create frontend folder structure
- [x] ✅ Initialize git repository
- [x] ✅ Create .gitignore (Python + Node)
- [ ] ⏳ Setup Python virtual environment
- [x] ✅ Install backend dependencies (requirements.txt)
- [ ] ⏳ Setup Vite + React project
- [ ] ⏳ Install frontend dependencies (package.json)
- [ ] ⏳ Configure TailwindCSS
- [ ] ⏳ Setup shadcn/ui

### Configuration
- [x] ✅ Create backend/utils/config.py
- [x] ✅ Create backend/utils/logger.py
- [x] ✅ Create backend/utils/exceptions.py
- [ ] ⏳ Configure CORS in FastAPI
- [x] ✅ Setup environment variables (.env)

### Models Setup
- [x] ✅ Create models/ structure (gguf, config, embeddings)
- [x] ✅ Move TinyLlama to models/gguf/
- [x] ✅ Create model_config.json
- [ ] ⏳ Download Mistral-7B-Instruct-v0.2.Q4_K_M.gguf

### Project Documentation
- [x] ✅ ARCHITECTURE.md created
- [x] ✅ TODO.md structured
- [x] ✅ SETUP.md created
- [x] ✅ README_PROJECT.md created
- [x] ✅ PHASE0_COMPLETE.md created
- [x] ✅ discussion.md updated

### Utility Scripts
- [x] ✅ backend/scripts/download_mistral.py
- [x] ✅ backend/scripts/test_model.py

---

## Phase 1: Immersive Documentation (Week 2) 🔥

### Creating Immersive Documentation

#### Races (13 files)
- [x] ✅ Being_A_Dwarf_Mountain.md
- [ ] 📝 Being_A_Dwarf_Hill.md
- [ ] 📝 Being_An_Elf_High.md
- [ ] 📝 Being_An_Elf_Wood.md
- [ ] 📝 Being_A_Human.md
- [ ] 📝 Being_A_Halfling_Lightfoot.md
- [ ] 📝 Being_A_Halfling_Stout.md
- [ ] 📝 Being_A_Dragonborn.md
- [ ] 📝 Being_A_Gnome_Forest.md
- [ ] 📝 Being_A_Gnome_Rock.md
- [ ] 📝 Being_A_Half_Elf.md
- [ ] 📝 Being_A_Half_Orc.md
- [ ] 📝 Being_A_Tiefling.md

#### Classes (12 files)
- [x] ✅ Being_A_Fighter.md
- [ ] 📝 Being_A_Wizard.md
- [ ] 📝 Being_A_Rogue.md
- [ ] 📝 Being_A_Cleric.md
- [ ] 📝 Being_A_Paladin.md
- [ ] 📝 Being_A_Ranger.md
- [ ] 📝 Being_A_Barbarian.md
- [ ] 📝 Being_A_Bard.md
- [ ] 📝 Being_A_Druid.md
- [ ] 📝 Being_A_Monk.md
- [ ] 📝 Being_A_Sorcerer.md
- [ ] 📝 Being_A_Warlock.md

#### Stats (12 files)
- [x] ✅ Having_High_Strength.md (16+)
- [ ] 📝 Having_Average_Strength.md (10-15)
- [ ] 📝 Having_Low_Strength.md (6-9)
- [ ] 📝 Having_High_Dexterity.md
- [ ] 📝 Having_Low_Dexterity.md
- [ ] 📝 Having_High_Constitution.md
- [ ] 📝 Having_Low_Constitution.md
- [ ] 📝 Having_High_Intelligence.md
- [x] ✅ Having_Low_Intelligence.md
- [ ] 📝 Having_High_Wisdom.md
- [ ] 📝 Having_Low_Wisdom.md
- [ ] 📝 Having_High_Charisma.md
- [ ] 📝 Having_Low_Charisma.md

#### Alignments (9 files)
- [x] ✅ Living_Lawful_Good.md
- [ ] 📝 Living_Neutral_Good.md
- [ ] 📝 Living_Chaotic_Good.md
- [ ] 📝 Living_Lawful_Neutral.md
- [ ] 📝 Living_True_Neutral.md
- [ ] 📝 Living_Chaotic_Neutral.md
- [ ] 📝 Living_Lawful_Evil.md
- [ ] 📝 Living_Neutral_Evil.md
- [ ] 📝 Living_Chaotic_Evil.md

---

## Phase 2: Backend - Parsing & Rules (Week 3)

### Knowledge Parser Module

#### Rule Parser
- [ ] ⏳ Create backend/knowledge_parser/rule_parser.py
  - [ ] RaceParser class
  - [ ] ClassParser class
  - [ ] RuleExtractor class
  - [ ] parse_races_from_md() function
  - [ ] parse_classes_from_md() function
  - [ ] extract_mechanics() function
- [ ] ⏳ Create backend/knowledge_parser/data_validator.py
  - [ ] Pydantic RaceSchema
  - [ ] Pydantic ClassSchema
  - [ ] Custom validators

#### Immersive Parser
- [ ] ⏳ Create backend/knowledge_parser/immersive_parser.py
  - [ ] ImmersiveDocParser class
  - [ ] FragmentExtractor class
  - [ ] parse_immersive_docs() function
  - [ ] extract_first_person_content() function

#### Generating Rules Database
- [ ] ⏳ Setup script: parse_all_rules.py
- [ ] ⏳ Generate data/rules_database.json
- [ ] ⏳ Validate generated JSON structure
- [ ] ⏳ Unit tests for parsers

---

## Phase 3: Backend - Character Creator (Week 4) 🔥

### Character Creator Module

#### Stats Management
- [ ] ⏳ Create backend/character_creator/stats_calculator.py
  - [ ] StatsManager class
  - [ ] DiceRoller class
  - [ ] calculate_modifier() method
  - [ ] generate_standard_array() method
  - [ ] roll_4d6_drop_lowest() method
  - [ ] point_buy() method
  - [ ] Stats unit tests

#### Behavioral Translation
- [ ] 🔥 Create backend/character_creator/behavioral_translator.py
  - [ ] BehavioralProfileBuilder class
  - [ ] translate_stats_to_behavior() method
  - [ ] translate_race_to_behavior() method
  - [ ] translate_class_to_behavior() method
  - [ ] translate_alignment_to_behavior() method
  - [ ] build_complete_profile() method
  - [ ] Translation unit tests

#### Character Generation
- [ ] ⏳ Create backend/character_creator/creator_logic.py
  - [ ] CharacterGenerator class
  - [ ] create_character() method
  - [ ] apply_racial_bonuses() method
  - [ ] calculate_hp() method
  - [ ] assign_proficiencies() method
  - [ ] generate_personality() method

#### Equipment
- [ ] ⏳ Create backend/character_creator/equipment_manager.py
  - [ ] EquipmentBuilder class
  - [ ] get_starting_equipment() method
  - [ ] calculate_ac() method

#### Tests
- [ ] ⏳ Test complete Dwarf Fighter creation
- [ ] ⏳ Test complete Elf Wizard creation
- [ ] ⏳ Test behavioral profile generated correctly

---

## Phase 4: Backend - RAG Engine (Week 5-6) 🔥

### Embeddings Module
- [ ] 🔥 Create backend/rag_engine/embeddings/model.py
  - [ ] EmbeddingModel class
  - [ ] Load sentence-transformers model
  - [ ] encode_text() method
  - [ ] encode_batch() method
  - [ ] Embeddings performance tests

- [ ] ⏳ Create backend/rag_engine/embeddings/character_embedder.py
  - [ ] CharacterKnowledgeEmbedder class
  - [ ] embed_fragment() method
  - [ ] embed_character_data() method

### VectorStore Module
- [ ] 🔥 Create backend/rag_engine/vectorstore/chromadb_manager.py
  - [ ] ChromaDBManager class
  - [ ] UniversalKnowledge class
  - [ ] CharacterKnowledge class
  - [ ] create_collection() method
  - [ ] add_documents() method
  - [ ] delete_collection() method
  - [ ] ChromaDB setup tests

- [ ] ⏳ Create backend/rag_engine/vectorstore/query_engine.py
  - [ ] VectorQueryEngine class
  - [ ] query_similar() method
  - [ ] query_with_filters() method
  - [ ] batch_query() method

### Knowledge Builder Module
- [ ] 🔥 Create backend/rag_engine/knowledge_builder/universal_indexer.py
  - [ ] UniversalKnowledgeIndexer class
  - [ ] index_immersive_docs() method
  - [ ] index_races() method
  - [ ] index_classes() method
  - [ ] index_alignments() method
  - [ ] Initial indexation script

- [ ] 🔥 Create backend/rag_engine/knowledge_builder/character_indexer.py
  - [ ] CharacterKnowledgeIndexer class
  - [ ] index_character() method
  - [ ] index_identity() method
  - [ ] index_behavioral_profile() method
  - [ ] update_character_knowledge() method

- [ ] ⏳ Create backend/rag_engine/knowledge_builder/fragment_builder.py
  - [ ] KnowledgeFragmenter class
  - [ ] MetadataEnricher class
  - [ ] create_fragment() method
  - [ ] add_metadata() method

### Retriever Module
- [ ] 🔥 Create backend/rag_engine/retriever.py
  - [ ] RAGRetriever class
  - [ ] FragmentPrioritizer class
  - [ ] retrieve_relevant_fragments() method
  - [ ] prioritize_critical_fragments() method
  - [ ] merge_universal_and_character() method
  - [ ] Retrieval quality tests

---

## Phase 5: Backend - LLM Interface (Week 7) 🔥

### Model Loading
- [ ] 🔥 Create backend/llm_interface/model_loader.py
  - [ ] GGUFModelLoader class
  - [ ] load_model() method
  - [ ] generate() method
  - [ ] Configuration parameters (temperature, top_p, etc.)
  - [ ] Model loading tests

### Prompt Building
- [ ] 🔥 Create backend/llm_interface/prompt_builder.py
  - [ ] DynamicPromptBuilder class
  - [ ] TemplateManager class
  - [ ] Base conversation template
  - [ ] Journal generation template
  - [ ] build_conversation_prompt() method
  - [ ] inject_behavioral_profile() method
  - [ ] inject_fragments() method
  - [ ] Template tests

### Inference Engine
- [ ] 🔥 Create backend/llm_interface/inference.py
  - [ ] CharacterConversationEngine class
  - [ ] chat() method
  - [ ] calculate_temperature() method
  - [ ] clean_response() method
  - [ ] Response generation tests

---

## Phase 6: Backend - Conversation & Journal (Week 8)

### Conversation Manager
- [ ] ⏳ Create backend/conversation_manager/memory.py
  - [ ] ConversationMemory class
  - [ ] ShortTermMemory class
  - [ ] LongTermMemory class
  - [ ] add_message() method
  - [ ] get_context_window() method
  - [ ] save_to_disk() method

- [ ] ⏳ Create backend/conversation_manager/enrichment.py
  - [ ] ConversationEnricher class
  - [ ] EventExtractor class
  - [ ] extract_events() method
  - [ ] create_memory_fragments() method

### Journal System
- [ ] ⏳ Create backend/journal_system/event_detector.py
  - [ ] EventDetector class
  - [ ] EventClassifier class
  - [ ] detect_important_event() method
  - [ ] classify_event_type() method

- [ ] ⏳ Create backend/journal_system/journal_generator.py
  - [ ] JournalEntryGenerator class
  - [ ] generate_entry() method
  - [ ] format_entry() method
  - [ ] Journal entry templates

- [ ] ⏳ Create backend/journal_system/journal_indexer.py
  - [ ] JournalIndexer class
  - [ ] index_journal_entry() method
  - [ ] link_to_timeline() method

---

## Phase 7: Backend - Character Evolution (Week 9)

### Level Up System
- [ ] ⏳ Create backend/character_evolution/level_up.py
  - [ ] LevelUpManager class
  - [ ] calculate_new_stats() method
  - [ ] add_class_features() method
  - [ ] update_hp() method
  - [ ] update_proficiency_bonus() method

### Class Change
- [ ] ⏳ Create backend/character_evolution/class_change.py
  - [ ] ClassChangeHandler class
  - [ ] change_class() method
  - [ ] update_behavioral_profile() method
  - [ ] preserve_history() method

### Timeline
- [ ] ⏳ Create backend/character_evolution/timeline_manager.py
  - [ ] CharacterTimeline class
  - [ ] PhaseManager class
  - [ ] add_phase() method
  - [ ] get_timeline() method
  - [ ] query_by_timeframe() method

---

## Phase 8: Backend - API (Week 10) 🔥

### API Setup
- [ ] 🔥 Create backend/api/main.py
  - [ ] Setup FastAPI app
  - [ ] Configure CORS
  - [ ] Add middleware
  - [ ] Health check endpoint

### Pydantic Models
- [ ] ⏳ Create backend/api/models/character_schema.py
  - [ ] CharacterCreate
  - [ ] CharacterResponse
  - [ ] Stats
  - [ ] BehavioralProfile

- [ ] ⏳ Create backend/api/models/chat_schema.py
  - [ ] ChatRequest
  - [ ] ChatResponse
  - [ ] Message

- [ ] ⏳ Create backend/api/models/journal_schema.py
  - [ ] JournalEntry
  - [ ] Timeline
  - [ ] Phase

### Routes - Character
- [ ] 🔥 Create backend/api/routes/character_routes.py
  - [ ] POST /character/create
  - [ ] GET /character/{id}
  - [ ] GET /characters (list all)
  - [ ] PUT /character/{id}
  - [ ] DELETE /character/{id}
  - [ ] Routes tests

### Routes - Chat
- [ ] 🔥 Create backend/api/routes/chat_routes.py
  - [ ] POST /chat
  - [ ] GET /chat/history/{character_id}
  - [ ] DELETE /chat/history/{character_id}
  - [ ] Routes tests

### Routes - Journal
- [ ] ⏳ Create backend/api/routes/journal_routes.py
  - [ ] GET /journal/{character_id}
  - [ ] POST /journal/{character_id}/entry
  - [ ] GET /journal/{character_id}/timeline

### Routes - Evolution
- [ ] ⏳ Create backend/api/routes/evolution_routes.py
  - [ ] POST /character/{id}/levelup
  - [ ] POST /character/{id}/class-change
  - [ ] GET /character/{id}/timeline

### API Tests
- [ ] ⏳ End-to-end integration tests
- [ ] ⏳ Load tests (performance)
- [ ] ⏳ OpenAPI/Swagger documentation

---

## Phase 9: Frontend - Setup & UI Components (Week 11)

### Frontend Setup
- [ ] ⏳ Configure React Router
- [ ] ⏳ Configure React Query
- [ ] ⏳ Configure Zustand stores
- [ ] ⏳ Create global layout
- [ ] ⏳ Create navigation

### shadcn/ui Components
- [ ] ⏳ Install Button component
- [ ] ⏳ Install Card component
- [ ] ⏳ Install Dialog component
- [ ] ⏳ Install Form component
- [ ] ⏳ Install Tabs component
- [ ] ⏳ Install ScrollArea component
- [ ] ⏳ Customize with D&D theme

### Custom UI Components
- [ ] ⏳ Create components/ui/Ornament.jsx
- [ ] ⏳ Create components/ui/DiceRoller.jsx
- [ ] ⏳ Create components/ui/StatGem.jsx
- [ ] ⏳ Create components/ui/ParchmentCard.jsx

---

## Phase 10: Frontend - Character Creator (Week 12) 🔥

### Creator Components
- [ ] 🔥 Create components/creator/CreationStepper.jsx
  - [ ] Multi-step state management
  - [ ] Navigation between steps
  - [ ] Validation each step

- [ ] 🔥 Create components/creator/RaceSelector.jsx
  - [ ] Display all races
  - [ ] Immersive descriptions
  - [ ] Preview traits

- [ ] 🔥 Create components/creator/ClassSelector.jsx
  - [ ] Display all classes
  - [ ] Preview abilities
  - [ ] Class icons

- [ ] 🔥 Create components/creator/StatsRoller.jsx
  - [ ] Dice rolling animation
  - [ ] Standard array method
  - [ ] Point buy method
  - [ ] Dice rolling method

- [ ] ⏳ Create components/creator/BackgroundForm.jsx
  - [ ] Personality input
  - [ ] Traits, ideals, bonds, flaws
  - [ ] Background selection

### Creator Page
- [ ] 🔥 Create pages/CharacterCreator.jsx
  - [ ] Integrate CreationStepper
  - [ ] Final submit
  - [ ] API create call
  - [ ] Redirect after creation

---

## Phase 11: Frontend - Character View & Chat (Week 13) 🔥

### Character Display
- [ ] 🔥 Create components/character/CharacterSheet.jsx
  - [ ] Character sheet layout
  - [ ] Display stats
  - [ ] Display abilities
  - [ ] Display equipment

- [ ] ⏳ Create components/character/StatsDisplay.jsx
  - [ ] Stat gems display
  - [ ] Modifier tooltips

- [ ] ⏳ Create components/character/AbilityCard.jsx
  - [ ] Ability card
  - [ ] Description
  - [ ] Usage

- [ ] ⏳ Create components/character/InventoryList.jsx
  - [ ] Equipment list
  - [ ] AC display
  - [ ] Weapons display

### Chat Interface
- [ ] 🔥 Create components/chat/ChatInterface.jsx
  - [ ] Chat layout
  - [ ] Messages list
  - [ ] Message input
  - [ ] Send message

- [ ] 🔥 Create components/chat/MessageBubble.jsx
  - [ ] Parchment style for character
  - [ ] Modern style for user
  - [ ] Timestamp
  - [ ] Avatar

- [ ] ⏳ Create components/chat/TypingIndicator.jsx
  - [ ] Dots animation
  - [ ] "Character is writing..."

- [ ] ⏳ Create components/chat/CharacterAvatar.jsx
  - [ ] Dynamic avatar
  - [ ] Status indicator

### Character View Page
- [ ] 🔥 Create pages/CharacterView.jsx
  - [ ] Split screen layout
  - [ ] Character sheet left
  - [ ] Chat interface right
  - [ ] Responsive mobile

---

## Phase 12: Frontend - Journal & Timeline (Week 14)

### Journal Components
- [ ] ⏳ Create components/journal/JournalViewer.jsx
  - [ ] Journal entries list
  - [ ] Date filters
  - [ ] Search

- [ ] ⏳ Create components/journal/JournalEntry.jsx
  - [ ] Entry display
  - [ ] Manuscript style
  - [ ] Expand/collapse

- [ ] ⏳ Create components/journal/Timeline.jsx
  - [ ] Vertical timeline
  - [ ] Character phases
  - [ ] Major events

### Journal Page
- [ ] ⏳ Create pages/JournalPage.jsx
  - [ ] Integrate JournalViewer
  - [ ] Integrate Timeline
  - [ ] Tab navigation

---

## Phase 13: Frontend - Home & Navigation (Week 15)

### Home Page
- [ ] 🔥 Create pages/Home.jsx
  - [ ] List created characters
  - [ ] Character cards
  - [ ] Create new button
  - [ ] Search/Filter characters

### Navigation
- [ ] ⏳ Create Header component
  - [ ] WhytDD logo
  - [ ] Navigation links
  - [ ] User menu (future)

### API Integration
- [ ] 🔥 Create api/client.js
  - [ ] Axios instance
  - [ ] Base URL config
  - [ ] Interceptors

- [ ] 🔥 Create api/characterApi.js
  - [ ] create()
  - [ ] get()
  - [ ] list()
  - [ ] update()
  - [ ] delete()

- [ ] 🔥 Create api/chatApi.js
  - [ ] sendMessage()
  - [ ] getHistory()

- [ ] ⏳ Create api/journalApi.js
  - [ ] getJournal()
  - [ ] getTimeline()

---

## Phase 14: Hooks & Stores (Week 15)

### Custom Hooks
- [ ] 🔥 Create hooks/useCharacter.js
  - [ ] React Query integration
  - [ ] CRUD operations
  - [ ] Cache management

- [ ] 🔥 Create hooks/useChat.js
  - [ ] Message sending
  - [ ] History loading
  - [ ] Real-time updates

- [ ] ⏳ Create hooks/useDiceRoller.js
  - [ ] Dice rolling logic
  - [ ] Animation state

- [ ] ⏳ Create hooks/useJournal.js
  - [ ] Fetch journal
  - [ ] Pagination

### Zustand Stores
- [ ] ⏳ Create stores/characterStore.js
  - [ ] currentCharacter
  - [ ] setCharacter
  - [ ] updateCharacter

- [ ] ⏳ Create stores/chatStore.js
  - [ ] messages
  - [ ] addMessage
  - [ ] clearMessages

---

## Phase 15: Styling & Polish (Week 16)

### D&D Styles
- [ ] 🔥 Implement D&D color palette
- [ ] 🔥 Configure medieval fonts
- [ ] ⏳ Create textures (parchment, leather)
- [ ] ⏳ Create animations (dice, gold shimmer)
- [ ] ⏳ Responsive design all screens
- [ ] ⏳ Dark mode (dungeon)

### Assets
- [ ] ⏳ Find/create class icons
- [ ] ⏳ Find/create race icons
- [ ] ⏳ Parchment texture
- [ ] ⏳ Leather texture
- [ ] ⏳ 3D dice images

---

## Phase 16: Testing & Debugging (Week 17-18)

### Backend Tests
- [ ] ⏳ Unit tests all modules
- [ ] ⏳ API integration tests
- [ ] ⏳ RAG retrieval quality tests
- [ ] ⏳ GGUF generation tests
- [ ] ⏳ ChromaDB performance tests

### Frontend Tests
- [ ] ⏳ Component tests (Vitest)
- [ ] ⏳ E2E tests (Playwright)
- [ ] ⏳ Responsive tests
- [ ] ⏳ Accessibility tests

### Debugging
- [ ] ⏳ Fix backend bugs
- [ ] ⏳ Fix frontend bugs
- [ ] ⏳ Performance optimization
- [ ] ⏳ Memory leaks check

---

## Phase 17: Documentation (Week 19)

### User Documentation
- [ ] 📝 Application usage guide
- [ ] 📝 Character creation guide
- [ ] 📝 Character conversation guide
- [ ] 📝 FAQ

### Developer Documentation
- [ ] 📝 Setup instructions
- [ ] 📝 Detailed architecture
- [ ] 📝 API documentation
- [ ] 📝 Code comments
- [ ] 📝 Contributing guide

---

## Phase 18: Deployment (Week 20)

### Backend Deployment
- [ ] ⏳ Backend Dockerfile
- [ ] ⏳ Docker-compose setup
- [ ] ⏳ Production environment variables
- [ ] ⏳ Deploy backend (server/cloud)

### Frontend Deployment
- [ ] ⏳ Optimized production build
- [ ] ⏳ Deploy frontend (Vercel/Netlify)
- [ ] ⏳ Configure production API endpoints

### Database
- [ ] ⏳ Setup ChromaDB persistence
- [ ] ⏳ Backup strategy
- [ ] ⏳ Migration scripts

---

## Future Features (Post-MVP)

### V2.0 - Improvements
- [ ] ⏳ Multi-characters in conversation
- [ ] ⏳ Integrated combat simulator
- [ ] ⏳ Automatic dice rolling
- [ ] ⏳ Advanced inventory management
- [ ] ⏳ Quest system
- [ ] ⏳ Character relationships
- [ ] ⏳ Export character sheet to PDF

### V3.0 - Campaign Mode
- [ ] ⏳ Dungeon Master mode
- [ ] ⏳ Adventurer group management
- [ ] ⏳ Interactive world map
- [ ] ⏳ Persistent NPCs
- [ ] ⏳ Game session management

### V4.0 - Advanced
- [ ] ⏳ Character Text-to-Speech
- [ ] ⏳ Character image generation (SD)
- [ ] ⏳ Multiplayer mode
- [ ] ⏳ Mobile app (React Native)
- [ ] ⏳ VR/AR support

---

## Immediate Priorities 🔥

1. **Immersive Documentation** - Without this, characters aren't immersive
2. **Behavioral Translator** - Core of stats → behavior translation
3. **Complete RAG Engine** - Memory system
4. **LLM Interface** - Response generation
5. **Main API Routes** - Create character + Chat
6. **Frontend Creator** - Creation interface
7. **Frontend Chat** - Conversation interface

---

## Important Notes

- **Don't code before having**:
  - ✅ Complete immersive documentation
  - ✅ Validated architecture
  - ✅ Test setup ready

- **Test as you go**:
  - Each module must have unit tests
  - Integration tests after each phase

- **Keep focus on MVP**:
  - Create simple character
  - Converse with character
  - Basic journal
  - Advanced features = V2+

---

**Last updated**: 2025-10-04
**Total estimate**: 20 weeks (5 months)
**Realistic MVP**: 12 weeks (3 months)
