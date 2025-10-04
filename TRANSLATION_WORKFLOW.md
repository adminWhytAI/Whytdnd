# 🌐 Workflow de Traduction - Documentation Immersive

## 📋 Vue d'Ensemble

Guide complet pour traduire les documents immersifs du français vers l'anglais via une Pull Request GitHub.

**Branche créée** : `translate/immersive-docs-to-english`  
**Status** : ✅ Prête pour traduction

---

## 🚀 Étapes Complètes

### 1. Vérifier la Branche

```bash
# Vérifier que vous êtes sur la bonne branche
git branch

# Devrait afficher: * translate/immersive-docs-to-english
```

### 2. Traduire les Fichiers avec GitHub Copilot

#### Méthode Recommandée: GitHub Copilot

Pour chaque fichier à traduire :

1. **Ouvrir le fichier français** dans VS Code
2. **Sélectionner tout le contenu** (Ctrl+A)
3. **Ouvrir Copilot Chat** (Ctrl+Shift+I)
4. **Utiliser ce prompt** :

```
Translate this D&D 5e immersive documentation from French to English.

Requirements:
- Maintain first-person perspective ("I am" not "He is")
- Use official D&D 5e terminology
- Preserve emotional depth and authenticity
- Keep markdown structure identical
- Make it sound natural in English (not literal)
- Adapt cultural expressions (e.g., "Par la barbe" → "By my beard")

Character voice must remain authentic and immersive.
```

5. **Copier la traduction**
6. **Créer nouveau fichier** avec même nom
7. **Coller et réviser** la traduction
8. **Vérifier qualité**

### 3. Fichiers à Traduire (dans l'ordre)

#### Priorité 1 : Races & Classes
```
1. Documentation/Immersive/Races/Being_A_Dwarf_Mountain.md
   → Expressions naines, culture clan, forge

2. Documentation/Immersive/Classes/Being_A_Fighter.md
   → Discipline, entraînement, combat
```

#### Priorité 2 : Stats
```
3. Documentation/Immersive/Stats/Having_High_Strength.md
   → Puissance physique, dominance

4. Documentation/Immersive/Stats/Having_Low_Intelligence.md
   → Langage simple, pensée directe
```

#### Priorité 3 : Alignments
```
5. Documentation/Immersive/Alignments/Living_Lawful_Good.md
   → Honneur, justice, principes
```

### 4. Points Clés de Traduction

#### Expressions Culturelles

**Dwarf (Nain)**
| Français | English |
|----------|---------|
| Par la barbe de mes ancêtres ! | By my ancestors' beards! |
| Dur comme la pierre | Hard as stone |
| L'honneur du clan | Clan honor |
| Forge et enclume | Forge and anvil |

**Fighter (Guerrier)**
| Français | English |
|----------|---------|
| Je m'entraîne chaque jour | I train every day |
| Discipline avant tout | Discipline above all |
| Analyser l'adversaire | Analyze the opponent |

**Low Intelligence**
| Français | English |
|----------|---------|
| Moi pas comprendre | Me not understand |
| Trop compliqué | Too hard |
| Faire simple | Keep simple |

**Lawful Good**
| Français | English |
|----------|---------|
| Je garde ma parole | I keep my word |
| La justice avant tout | Justice above all |
| Mon honneur me guide | My honor guides me |

#### Termes Techniques D&D 5e

| Français | English |
|----------|---------|
| Guerrier | Fighter |
| Nain des Montagnes | Mountain Dwarf |
| Nain des Collines | Hill Dwarf |
| Loyal Bon | Lawful Good |
| Force | Strength |
| Dextérité | Dexterity |
| Constitution | Constitution |
| Intelligence | Intelligence |
| Sagesse | Wisdom |
| Charisme | Charisma |
| Vision dans le noir | Darkvision |
| Résistance naine | Dwarven Resilience |

### 5. Checklist Qualité par Fichier

Pour chaque fichier traduit, vérifier :

- [ ] **Perspective** : Tout en "I/me/my" (1ère personne)
- [ ] **Émotion** : Le sentiment immersif est préservé
- [ ] **Termes** : Terminologie D&D 5e officielle
- [ ] **Naturel** : Ça sonne anglais natif (pas littéral)
- [ ] **Structure** : Markdown identique (headers, listes)
- [ ] **Longueur** : Word count similaire (~±10%)
- [ ] **Voice** : Personnalité du personnage claire

### 6. Commit les Traductions

Après avoir traduit TOUS les fichiers :

```bash
# Ajouter les nouveaux fichiers
git add Documentation/Immersive/

# Vérifier ce qui va être commité
git status

# Commiter avec message descriptif
git commit -m "🌐 Translate immersive docs: French → English

- Translated Being_A_Dwarf_Mountain.md
- Translated Being_A_Fighter.md
- Translated Having_High_Strength.md
- Translated Having_Low_Intelligence.md
- Translated Living_Lawful_Good.md

Used GitHub Copilot with manual review for authenticity.
All official D&D 5e terminology applied.
First-person perspective and emotional depth maintained.

Total: ~10,800 words translated"
```

### 7. Push la Branche

```bash
# Push vers GitHub
git push origin translate/immersive-docs-to-english
```

### 8. Créer la Pull Request sur GitHub

1. **Aller sur GitHub** : https://github.com/adminWhytAI/Whytdnd
2. **Cliquer "Compare & pull request"** (apparaît automatiquement après push)
3. **Remplir le template** :
   - Cocher les fichiers traduits
   - Cocher la checklist qualité
   - Ajouter exemples de traduction
4. **Assignee** : @adminWhytAI
5. **Labels** : `documentation`, `translation`, `phase-1`, `immersive-docs`
6. **Create Pull Request**

### 9. Review & Merge

1. **Review** : Vérifier la qualité sur GitHub
2. **Demander modifications** si nécessaire
3. **Approve** quand satisfait
4. **Merge** dans main

### 10. Après le Merge

```bash
# Retourner sur main
git checkout main

# Pull les changements
git pull origin main

# Supprimer la branche locale (optionnel)
git branch -d translate/immersive-docs-to-english
```

Puis mettre à jour :
- [ ] `TODO.md` - Marquer traductions complètes
- [ ] `PHASE1_PROGRESS.md` - Update status

---

## 🎨 Exemple de Traduction

### Avant (Français)

```markdown
## Forme Physique

Je suis trapu et dense, tout en muscles et en os solide. 
Ma barbe est épaisse, symbole de mon âge et de ma sagesse.

### Combat

Par la barbe de mes ancêtres ! Quand je brandis ma hache, 
mes ennemis tremblent. Je suis un mur vivant.
```

### Après (English)

```markdown
## Physical Form

I am stocky and dense, all muscle and solid bone.
My beard is thick, a symbol of my age and wisdom.

### Combat

By my ancestors' beards! When I raise my axe,
my enemies tremble. I am a living wall.
```

---

## ⚠️ Points d'Attention

### À FAIRE
✅ Utiliser GitHub Copilot pour traduction initiale  
✅ Réviser manuellement pour authenticité  
✅ Tester que ça sonne naturel en anglais  
✅ Vérifier termes D&D 5e officiels  
✅ Maintenir la voix du personnage  

### À NE PAS FAIRE
❌ Traduction littérale mot à mot  
❌ Perdre l'émotion/immersion  
❌ Changer la structure markdown  
❌ Utiliser terminologie non-officielle  
❌ Oublier la perspective 1ère personne  

---

## 🔧 Outils Utiles

### VS Code Extensions
- **GitHub Copilot** : Traduction assistée par IA
- **Grammarly** : Vérification grammaire anglaise
- **Code Spell Checker** : Orthographe
- **Markdown All in One** : Preview markdown

### Ressources D&D 5e
- **Player's Handbook** : Terminologie officielle
- **D&D Beyond** : Référence en ligne
- **Roll20 Wiki** : Termes rapides

---

## 📊 Tracking

### Status Fichiers

| Fichier | Status | Reviewer | Notes |
|---------|--------|----------|-------|
| Being_A_Dwarf_Mountain.md | ⏳ À faire | - | Priorité 1 |
| Being_A_Fighter.md | ⏳ À faire | - | Priorité 1 |
| Having_High_Strength.md | ⏳ À faire | - | Priorité 2 |
| Having_Low_Intelligence.md | ⏳ À faire | - | Priorité 2 |
| Living_Lawful_Good.md | ⏳ À faire | - | Priorité 3 |

**Temps estimé total** : 2-3 heures

---

## ✅ Checklist Finale

Avant de créer la PR, vérifier :

- [ ] Tous les 5 fichiers traduits
- [ ] Qualité vérifiée pour chaque fichier
- [ ] Commit fait avec message descriptif
- [ ] Push vers GitHub réussi
- [ ] Template PR rempli complètement
- [ ] Labels et assignee configurés

---

**Branche** : `translate/immersive-docs-to-english`  
**Créée le** : 2025-10-04  
**Prête pour** : Traduction avec GitHub Copilot  
**Priority** : HIGH 🔥
