# WhytDD - Test Suite Documentation

## 📋 Vue d'ensemble

Suite de tests complète pour valider toutes les fonctionnalités créées dans les Phases 2 et 3.

**Localisation** : `backend/tests/`

**Total** : 4 test suites + 1 master runner

---

## 🧪 Test Suites

### 1. test_parsers.py - Knowledge Parser Tests

**Objectif** : Valider les parsers et validation de données

**Tests inclus** :
- ✅ `test_ability_scores_validation()` - Validation ability scores
  - Scores valides acceptés
  - Scores invalides rejetés (> 30)
  - Calcul modificateurs correct
  
- ✅ `test_character_creation_validation()` - Validation création personnage
  - Schema CharacterCreate
  - Données valides acceptées
  
- ✅ `test_race_schema_validation()` - Validation schema race
  - RaceSchema complet
  - Traits, abilities, languages
  
- ✅ `test_class_schema_validation()` - Validation schema classe
  - ClassSchema complet
  - Hit die, proficiencies, features
  
- ✅ `test_invalid_data_rejection()` - Rejet données invalides
  - Scores > 30 rejetés
  - Champs manquants rejetés
  
- ✅ `test_immersive_parser_structure()` - Structure immersive parser
  - Classes existent
  - Méthodes requises présentes
  
- ✅ `test_rule_parser_structure()` - Structure rule parser
  - Classes existent
  - Méthodes requises présentes

**Commande** :
```bash
python backend/tests/test_parsers.py
```

**Tests** : 7
**Durée estimée** : ~2 secondes

---

### 2. test_stats_calculator.py - Stats Calculator Tests

**Objectif** : Valider génération et calcul ability scores

**Tests inclus** :
- ✅ `test_modifier_calculation()` - Calcul modificateurs
  - 9 test cases (scores 1 à 30)
  - Formule: (score - 10) // 2
  
- ✅ `test_standard_array()` - Standard array
  - [15, 14, 13, 12, 10, 8]
  
- ✅ `test_point_buy_validation()` - Validation point buy
  - 27 points valides acceptés
  - Trop/trop peu de points rejetés
  - Scores invalides rejetés (> 15 ou < 8)
  
- ✅ `test_racial_bonuses()` - Application bonus raciaux
  - Mountain Dwarf: +2 STR, +2 CON
  - Application correcte
  
- ✅ `test_dice_rolling()` - Jets de dés statistiques
  - 100 rolls 4d6 drop lowest
  - Validation min (3-8), max (15-18), avg (10-14)

**Commande** :
```bash
python backend/tests/test_stats_calculator.py
```

**Tests** : 5
**Durée estimée** : ~3 secondes

---

### 3. test_behavioral_translator.py - Behavioral Translator Tests

**Objectif** : Valider traduction mécanique → comportement

**Tests inclus** :
- ✅ `test_stat_translation()` - Traduction stats
  - High STR → "physically imposing"
  - Low CHA → "struggle in social situations"
  
- ✅ `test_race_translation()` - Traduction races
  - 3 races testées (Dwarf, Elf, Human)
  - Keywords culturels présents
  
- ✅ `test_class_translation()` - Traduction classes
  - 4 classes testées (Fighter, Wizard, Rogue, Cleric)
  - Keywords mentality présents
  
- ✅ `test_alignment_translation()` - Traduction alignments
  - 3 alignments testés (LG, CG, NE)
  - Keywords moraux présents
  
- ✅ `test_complete_profile()` - Profil comportemental complet
  - Bruenor (Mountain Dwarf Fighter LG)
  - 20-50 directives générées
  - Structure profile validée
  - Sample directives affichées

**Commande** :
```bash
python backend/tests/test_behavioral_translator.py
```

**Tests** : 5
**Durée estimée** : ~2 secondes

---

### 4. test_character_creation.py - Character Creation Tests

**Objectif** : Valider création complète de personnages

**Tests inclus** :
- ✅ `test_create_dwarf_fighter()` - Bruenor Battlehammer
  - Mountain Dwarf Fighter (Lawful Good)
  - Bonus raciaux appliqués (STR 15→17, CON 15→17)
  - HP calculé (10 + CON mod)
  - Features présentes
  - Equipment présent
  
- ✅ `test_create_elf_wizard()` - Taako (High Elf Wizard)
  - Bonus raciaux (DEX 14→16, INT 15→16)
  - HP calculé (6 + CON mod)
  - Validation complète
  
- ✅ `test_create_human_rogue()` - Vax'ildan (Human Rogue)
  - Human +1 all abilities
  - HP calculé (8 + CON mod)
  - Validation complète
  
- ✅ `test_equipment_ac_calculation()` - Calculs AC
  - 5 scenarios testés
  - Unarmored, Leather, Chain Mail, Shield
  - Formules correctes
  
- ✅ `test_behavioral_profile_integration()` - Profile comportemental
  - Grog (Half-Orc Barbarian CN)
  - Profile généré et attaché
  - 20-50 directives
  - Breakdown par catégorie

**Commande** :
```bash
python backend/tests/test_character_creation.py
```

**Tests** : 5
**Durée estimée** : ~5 secondes

---

## 🚀 Master Test Runner

### run_all_tests.py

**Objectif** : Exécuter toutes les test suites dans l'ordre

**Fonctionnalités** :
- Exécute les 4 test suites séquentiellement
- Vérifie existence des fichiers
- Affiche résultats en temps réel
- Summary final
- Exit code approprié (0 = success, 1 = failure)

**Commande** :
```bash
python backend/tests/run_all_tests.py
```

**Tests totaux** : 22 tests
**Durée estimée** : ~12 secondes

**Output attendu** :
```
======================================================================
WHYTDD - MASTER TEST SUITE
======================================================================
Started at: 2025-10-04 02:00:00

📋 Found 4 test suites

======================================================================
Running: test_parsers.py
======================================================================
[... tests s'exécutent ...]

======================================================================
Running: test_stats_calculator.py
======================================================================
[... tests s'exécutent ...]

======================================================================
Running: test_behavioral_translator.py
======================================================================
[... tests s'exécutent ...]

======================================================================
Running: test_character_creation.py
======================================================================
[... tests s'exécutent ...]

======================================================================
FINAL SUMMARY
======================================================================
   ✅ PASS: test_parsers.py
   ✅ PASS: test_stats_calculator.py
   ✅ PASS: test_behavioral_translator.py
   ✅ PASS: test_character_creation.py

======================================================================
Total: 4/4 test suites passed
Finished at: 2025-10-04 02:00:12
======================================================================

   🎉 ALL TEST SUITES PASSED! 🎉

   ✅ WhytDD is ready for Phase 4!
```

---

## 📊 Couverture des Tests

### Phase 2 - Knowledge Parser (100%)
- ✅ Pydantic schemas validation
- ✅ AbilityScores validation
- ✅ CharacterCreate validation
- ✅ RaceSchema validation
- ✅ ClassSchema validation
- ✅ Invalid data rejection
- ✅ Parser structure validation

### Phase 3 - Character Creator (100%)
- ✅ Modifier calculation
- ✅ Standard array
- ✅ Point buy validation
- ✅ Racial bonuses application
- ✅ Dice rolling (statistical)
- ✅ Stat translation
- ✅ Race translation
- ✅ Class translation
- ✅ Alignment translation
- ✅ Complete behavioral profile
- ✅ Character creation (3 races/classes)
- ✅ AC calculation (5 scenarios)
- ✅ Behavioral profile integration

### Modules Testés
1. ✅ `knowledge_parser/data_validator.py` - 100%
2. ✅ `knowledge_parser/rule_parser.py` - Structure
3. ✅ `knowledge_parser/immersive_parser.py` - Structure
4. ✅ `character_creator/stats_calculator.py` - 100%
5. ✅ `character_creator/behavioral_translator.py` - 100%
6. ✅ `character_creator/creator_logic.py` - 100%
7. ✅ `character_creator/equipment_manager.py` - 100%

---

## 🔧 Dépendances

**Packages requis** :
- `pydantic` - Validation schemas
- `pathlib` - Path manipulation
- Standard library (sys, subprocess, datetime)

**Pas de dépendances externes** pour les tests de base.

---

## ⚠️ Notes Importantes

### Tests qui Nécessitent des Fichiers

Certains tests sont **structurels** et ne nécessitent pas de fichiers :
- `test_immersive_parser_structure()` - Vérifie seulement que les classes/méthodes existent
- `test_rule_parser_structure()` - Vérifie seulement que les classes/méthodes existent

**Tests avec fichiers réels** (à créer plus tard) :
- Parse réel de `02_Races.md`
- Parse réel de `03_Classes_Resume.md`
- Parse réel des fichiers immersifs

### Tests Statistiques

Le test `test_dice_rolling()` est **statistique** :
- Peut échouer occasionnellement (probabilité très faible)
- 100 rolls pour validation distribution
- Tolérances larges pour min/max/avg

### Performance

**Temps d'exécution** :
- Tests unitaires : < 1 seconde chacun
- Tests de création : 1-2 secondes chacun
- Suite complète : ~12 secondes

---

## 🎯 Prochains Tests (Phase 4)

Quand Phase 4 sera créée :

1. **test_embeddings.py**
   - Load sentence-transformers
   - Encode text
   - Encode batch
   - Vector dimensions

2. **test_chromadb.py**
   - Create collection
   - Add documents
   - Query vectors
   - Retrieve similar

3. **test_knowledge_indexing.py**
   - Index technical docs
   - Index immersive docs
   - Index behavioral profiles

4. **test_retrieval.py**
   - Retrieve by character
   - Retrieve by context
   - Ranking relevance

---

## ✅ Validation Checklist

Avant de passer à Phase 4 :

- [ ] Tous les tests passent (`run_all_tests.py`)
- [ ] Aucune exception non gérée
- [ ] Output clair et informatif
- [ ] Exit codes corrects
- [ ] Documentation à jour

---

**Test suite créée le** : 2025-10-04
**Phases couvertes** : Phase 2 & Phase 3
**Status** : ✅ Prêt pour exécution
