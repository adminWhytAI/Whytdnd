# WhytDD - TODO List Complète

## Légende
- ⏳ En attente
- 🚧 En cours
- ✅ Terminé
- ⚠️ Bloqué
- 🔥 Priorité haute
- 📝 Documentation

---

## Phase 0 : Setup Initial (Semaine 1) - 85% ✅

### Environment Setup
- [x] ✅ Créer structure dossiers backend
- [ ] ⏳ Créer structure dossiers frontend
- [x] ✅ Initialiser git repository
- [x] ✅ Créer .gitignore (Python + Node)
- [ ] ⏳ Setup virtual environment Python
- [x] ✅ Installer dépendances backend (requirements.txt)
- [ ] ⏳ Setup projet Vite + React
- [ ] ⏳ Installer dépendances frontend (package.json)
- [ ] ⏳ Configurer TailwindCSS
- [ ] ⏳ Setup shadcn/ui

### Configuration
- [x] ✅ Créer backend/utils/config.py
- [x] ✅ Créer backend/utils/logger.py
- [x] ✅ Créer backend/utils/exceptions.py
- [ ] ⏳ Configurer CORS dans FastAPI
- [x] ✅ Setup variables d'environnement (.env)

### Models Setup
- [x] ✅ Créer structure models/ (gguf, config, embeddings)
- [x] ✅ Déplacer TinyLlama dans models/gguf/
- [x] ✅ Créer model_config.json
- [ ] ⏳ Télécharger Mistral-7B-Instruct-v0.2.Q4_K_M.gguf

### Documentation Projet
- [x] ✅ ARCHITECTURE.md créé
- [x] ✅ TODO.md structuré
- [x] ✅ SETUP.md créé
- [x] ✅ README_PROJECT.md créé
- [x] ✅ PHASE0_COMPLETE.md créé
- [x] ✅ discussion.md mis à jour

### Scripts Utilitaires
- [x] ✅ backend/scripts/download_mistral.py
- [x] ✅ backend/scripts/test_model.py

### Git Setup
- [x] ✅ git init
- [x] ✅ git add + commit (46 fichiers, 95,782 lignes)
- [ ] ⏳ Créer repo GitHub et push

---

## Phase 1 : Documentation Immersive (Semaine 2) 🔥 - 11% EN COURS

**Objectif** : 46 fichiers immersifs en première personne
**Créés** : 5/46 (~10,800 mots)
**Progression** : 11%

### Création Documentation Immersive

#### Races (13 fichiers) - 1/13 créé
- [x] ✅ Being_A_Dwarf_Mountain.md (2,800 mots)
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

#### Classes (12 fichiers) - 1/12 créé
- [x] ✅ Being_A_Fighter.md (2,200 mots)
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

#### Stats (12 fichiers) - 2/12 créés
- [x] ✅ Having_High_Strength.md (16+) (1,800 mots)
- [ ] 📝 Having_Average_Strength.md (10-15)
- [ ] 📝 Having_Low_Strength.md (6-9)
- [ ] 📝 Having_High_Dexterity.md
- [ ] 📝 Having_Low_Dexterity.md
- [ ] 📝 Having_High_Constitution.md
- [ ] 📝 Having_Low_Constitution.md
- [ ] 📝 Having_High_Intelligence.md
- [x] ✅ Having_Low_Intelligence.md (1,600 mots)
- [ ] 📝 Having_High_Wisdom.md
- [ ] 📝 Having_Low_Wisdom.md
- [ ] 📝 Having_High_Charisma.md
- [ ] 📝 Having_Low_Charisma.md

#### Alignments (9 fichiers) - 1/9 créé
- [x] ✅ Living_Lawful_Good.md (2,400 mots)
- [ ] 📝 Living_Neutral_Good.md
- [ ] 📝 Living_Chaotic_Good.md
- [ ] 📝 Living_Lawful_Neutral.md
- [ ] 📝 Living_True_Neutral.md
- [ ] 📝 Living_Chaotic_Neutral.md
- [ ] 📝 Living_Lawful_Evil.md
- [ ] 📝 Living_Neutral_Evil.md
- [ ] 📝 Living_Chaotic_Evil.md

### Suivi Phase 1

**Fichiers créés** : 5/46 (11%)
**Mots écrits** : ~10,800
**Temps investi** : ~1h15
**Fichiers tracking** : PHASE1_PROGRESS.md créé

**Prochaines priorités** :
- Being_A_Human.md (race populaire)
- Being_An_Elf_High.md (race populaire)
- Being_A_Wizard.md (classe populaire)
- Being_A_Rogue.md (classe populaire)
- Having_High_Intelligence.md (contraste avec Low)

---

## Phase 2 : Backend - Parsing & Rules (Semaine 3) - 🚧 EN COURS

### Knowledge Parser Module

#### Rule Parser ✅ COMPLÉTÉ
- [x] ✅ Créer backend/knowledge_parser/rule_parser.py
  - [x] ✅ Classe RaceParser
  - [x] ✅ Classe ClassParser
  - [x] ✅ Classe RuleExtractor
  - [x] ✅ Fonction parse_races_from_md()
  - [x] ✅ Fonction parse_classes_from_md()
  - [x] ✅ Fonction extract_mechanics()
  
- [x] ✅ Créer backend/knowledge_parser/data_validator.py
  - [x] ✅ Schéma Pydantic RaceSchema
  - [x] ✅ Schéma Pydantic ClassSchema
  - [x] ✅ Schéma Pydantic CharacterCreate
  - [x] ✅ Schéma Pydantic AbilityScores
  - [x] ✅ Schéma Pydantic KnowledgeFragment
  - [x] ✅ Validateurs customs

#### Immersive Parser ✅ COMPLÉTÉ
- [x] ✅ Créer backend/knowledge_parser/immersive_parser.py
  - [x] ✅ Classe ImmersiveDocParser
  - [x] ✅ Classe FragmentExtractor
  - [x] ✅ Fonction parse_immersive_docs()
  - [x] ✅ Fonction extract_first_person_content()
  - [x] ✅ Métadonnées extraction
  - [x] ✅ Section splitting

#### Génération Rules Database ✅ COMPLÉTÉ
- [x] ✅ Script setup: backend/scripts/parse_all_rules.py
  - [x] ✅ Parse technical documentation
  - [x] ✅ Parse immersive documentation
  - [x] ✅ Generate alignments data
  - [x] ✅ Generate ability scores data
  - [x] ✅ Build complete database
  - [x] ✅ Save to JSON with validation
- [ ] ⏳ Générer data/rules_database.json (run script)
- [ ] ⏳ Tests unitaires parsers

---

## Phase 3 : Backend - Character Creator (Semaine 4) 🔥

### Character Creator Module

#### Stats Management
- [ ] ⏳ Créer backend/character_creator/stats_calculator.py
  - [ ] Classe StatsManager
  - [ ] Classe DiceRoller
  - [ ] Méthode calculate_modifier()
  - [ ] Méthode generate_standard_array()
  - [ ] Méthode roll_4d6_drop_lowest()
  - [ ] Méthode point_buy()
  - [ ] Tests unitaires stats

#### Behavioral Translation
- [ ] 🔥 Créer backend/character_creator/behavioral_translator.py
  - [ ] Classe BehavioralProfileBuilder
  - [ ] Méthode translate_stats_to_behavior()
  - [ ] Méthode translate_race_to_behavior()
  - [ ] Méthode translate_class_to_behavior()
  - [ ] Méthode translate_alignment_to_behavior()
  - [ ] Méthode build_complete_profile()
  - [ ] Tests unitaires translation

#### Character Generation
- [ ] ⏳ Créer backend/character_creator/creator_logic.py
  - [ ] Classe CharacterGenerator
  - [ ] Méthode create_character()
  - [ ] Méthode apply_racial_bonuses()
  - [ ] Méthode calculate_hp()
  - [ ] Méthode assign_proficiencies()
  - [ ] Méthode generate_personality()

#### Equipment
- [ ] ⏳ Créer backend/character_creator/equipment_manager.py
  - [ ] Classe EquipmentBuilder
  - [ ] Méthode get_starting_equipment()
  - [ ] Méthode calculate_ac()

#### Tests
- [ ] ⏳ Test création Nain Guerrier complet
- [ ] ⏳ Test création Elfe Magicien complet
- [ ] ⏳ Test behavioral profile généré correctement

---

## Phase 4 : Backend - RAG Engine (Semaine 5-6) 🔥

### Embeddings Module
- [ ] 🔥 Créer backend/rag_engine/embeddings/model.py
  - [ ] Classe EmbeddingModel
  - [ ] Charger sentence-transformers model
  - [ ] Méthode encode_text()
  - [ ] Méthode encode_batch()
  - [ ] Tests performance embeddings

- [ ] ⏳ Créer backend/rag_engine/embeddings/character_embedder.py
  - [ ] Classe CharacterKnowledgeEmbedder
  - [ ] Méthode embed_fragment()
  - [ ] Méthode embed_character_data()

### VectorStore Module
- [ ] 🔥 Créer backend/rag_engine/vectorstore/chromadb_manager.py
  - [ ] Classe ChromaDBManager
  - [ ] Classe UniversalKnowledge
  - [ ] Classe CharacterKnowledge
  - [ ] Méthode create_collection()
  - [ ] Méthode add_documents()
  - [ ] Méthode delete_collection()
  - [ ] Tests ChromaDB setup

- [ ] ⏳ Créer backend/rag_engine/vectorstore/query_engine.py
  - [ ] Classe VectorQueryEngine
  - [ ] Méthode query_similar()
  - [ ] Méthode query_with_filters()
  - [ ] Méthode batch_query()

### Knowledge Builder Module
- [ ] 🔥 Créer backend/rag_engine/knowledge_builder/universal_indexer.py
  - [ ] Classe UniversalKnowledgeIndexer
  - [ ] Méthode index_immersive_docs()
  - [ ] Méthode index_races()
  - [ ] Méthode index_classes()
  - [ ] Méthode index_alignments()
  - [ ] Script initial indexation

- [ ] 🔥 Créer backend/rag_engine/knowledge_builder/character_indexer.py
  - [ ] Classe CharacterKnowledgeIndexer
  - [ ] Méthode index_character()
  - [ ] Méthode index_identity()
  - [ ] Méthode index_behavioral_profile()
  - [ ] Méthode update_character_knowledge()

- [ ] ⏳ Créer backend/rag_engine/knowledge_builder/fragment_builder.py
  - [ ] Classe KnowledgeFragmenter
  - [ ] Classe MetadataEnricher
  - [ ] Méthode create_fragment()
  - [ ] Méthode add_metadata()

### Retriever Module
- [ ] 🔥 Créer backend/rag_engine/retriever.py
  - [ ] Classe RAGRetriever
  - [ ] Classe FragmentPrioritizer
  - [ ] Méthode retrieve_relevant_fragments()
  - [ ] Méthode prioritize_critical_fragments()
  - [ ] Méthode merge_universal_and_character()
  - [ ] Tests retrieval qualité

---

## Phase 5 : Backend - LLM Interface (Semaine 7) 🔥

### Model Loading
- [ ] 🔥 Créer backend/llm_interface/model_loader.py
  - [ ] Classe GGUFModelLoader
  - [ ] Méthode load_model()
  - [ ] Méthode generate()
  - [ ] Configuration paramètres (temperature, top_p, etc.)
  - [ ] Tests chargement model

### Prompt Building
- [ ] 🔥 Créer backend/llm_interface/prompt_builder.py
  - [ ] Classe DynamicPromptBuilder
  - [ ] Classe TemplateManager
  - [ ] Template base conversation
  - [ ] Template journal generation
  - [ ] Méthode build_conversation_prompt()
  - [ ] Méthode inject_behavioral_profile()
  - [ ] Méthode inject_fragments()
  - [ ] Tests templates

### Inference Engine
- [ ] 🔥 Créer backend/llm_interface/inference.py
  - [ ] Classe CharacterConversationEngine
  - [ ] Méthode chat()
  - [ ] Méthode calculate_temperature()
  - [ ] Méthode clean_response()
  - [ ] Tests génération réponses

---

## Phase 6 : Backend - Conversation & Journal (Semaine 8)

### Conversation Manager
- [ ] ⏳ Créer backend/conversation_manager/memory.py
  - [ ] Classe ConversationMemory
  - [ ] Classe ShortTermMemory
  - [ ] Classe LongTermMemory
  - [ ] Méthode add_message()
  - [ ] Méthode get_context_window()
  - [ ] Méthode save_to_disk()

- [ ] ⏳ Créer backend/conversation_manager/enrichment.py
  - [ ] Classe ConversationEnricher
  - [ ] Classe EventExtractor
  - [ ] Méthode extract_events()
  - [ ] Méthode create_memory_fragments()

### Journal System
- [ ] ⏳ Créer backend/journal_system/event_detector.py
  - [ ] Classe EventDetector
  - [ ] Classe EventClassifier
  - [ ] Méthode detect_important_event()
  - [ ] Méthode classify_event_type()

- [ ] ⏳ Créer backend/journal_system/journal_generator.py
  - [ ] Classe JournalEntryGenerator
  - [ ] Méthode generate_entry()
  - [ ] Méthode format_entry()
  - [ ] Template entrées journal

- [ ] ⏳ Créer backend/journal_system/journal_indexer.py
  - [ ] Classe JournalIndexer
  - [ ] Méthode index_journal_entry()
  - [ ] Méthode link_to_timeline()

---

## Phase 7 : Backend - Character Evolution (Semaine 9)

### Level Up System
- [ ] ⏳ Créer backend/character_evolution/level_up.py
  - [ ] Classe LevelUpManager
  - [ ] Méthode calculate_new_stats()
  - [ ] Méthode add_class_features()
  - [ ] Méthode update_hp()
  - [ ] Méthode update_proficiency_bonus()

### Class Change
- [ ] ⏳ Créer backend/character_evolution/class_change.py
  - [ ] Classe ClassChangeHandler
  - [ ] Méthode change_class()
  - [ ] Méthode update_behavioral_profile()
  - [ ] Méthode preserve_history()

### Timeline
- [ ] ⏳ Créer backend/character_evolution/timeline_manager.py
  - [ ] Classe CharacterTimeline
  - [ ] Classe PhaseManager
  - [ ] Méthode add_phase()
  - [ ] Méthode get_timeline()
  - [ ] Méthode query_by_timeframe()

---

## Phase 8 : Backend - API (Semaine 10) 🔥

### API Setup
- [ ] 🔥 Créer backend/api/main.py
  - [ ] Setup FastAPI app
  - [ ] Configure CORS
  - [ ] Add middleware
  - [ ] Health check endpoint

### Pydantic Models
- [ ] ⏳ Créer backend/api/models/character_schema.py
  - [ ] CharacterCreate
  - [ ] CharacterResponse
  - [ ] Stats
  - [ ] BehavioralProfile

- [ ] ⏳ Créer backend/api/models/chat_schema.py
  - [ ] ChatRequest
  - [ ] ChatResponse
  - [ ] Message

- [ ] ⏳ Créer backend/api/models/journal_schema.py
  - [ ] JournalEntry
  - [ ] Timeline
  - [ ] Phase

### Routes - Character
- [ ] 🔥 Créer backend/api/routes/character_routes.py
  - [ ] POST /character/create
  - [ ] GET /character/{id}
  - [ ] GET /characters (list all)
  - [ ] PUT /character/{id}
  - [ ] DELETE /character/{id}
  - [ ] Tests routes

### Routes - Chat
- [ ] 🔥 Créer backend/api/routes/chat_routes.py
  - [ ] POST /chat
  - [ ] GET /chat/history/{character_id}
  - [ ] DELETE /chat/history/{character_id}
  - [ ] Tests routes

### Routes - Journal
- [ ] ⏳ Créer backend/api/routes/journal_routes.py
  - [ ] GET /journal/{character_id}
  - [ ] POST /journal/{character_id}/entry
  - [ ] GET /journal/{character_id}/timeline

### Routes - Evolution
- [ ] ⏳ Créer backend/api/routes/evolution_routes.py
  - [ ] POST /character/{id}/levelup
  - [ ] POST /character/{id}/class-change
  - [ ] GET /character/{id}/timeline

### Tests API
- [ ] ⏳ Tests d'intégration end-to-end
- [ ] ⏳ Tests charge (performance)
- [ ] ⏳ Documentation OpenAPI/Swagger

---

## Phase 9 : Frontend - Setup & UI Components (Semaine 11)

### Setup Frontend
- [ ] ⏳ Configurer React Router
- [ ] ⏳ Configurer React Query
- [ ] ⏳ Configurer Zustand stores
- [ ] ⏳ Créer layout global
- [ ] ⏳ Créer navigation

### shadcn/ui Components
- [ ] ⏳ Installer Button component
- [ ] ⏳ Installer Card component
- [ ] ⏳ Installer Dialog component
- [ ] ⏳ Installer Form component
- [ ] ⏳ Installer Tabs component
- [ ] ⏳ Installer ScrollArea component
- [ ] ⏳ Customiser avec thème D&D

### Custom UI Components
- [ ] ⏳ Créer components/ui/Ornament.jsx
- [ ] ⏳ Créer components/ui/DiceRoller.jsx
- [ ] ⏳ Créer components/ui/StatGem.jsx
- [ ] ⏳ Créer components/ui/ParchmentCard.jsx

---

## Phase 10 : Frontend - Character Creator (Semaine 12) 🔥

### Creator Components
- [ ] 🔥 Créer components/creator/CreationStepper.jsx
  - [ ] State management multi-steps
  - [ ] Navigation entre steps
  - [ ] Validation chaque step

- [ ] 🔥 Créer components/creator/RaceSelector.jsx
  - [ ] Affichage toutes races
  - [ ] Descriptions immersives
  - [ ] Preview traits

- [ ] 🔥 Créer components/creator/ClassSelector.jsx
  - [ ] Affichage toutes classes
  - [ ] Preview capacités
  - [ ] Icônes classes

- [ ] 🔥 Créer components/creator/StatsRoller.jsx
  - [ ] Animation jets de dés
  - [ ] Méthode standard array
  - [ ] Méthode point buy
  - [ ] Méthode dice rolling

- [ ] ⏳ Créer components/creator/BackgroundForm.jsx
  - [ ] Input personnalité
  - [ ] Traits, idéaux, liens, défauts
  - [ ] Background selection

### Creator Page
- [ ] 🔥 Créer pages/CharacterCreator.jsx
  - [ ] Intégrer CreationStepper
  - [ ] Submit final
  - [ ] Appel API create
  - [ ] Redirect après création

---

## Phase 11 : Frontend - Character View & Chat (Semaine 13) 🔥

### Character Display
- [ ] 🔥 Créer components/character/CharacterSheet.jsx
  - [ ] Layout feuille personnage
  - [ ] Display stats
  - [ ] Display capacités
  - [ ] Display équipement

- [ ] ⏳ Créer components/character/StatsDisplay.jsx
  - [ ] Affichage gemmes stats
  - [ ] Tooltips modificateurs

- [ ] ⏳ Créer components/character/AbilityCard.jsx
  - [ ] Card capacité
  - [ ] Description
  - [ ] Usage

- [ ] ⏳ Créer components/character/InventoryList.jsx
  - [ ] Liste équipement
  - [ ] AC display
  - [ ] Armes display

### Chat Interface
- [ ] 🔥 Créer components/chat/ChatInterface.jsx
  - [ ] Layout chat
  - [ ] Messages list
  - [ ] Input message
  - [ ] Send message

- [ ] 🔥 Créer components/chat/MessageBubble.jsx
  - [ ] Style parchemin personnage
  - [ ] Style moderne utilisateur
  - [ ] Timestamp
  - [ ] Avatar

- [ ] ⏳ Créer components/chat/TypingIndicator.jsx
  - [ ] Animation dots
  - [ ] "Personnage écrit..."

- [ ] ⏳ Créer components/chat/CharacterAvatar.jsx
  - [ ] Avatar dynamique
  - [ ] Status indicator

### Character View Page
- [ ] 🔥 Créer pages/CharacterView.jsx
  - [ ] Split screen layout
  - [ ] Character sheet left
  - [ ] Chat interface right
  - [ ] Responsive mobile

---

## Phase 12 : Frontend - Journal & Timeline (Semaine 14)

### Journal Components
- [ ] ⏳ Créer components/journal/JournalViewer.jsx
  - [ ] Liste entrées journal
  - [ ] Filtres par date
  - [ ] Search

- [ ] ⏳ Créer components/journal/JournalEntry.jsx
  - [ ] Affichage entrée
  - [ ] Style manuscrit
  - [ ] Expand/collapse

- [ ] ⏳ Créer components/journal/Timeline.jsx
  - [ ] Timeline verticale
  - [ ] Phases personnage
  - [ ] Événements majeurs

### Journal Page
- [ ] ⏳ Créer pages/JournalPage.jsx
  - [ ] Intégrer JournalViewer
  - [ ] Intégrer Timeline
  - [ ] Tab navigation

---

## Phase 13 : Frontend - Home & Navigation (Semaine 15)

### Home Page
- [ ] 🔥 Créer pages/Home.jsx
  - [ ] Liste personnages créés
  - [ ] Cards personnages
  - [ ] Bouton créer nouveau
  - [ ] Search/Filter personnages

### Navigation
- [ ] ⏳ Créer Header component
  - [ ] Logo WhytDD
  - [ ] Navigation links
  - [ ] User menu (futur)

### API Integration
- [ ] 🔥 Créer api/client.js
  - [ ] Axios instance
  - [ ] Base URL config
  - [ ] Interceptors

- [ ] 🔥 Créer api/characterApi.js
  - [ ] create()
  - [ ] get()
  - [ ] list()
  - [ ] update()
  - [ ] delete()

- [ ] 🔥 Créer api/chatApi.js
  - [ ] sendMessage()
  - [ ] getHistory()

- [ ] ⏳ Créer api/journalApi.js
  - [ ] getJournal()
  - [ ] getTimeline()

---

## Phase 14 : Hooks & Stores (Semaine 15)

### Custom Hooks
- [ ] 🔥 Créer hooks/useCharacter.js
  - [ ] React Query integration
  - [ ] CRUD operations
  - [ ] Cache management

- [ ] 🔥 Créer hooks/useChat.js
  - [ ] Message sending
  - [ ] History loading
  - [ ] Real-time updates

- [ ] ⏳ Créer hooks/useDiceRoller.js
  - [ ] Dice rolling logic
  - [ ] Animation state

- [ ] ⏳ Créer hooks/useJournal.js
  - [ ] Fetch journal
  - [ ] Pagination

### Zustand Stores
- [ ] ⏳ Créer stores/characterStore.js
  - [ ] currentCharacter
  - [ ] setCharacter
  - [ ] updateCharacter

- [ ] ⏳ Créer stores/chatStore.js
  - [ ] messages
  - [ ] addMessage
  - [ ] clearMessages

---

## Phase 15 : Styling & Polish (Semaine 16)

### Styles D&D
- [ ] 🔥 Implémenter palette couleurs D&D
- [ ] 🔥 Configurer fonts médiévales
- [ ] ⏳ Créer textures (parchemin, cuir)
- [ ] ⏳ Créer animations (dés, shimmer or)
- [ ] ⏳ Responsive design tous écrans
- [ ] ⏳ Dark mode (donjon)

### Assets
- [ ] ⏳ Trouver/créer icônes classes
- [ ] ⏳ Trouver/créer icônes races
- [ ] ⏳ Texture parchemin
- [ ] ⏳ Texture cuir
- [ ] ⏳ Images dés 3D

---

## Phase 16 : Testing & Debugging (Semaine 17-18)

### Tests Backend
- [ ] ⏳ Tests unitaires tous modules
- [ ] ⏳ Tests intégration API
- [ ] ⏳ Tests RAG retrieval qualité
- [ ] ⏳ Tests génération GGUF
- [ ] ⏳ Tests performance ChromaDB

### Tests Frontend
- [ ] ⏳ Tests composants (Vitest)
- [ ] ⏳ Tests E2E (Playwright)
- [ ] ⏳ Tests responsive
- [ ] ⏳ Tests accessibilité

### Debugging
- [ ] ⏳ Fix bugs backend
- [ ] ⏳ Fix bugs frontend
- [ ] ⏳ Optimisation performance
- [ ] ⏳ Memory leaks check

---

## Phase 17 : Documentation (Semaine 19)

### Documentation Utilisateur
- [ ] 📝 Guide utilisation application
- [ ] 📝 Guide création personnage
- [ ] 📝 Guide conversation avec personnage
- [ ] 📝 FAQ

### Documentation Développeur
- [ ] 📝 Setup instructions
- [ ] 📝 Architecture détaillée
- [ ] 📝 API documentation
- [ ] 📝 Code comments
- [ ] 📝 Contributing guide

---

## Phase 18 : Deployment (Semaine 20)

### Backend Deployment
- [ ] ⏳ Dockerfile backend
- [ ] ⏳ Docker-compose setup
- [ ] ⏳ Environment variables production
- [ ] ⏳ Deploy backend (serveur/cloud)

### Frontend Deployment
- [ ] ⏳ Build production optimisé
- [ ] ⏳ Deploy frontend (Vercel/Netlify)
- [ ] ⏳ Configure API endpoints production

### Database
- [ ] ⏳ Setup ChromaDB persistance
- [ ] ⏳ Backup strategy
- [ ] ⏳ Migration scripts

---

## Features Futures (Post-MVP)

### V2.0 - Améliorations
- [ ] ⏳ Multi-personnages dans conversation
- [ ] ⏳ Combat simulator intégré
- [ ] ⏳ Jet de dés automatique
- [ ] ⏳ Gestion inventaire avancée
- [ ] ⏳ Système de quêtes
- [ ] ⏳ Relation entre personnages
- [ ] ⏳ Export feuille personnage PDF

### V3.0 - Mode Campagne
- [ ] ⏳ Mode Maître du Donjon
- [ ] ⏳ Gestion groupe aventuriers
- [ ] ⏳ Carte monde interactive
- [ ] ⏳ PNJ persistants
- [ ] ⏳ Gestion session de jeu

### V4.0 - Advanced
- [ ] ⏳ Text-to-Speech personnage
- [ ] ⏳ Génération image personnage (SD)
- [ ] ⏳ Mode multijoueur
- [ ] ⏳ Mobile app (React Native)
- [ ] ⏳ VR/AR support

---

## Priorités Immédiates 🔥

1. **Documentation Immersive** - Sans ça, personnages pas immersifs
2. **Behavioral Translator** - Cœur de la traduction stats → comportement
3. **RAG Engine complet** - Système de mémoire
4. **LLM Interface** - Génération réponses
5. **API Routes principales** - Create character + Chat
6. **Frontend Creator** - Interface création
7. **Frontend Chat** - Interface conversation

---

## Notes Importantes

- **Ne pas coder avant d'avoir** :
  - ✅ Documentation immersive complète
  - ✅ Architecture validée
  - ✅ Tests setup prêt

- **Tester au fur et à mesure** :
  - Chaque module doit avoir tests unitaires
  - Tests intégration après chaque phase

- **Garder focus sur MVP** :
  - Créer personnage simple
  - Converser avec personnage
  - Journal basique
  - Features avancées = V2+

---

**Dernière mise à jour** : 2025-10-04
**Estimation totale** : 20 semaines (5 mois)
**MVP réaliste** : 12 semaines (3 mois)
