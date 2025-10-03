# Système de Jeu - D&D 5e

## Le d20 : Cœur du Système

### Principe Fondamental

Presque toutes les actions incertaines se résolvent avec un **d20** :
```
d20 + Modificateurs ≥ Degré de Difficulté (DD)
```

### Les Trois Types de Jets

1. **Jets de Caractéristique**
2. **Jets d'Attaque**
3. **Jets de Sauvegarde**

## Jets de Caractéristique

### Quand Utiliser

Quand un personnage tente une action dont l'issue est incertaine :
- Escalader une falaise
- Persuader un garde
- Déchiffrer un texte ancien
- Détecter un piège

### Formule

```
d20 + Modificateur de Caractéristique + Bonus de Maîtrise (si applicable) ≥ DD
```

### Avec ou Sans Maîtrise

**Avec maîtrise** (compétence ou outil maîtrisé) :
- Ajouter le **bonus de maîtrise** (+2 à +6)

**Sans maîtrise** :
- Seulement le modificateur de caractéristique

**Exemple** :
- Escalade (Force), niveau 3, Force 16 (+3), maîtrise Athlétisme
- Jet : d20 + 3 (Force) + 2 (maîtrise) = d20 + 5

### Les 18 Compétences

**Force (FOR)**
- Athlétisme

**Dextérité (DEX)**
- Acrobaties
- Discrétion
- Escamotage

**Intelligence (INT)**
- Arcanes
- Histoire
- Investigation
- Nature
- Religion

**Sagesse (SAG)**
- Dressage
- Intuition
- Médecine
- Perception
- Survie

**Charisme (CHA)**
- Intimidation
- Persuasion
- Représentation
- Supercherie

### Tests Passifs

Certaines situations utilisent des **valeurs passives** (pas de jet) :

```
10 + tous les modificateurs applicables
```

**Perception passive** (la plus courante) :
```
10 + mod. Sagesse + bonus maîtrise (si Perception maîtrisée)
```

**Utilité** :
- MD l'utilise pour comparer discrètement
- Détecter embuscades
- Remarquer détails

## Degré de Difficulté (DD)

### Table des DD

| DD | Difficulté |
|----|------------|
| 5 | Très facile |
| 10 | Facile |
| 15 | Moyen |
| 20 | Difficile |
| 25 | Très difficile |
| 30 | Quasi impossible |

### DD Courants par Tâche

**Athlétisme/Acrobaties** :
- Escalader surface rugueuse : DD 10
- Escalader mur lisse : DD 20
- Sauter 3m en hauteur : DD 20

**Discrétion** :
- Se cacher : vs Perception passive
- Se déplacer silencieusement : DD 10-15

**Persuasion/Intimidation** :
- Convaincre personne amicale : DD 10
- Convaincre personne neutre : DD 15
- Convaincre personne hostile : DD 20

## Jets d'Attaque

### Formule

```
d20 + Bonus d'Attaque ≥ Classe d'Armure (CA) de la cible
```

### Bonus d'Attaque

**Armes de mêlée** :
```
Mod. Force + Bonus Maîtrise (si arme maîtrisée)
```

**Armes de finesse** (rapière, dague, etc.) :
```
Mod. Force OU Mod. Dextérité + Bonus Maîtrise
```

**Armes à distance** :
```
Mod. Dextérité + Bonus Maîtrise
```

**Armes de lancer** :
```
Mod. Force + Bonus Maîtrise (mêlée ou lancé)
```

**Sorts** :
```
Mod. Caractéristique Magique + Bonus Maîtrise
```

### En Cas de Toucher

Lancer les **dés de dégâts** de l'arme/sort + modificateur

**Exemple** :
- Épée longue : 1d8 + mod. Force
- Boule de feu : 8d6 (pas de modificateur)

### Coups Critiques

**20 naturel** (le d20 montre 20) :
- Touche automatiquement
- **Doubler les dés de dégâts** (pas les modificateurs)
- Exemple : 1d8+3 devient 2d8+3

**1 naturel** (le d20 montre 1) :
- Échec automatique

## Jets de Sauvegarde

### Quand Utiliser

Quand une créature tente de **résister** à un effet :
- Éviter un sort
- Résister à un poison
- Échapper à un piège

### Formule

```
d20 + Modificateur de Caractéristique + Bonus Maîtrise (si maîtrisé) ≥ DD
```

### DD des Sorts

```
DD = 8 + Bonus Maîtrise + Mod. Caractéristique Magique du lanceur
```

**Exemple** :
- Magicien niveau 5, Intelligence 16 (+3)
- DD sorts = 8 + 3 (maîtrise) + 3 (Int) = 14

### Résultat

**Réussite** : Évite l'effet ou subit la moitié des dégâts
**Échec** : Subit l'effet complet

## Avantage et Désavantage

### Avantage

**Lancer 2d20, prendre le meilleur résultat**

**Situations donnant avantage** :
- Attaquer une cible inconsciente
- Attaquer une cible invisible que vous voyez
- Aider un allié
- Conditions favorables (surprise, terrain idéal, etc.)
- Certaines capacités de classe

### Désavantage

**Lancer 2d20, prendre le pire résultat**

**Situations donnant désavantage** :
- Attaquer en étant invisible
- Attaquer au-delà de portée normale
- Combat rapproché avec arme à distance
- Conditions défavorables (obscurité, entravé, etc.)

### Règle Importante

**Avantage et désavantage s'annulent** :
- Plusieurs sources d'avantage = 1 avantage
- Plusieurs sources de désavantage = 1 désavantage
- Si les deux : jet normal

## Bonus de Maîtrise

### Progression

| Niveau | Bonus |
|--------|-------|
| 1-4    | +2    |
| 5-8    | +3    |
| 9-12   | +4    |
| 13-16  | +5    |
| 17-20  | +6    |

### Application

S'applique à :
- Jets de caractéristique (compétences maîtrisées)
- Jets d'attaque (armes maîtrisées)
- Jets de sauvegarde (maîtrisés)
- DD des sorts
- Certaines capacités de classe

**Règle d'or** : Ne s'applique qu'**une seule fois** par jet

### Expertise

Certaines capacités (Barde, Roublard) donnent **Expertise** :
```
Double le bonus de maîtrise pour une compétence
```

**Exemple** :
- Niveau 5 (maîtrise +3), Expertise en Discrétion
- Bonus total Discrétion : +6 (au lieu de +3)

## Actions en Jeu

### Action Standard

**1 action par tour** parmi :
- **Attaquer**
- **Lancer un sort** (1 action)
- **Foncer** (double mouvement)
- **Se désengager** (éviter attaques opportunité)
- **Esquiver** (désavantage contre vous)
- **Se cacher**
- **Aider** (donner avantage à un allié)
- **Chercher** (trouver quelque chose)
- **Utiliser un objet**
- **Préparer** (action conditionnelle)

### Action Bonus

**1 action bonus par tour** (si capacité le permet) :
- Combat à deux armes
- Sorts spécifiques (sort accéléré)
- Capacités de classe (Rage du barbare, Ki du moine, etc.)

**Important** : Pas d'action bonus "par défaut"

### Réaction

**1 réaction par round** :
- **Attaque d'opportunité** (ennemi sort de votre portée)
- Sorts avec temps d'incantation "réaction" (Bouclier, etc.)
- Capacités spécifiques

**Se recharge au début de votre tour**

### Mouvement

**Distance = Vitesse du personnage** (généralement 9 m ou 7,50 m)
- Peut être divisé (3m → action → 6m)
- Terrain difficile = 2× distance

### Action Gratuite

Actions très rapides :
- Lâcher un objet
- Parler brièvement
- Interaction objet simple

## Repos

### Repos Court

**Durée** : Au moins 1 heure
**Activités** : Repos léger (manger, soigner, lire)

**Récupération** :
- **Dés de vie** : Dépenser pour récupérer PV (1 dé = 1d[dé]+mod.Con)
- Certaines capacités (Action surge, Rage, etc.)

### Repos Long

**Durée** : Au moins 8 heures
**Activités** : Dormir ou activité légère (max 2h de veille)

**Récupération** :
- **Tous les points de vie**
- **Moitié des dés de vie dépensés** (minimum 1)
- **Emplacements de sorts**
- **Toutes les capacités limitées**

**Limitation** : 1 repos long par période de 24h

## Conditions

### Conditions Principales

**Aveuglé**
- Échec automatique tests visuels
- Désavantage attaques
- Avantage aux attaques contre vous

**Charmé**
- Ne peut attaquer le charmeur
- Charmeur a avantage aux interactions sociales

**Assourdi**
- Échec automatique tests auditifs

**Effrayé**
- Désavantage tests et attaques tant que source visible
- Ne peut approcher source

**Empoigné**
- Vitesse = 0
- Fin si empoigneur incapable ou éloigné

**Entravé**
- Vitesse = 0
- Désavantage attaques et Dex
- Avantage aux attaques contre

**Invisible**
- Impossible à voir sans magie
- Avantage aux attaques
- Désavantage aux attaques contre

**Paralysé**
- Incapable d'agir
- Échec auto JdS For et Dex
- Avantage aux attaques contre
- Critiques automatiques si mêlée

**Pétrifié**
- Transformé en pierre
- Résistance à tous dégâts
- Immunité poison/maladie

**Empoisonné**
- Désavantage attaques et tests caractéristique

**À terre**
- Seulement ramper (vitesse/2)
- Désavantage attaques
- Désavantage attaques à distance contre
- Avantage attaques mêlée contre

**Entravé**
- Vitesse = 0
- Désavantage attaques et Dex
- Avantage attaques contre

**Étourdi**
- Incapable d'agir
- Échec auto JdS For et Dex
- Avantage attaques contre

**Inconscient**
- Incapable, ne peut bouger/parler
- Lâche objets
- Échec auto JdS For et Dex
- Avantage attaques contre
- Critiques auto si mêlée (5 pieds)

## Autres Règles Importantes

### Arrondir

**Toujours à l'inférieur**
- 7,5 → 7
- 15/2 = 7,5 → 7

### Particulier avant Général

**Les exceptions l'emportent** :
- Si règle spécifique contredit règle générale
- La règle spécifique s'applique

### Cumul des Effets

**Effets de même nom ne se cumulent pas** :
- Prendre le plus puissant
- Exception : dégâts et soins se cumulent toujours

### Vision et Lumière

**Lumière vive** : Vision normale

**Lumière faible** :
- Désavantage Perception visuelle
- Zone légèrement obscurcie

**Obscurité** :
- Zone très obscurcie
- Impossible de voir (aveuglé effectivement)

**Vision dans le noir** :
- Voir dans obscurité comme lumière faible
- Voir dans lumière faible comme lumière vive
- Portée variable (généralement 18m ou 36m)

### Abris

**Abri partiel (+2 CA et JdS Dex)**
- Obstacle couvre au moins moitié

**Abri important (+5 CA et JdS Dex)**
- Obstacle couvre au moins 3/4

**Abri total (ne peut être ciblé)**
- Complètement couvert

### Portées des Armes

**Mêlée** : Généralement 1,50 m

**À distance** :
- **Portée normale** : Pas de pénalité
- **Portée longue** : Désavantage
- **Au-delà** : Impossible

**Exemple** :
- Arc court : 24/96 m
- Attaque normale jusqu'à 24m
- Désavantage 24m-96m
- Impossible au-delà de 96m

### Concentration

**Certains sorts nécessitent Concentration** :
- 1 seul sort de concentration à la fois
- Prendre dégâts = JdS Constitution (DD 10 ou moitié dégâts)
- Échec = concentration perdue
- Lancer autre sort concentration = fin du précédent

### Dégâts et Résistances

**Résistance** : Diviser dégâts par 2

**Vulnérabilité** : Multiplier dégâts par 2

**Immunité** : 0 dégât

**Ordre d'application** :
1. Additionner tous bonus/pénalités
2. Appliquer résistance/vulnérabilité
3. Arrondir à l'inférieur

## Règles Maison Courantes

*Ces règles ne sont pas officielles mais populaires :*

**Critique 20 hors combat** : 20 naturel = succès automatique sur test caractéristique

**Règle de la mort héroïque** : 3 échecs en JdS mort = vraiment mort

**Potions en action bonus** : Boire potion = action bonus

**Flanquer** : Attaquer avec allié opposé = avantage

---

*Pour plus de détails sur le combat et la magie, consultez les fichiers spécifiques.*
