# Discussion Architecture WhytDD - Système de Personnage D&D avec GGUF

**Date** : 3 octobre 2025

## Objectif du Projet

Créer un système permettant de **générer des personnages D&D 5e** selon les règles officielles et de **discuter avec eux via un modèle GGUF**, où le personnage devient véritablement vivant grâce à sa base de connaissances.

## Décision Clé : Architecture RAG au lieu de Prompt Statique

### ❌ Approche Rejetée : Prompt Système Prédéfini

**Problème** : Un prompt statique qui contient toutes les infos du personnage serait :
- Limité par la taille du contexte
- Figé et difficile à faire évoluer
- Inefficace (envoie tout à chaque message)
- Ne permet pas l'évolution du personnage

### ✅ Approche Retenue : Système RAG (Retrieval-Augmented Generation)

**Principe** : Le personnage est une **base de connaissances vivante** que le GGUF interroge dynamiquement.

**Fonctionnement** :
1. Toutes les données du personnage sont fragmentées et indexées vectoriellement
2. À chaque message utilisateur, le système récupère SEULEMENT les fragments pertinents
3. Le prompt est **auto-généré dynamiquement** avec ces fragments + contexte conversation
4. Le GGUF répond en incarnant le personnage avec les infos pertinentes
5. Nouvelles expériences sont ajoutées en temps réel à la base

## Structure de la Base de Connaissances

### Types de Données

**Données Immuables** (ne changent jamais)
- Race et traits raciaux
- Nom
- Valeurs de caractéristiques de base

**Données Semi-Statiques** (changent rarement)
- Niveau actuel
- Classe et capacités
- Compétences maîtrisées
- Équipement principal
- Relations établies

**Données Dynamiques** (évoluent constamment)
- Expériences vécues
- Conversations précédentes
- Quêtes en cours
- État émotionnel actuel
- Objets acquis
- PNJ rencontrés
- Évolution de personnalité

### Organisation des Fragments

Chaque fragment de connaissance contient :
- **Contenu** : L'information elle-même
- **Type** : Identité, personnalité, compétence, histoire, etc.
- **Priorité** : Critique (toujours inclus) / Haute / Moyenne / Basse
- **Temporalité** : Passé lointain / Passé / Récent / Présent
- **Métadonnées** : Catégorie, date, fréquence d'usage

## Exemple Concret : Conaosfeo le Paladin

### Timeline du Personnage

**Phase 1 : Paladin de la Vengeance**
```
Base de connaissances :
- "Je suis Conaosfeo, Paladin de la Vengeance"
- "J'ai juré de punir les coupables et protéger les innocents"
- "Capacités : Châtiment Divin, Aura de Protection"
- "Alignement : Loyal Bon"
```

**Phase 2 : Le Tournant (Meurtre d'Innocents)**
```
Événements ajoutés :
- "J'ai tué des innocents dans ma quête de vengeance"
- "J'ai trahi mon serment sacré"
- "Leur sang hante mes nuits"
- "Date et contexte de l'événement"
```

**Phase 3 : Transformation en Parjure**
```
Nouvelles données :
- "Je suis maintenant un Paladin Parjure"
- "J'ai perdu mes pouvoirs de Vengeance"
- "Nouvelles capacités : Toucher Maudit, Aura de Haine"
- "Alignement : Neutre Mauvais"
- "État émotionnel : Culpabilité/Rage/Déni"
```

### Le Système Conserve TOUTE l'Histoire

**Important** : Le personnage garde en mémoire :
- ✅ Qui il était (Paladin Vengeance)
- ✅ Ce qu'il a fait (Tué innocents)
- ✅ Comment il a changé (Devenu Parjure)
- ✅ Qui il est maintenant (Parjure avec capacités Ténèbres)
- ✅ Son état émotionnel face à son passé

**Chaque phase a une métadonnée temporelle** permettant au RAG de récupérer les infos pertinentes selon le contexte de la question.

## Workflow Technique

### À Chaque Message Utilisateur

1. **Message reçu** : "Parle-moi de ton serment"

2. **Transformation en embedding** : Le message devient un vecteur mathématique

3. **Recherche RAG** : Le système trouve les 5-10 fragments les plus pertinents
   - "J'étais Paladin de la Vengeance" [Phase 1]
   - "J'ai trahi mon serment" [Phase 2]
   - "Je suis maintenant Parjure" [Phase 3]
   - "Leur sang hante mes nuits" [État émotionnel]

4. **Construction du Prompt Auto-Généré** :
   ```
   Tu es Conaosfeo.
   
   Informations te concernant :
   - Tu étais Paladin de la Vengeance
   - Tu as trahi ton serment en tuant des innocents
   - Tu es maintenant un Paladin Parjure
   - Leur sang hante tes nuits
   
   [Derniers échanges conversation]
   
   Utilisateur : "Parle-moi de ton serment"
   
   Réponds en restant Conaosfeo :
   ```

5. **GGUF Génère Réponse** : Réponse cohérente avec le personnage et son évolution

6. **Enrichissement** : Le système peut extraire et ajouter de nouvelles infos de la conversation

## Avantages de Cette Approche

### 1. Pas de Limite de Taille
Le personnage peut avoir une histoire IMMENSE, seules les parties pertinentes sont envoyées au GGUF.

### 2. Évolution Naturelle
Nouvelles expériences ajoutées en temps réel :
- Montée de niveau
- Nouveaux objets magiques
- Relations développées
- Traumatismes
- Changements de personnalité

### 3. Cohérence Dynamique
Le personnage répond différemment selon le contexte :
- Question sur combat → Récupère compétences martiales
- Question sur histoire → Récupère backstory complète
- Question émotionnelle → Récupère personnalité + événements marquants

### 4. Mémoire à Long Terme
Contrairement à un prompt statique :
- Le personnage se souvient de TOUT
- Même des conversations d'il y a des mois
- Accessible via recherche sémantique

### 5. Multi-Personnages Efficace
Chaque personnage a sa propre base de connaissances. Le système bascule entre eux facilement.

## Technologies Nécessaires

### Backend
- **Python** avec FastAPI pour l'API REST
- **Sentence-transformers** : Génération d'embeddings locaux (multilingue français)
- **ChromaDB** : Base de données vectorielle locale (gratuite, rapide)
- **llama-cpp-python** : Interface avec le modèle GGUF

### Frontend
- **HTML/CSS/JavaScript** : Interface simple
- Page de création de personnage (formulaire)
- Interface de chat avec le personnage

### Structure Projet

```
WhytDD/
├── Documentation/              [✅ Documentation D&D créée]
├── gguf/                      [Modèles GGUF]
├── backend/
│   ├── rag_engine/            [Système RAG]
│   │   ├── embeddings/        [Génération embeddings]
│   │   ├── vectorstore/       [ChromaDB]
│   │   ├── knowledge_builder/ [Construction base]
│   │   └── retriever.py       [Orchestration]
│   ├── character_creator/     [Générateur personnage]
│   ├── llm_interface/         [Interface GGUF avec RAG]
│   └── api/                   [API REST]
├── frontend/
│   ├── character_creator.html [Création personnage]
│   ├── chat_interface.html    [Chat avec personnage]
│   └── js/css/
├── characters/                 [Stockage personnages]
└── character_knowledge/        [Bases de connaissances]
    └── [character_id]/
        ├── core_identity.json
        ├── personality.json
        ├── backstory.json
        ├── experiences/
        └── vector_db/          [Embeddings ChromaDB]
```

## Workflow Utilisateur Final

1. **Création** : Formulaire web → Personnage généré selon règles D&D
2. **Indexation** : Toutes données fragmentées et vectorisées (quelques secondes)
3. **Chat** : Interface de discussion
4. **Conversation** : 
   - RAG récupère infos pertinentes
   - GGUF génère réponse cohérente
   - Expériences enrichissent la base
5. **Évolution** : Le personnage grandit avec ses aventures

## Cas d'Usage Avancés

### Montée de Niveau
Ajouter simplement nouvelles capacités et stats à la base. Le personnage en parle naturellement si pertinent.

### Objets Magiques
"Je possède Dawnbringer, une épée solaire légendaire"
Le personnage mentionne son arme quand approprié.

### Relations Évolutives
"Je déteste les elfes" → après aventures → "Je respecte Legolas"
Le RAG récupère l'info la plus récente avec contexte historique.

### Traumatismes
"Depuis la mort de mon ami, je suis plus méfiant"
Impact persistant dans les réponses futures.

## Points Clés de la Discussion

### Confirmation : Prompt Auto-Généré

✅ **OUI** : Le prompt est reconstruit à chaque message
✅ **OUI** : Il se met à jour selon fiche personnage, stats, histoire
✅ **OUI** : Toutes les phases d'évolution sont conservées
✅ **OUI** : Le personnage garde le contexte de son background complet

### Le Personnage Est Vraiment Vivant

Le système RAG permet au personnage de :
- Se souvenir de tout son passé
- Évoluer avec ses expériences
- Répondre de manière cohérente et contextualisée
- Avoir une vraie profondeur émotionnelle
- Grandir et changer avec le temps

**Sans jamais** :
- Surcharger le contexte du GGUF
- Oublier son histoire
- Se contredire
- Être limité par un prompt figé

## Prochaines Étapes

1. Implémenter le générateur de personnages (règles D&D 5e)
2. Créer le système de fragmentation et d'indexation
3. Développer l'interface RAG avec ChromaDB
4. Intégrer le GGUF avec le système de prompts dynamiques
5. Créer les interfaces frontend (création + chat)
6. Tests avec des personnages complets et évolutifs

---

## Ajouts Architecture et Planning

### Fichiers Créés

**ARCHITECTURE.md** :
- Arborescence complète du projet
- Liste tous les fichiers avec imports et classes
- Liaisons inter-fichiers détaillées
- Flux de données complets
- Configuration requise

**TODO.md** :
- Todolist exhaustive (20 semaines)
- Phases structurées par modules
- Priorités identifiées
- Timeline MVP : 12 semaines
- Features futures V2.0+

### Stack Finale Validée

**Backend** :
- Python 3.10+ / FastAPI
- ChromaDB (base vectorielle)
- sentence-transformers (embeddings)
- llama-cpp-python (GGUF)

**Frontend** :
- React 18 + Vite
- TailwindCSS + shadcn/ui (thème D&D médiéval)
- React Query + Zustand
- React Router

### Documentation Requise

**Documentation Immersive (PRIORITÉ)** :
- 13 races en 1ère personne (Being_A_Dwarf.md, etc.)
- 12 classes en 1ère personne (Being_A_Fighter.md, etc.)
- Stats high/low (Having_High_Strength.md, etc.)
- 9 alignements vécus (Living_Lawful_Good.md, etc.)

**But** : Le GGUF doit "devenir" le personnage, pas le "décrire"

### Double Documentation Confirmée

**Technical (existante)** : Pour le système, calculs, mécaniques

**Immersive (à créer)** : Pour le GGUF, expérience 1ère personne

---

**Cette approche transforme un simple chatbot en un véritable personnage D&D vivant avec mémoire, personnalité et évolution authentique.**
