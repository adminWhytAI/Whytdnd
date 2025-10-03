"""
Data Validator - Pydantic schemas for validating D&D data structures
"""
from typing import Dict, List, Optional, Literal
from pydantic import BaseModel, Field, validator


# ============================================================================
# ABILITY SCORES
# ============================================================================

class AbilityScores(BaseModel):
    """D&D 5e ability scores"""
    strength: int = Field(ge=1, le=30, description="Strength score")
    dexterity: int = Field(ge=1, le=30, description="Dexterity score")
    constitution: int = Field(ge=1, le=30, description="Constitution score")
    intelligence: int = Field(ge=1, le=30, description="Intelligence score")
    wisdom: int = Field(ge=1, le=30, description="Wisdom score")
    charisma: int = Field(ge=1, le=30, description="Charisma score")
    
    @validator('*')
    def validate_ability_score(cls, v):
        """Ensure ability scores are in valid range"""
        if not 1 <= v <= 30:
            raise ValueError(f"Ability score must be between 1 and 30, got {v}")
        return v
    
    def get_modifier(self, ability: str) -> int:
        """Calculate ability modifier"""
        score = getattr(self, ability.lower())
        return (score - 10) // 2
    
    class Config:
        schema_extra = {
            "example": {
                "strength": 16,
                "dexterity": 14,
                "constitution": 15,
                "intelligence": 10,
                "wisdom": 12,
                "charisma": 8
            }
        }


# ============================================================================
# RACE SCHEMAS
# ============================================================================

class RacialTrait(BaseModel):
    """A racial trait or feature"""
    name: str = Field(..., description="Trait name")
    description: str = Field(..., description="Trait description")
    mechanical_effect: Optional[str] = Field(None, description="Game mechanical effect")


class SubraceSchema(BaseModel):
    """Subrace information"""
    name: str = Field(..., description="Subrace name")
    ability_score_increase: Dict[str, int] = Field(
        default_factory=dict,
        description="Additional ability score increases"
    )
    traits: List[RacialTrait] = Field(
        default_factory=list,
        description="Subrace-specific traits"
    )


class RaceSchema(BaseModel):
    """Complete race information"""
    name: str = Field(..., description="Race name")
    ability_score_increase: Dict[str, int] = Field(
        ...,
        description="Base ability score increases"
    )
    size: Literal["Small", "Medium"] = Field(..., description="Creature size")
    speed: int = Field(..., ge=0, description="Base walking speed in feet")
    languages: List[str] = Field(..., description="Known languages")
    traits: List[RacialTrait] = Field(default_factory=list, description="Racial traits")
    subraces: Dict[str, SubraceSchema] = Field(
        default_factory=dict,
        description="Available subraces"
    )
    
    @validator('speed')
    def validate_speed(cls, v):
        """Validate speed is reasonable"""
        if v < 0 or v > 120:
            raise ValueError(f"Speed must be between 0 and 120 feet, got {v}")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Dwarf",
                "ability_score_increase": {"Constitution": 2},
                "size": "Medium",
                "speed": 25,
                "languages": ["Common", "Dwarvish"],
                "traits": [
                    {
                        "name": "Darkvision",
                        "description": "See in dim light within 60 feet",
                        "mechanical_effect": "60 ft darkvision"
                    }
                ],
                "subraces": {
                    "Mountain Dwarf": {
                        "name": "Mountain Dwarf",
                        "ability_score_increase": {"Strength": 2},
                        "traits": []
                    }
                }
            }
        }


# ============================================================================
# CLASS SCHEMAS
# ============================================================================

class ClassFeature(BaseModel):
    """A class feature"""
    name: str = Field(..., description="Feature name")
    level: int = Field(..., ge=1, le=20, description="Level gained")
    description: str = Field(..., description="Feature description")


class ClassSchema(BaseModel):
    """Complete class information"""
    name: str = Field(..., description="Class name")
    hit_die: Literal[6, 8, 10, 12] = Field(..., description="Hit die size")
    primary_ability: List[str] = Field(..., description="Primary abilities")
    saving_throws: List[str] = Field(..., min_items=2, max_items=2, description="Proficient saving throws")
    armor_proficiencies: List[str] = Field(default_factory=list, description="Armor proficiencies")
    weapon_proficiencies: List[str] = Field(default_factory=list, description="Weapon proficiencies")
    tool_proficiencies: List[str] = Field(default_factory=list, description="Tool proficiencies")
    skills: Dict[str, int] = Field(
        default_factory=dict,
        description="Skill choices (skill category: number of choices)"
    )
    features: List[ClassFeature] = Field(default_factory=list, description="Class features")
    
    @validator('hit_die')
    def validate_hit_die(cls, v):
        """Validate hit die is standard D&D value"""
        if v not in [6, 8, 10, 12]:
            raise ValueError(f"Hit die must be 6, 8, 10, or 12, got {v}")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Fighter",
                "hit_die": 10,
                "primary_ability": ["Strength", "Dexterity"],
                "saving_throws": ["Strength", "Constitution"],
                "armor_proficiencies": ["Light", "Medium", "Heavy", "Shields"],
                "weapon_proficiencies": ["Simple", "Martial"],
                "skills": {"Any": 2},
                "features": [
                    {
                        "name": "Fighting Style",
                        "level": 1,
                        "description": "Choose a fighting style"
                    }
                ]
            }
        }


# ============================================================================
# CHARACTER SCHEMAS
# ============================================================================

class CharacterIdentity(BaseModel):
    """Basic character identity"""
    name: str = Field(..., min_length=1, description="Character name")
    race: str = Field(..., description="Character race")
    subrace: Optional[str] = Field(None, description="Character subrace")
    class_name: str = Field(..., alias="class", description="Character class")
    level: int = Field(1, ge=1, le=20, description="Character level")
    alignment: str = Field(..., description="Character alignment")
    background: Optional[str] = Field(None, description="Character background")


class CharacterStats(BaseModel):
    """Character statistics"""
    abilities: AbilityScores = Field(..., description="Ability scores")
    hp_max: int = Field(..., ge=1, description="Maximum hit points")
    hp_current: int = Field(..., ge=0, description="Current hit points")
    ac: int = Field(..., ge=10, description="Armor class")
    proficiency_bonus: int = Field(..., ge=2, description="Proficiency bonus")
    
    @validator('hp_current')
    def validate_hp_current(cls, v, values):
        """HP current cannot exceed max"""
        if 'hp_max' in values and v > values['hp_max']:
            raise ValueError(f"Current HP ({v}) cannot exceed max HP ({values['hp_max']})")
        return v


class CharacterPersonality(BaseModel):
    """Character personality traits"""
    personality_traits: List[str] = Field(default_factory=list, max_items=2)
    ideals: List[str] = Field(default_factory=list, max_items=1)
    bonds: List[str] = Field(default_factory=list, max_items=1)
    flaws: List[str] = Field(default_factory=list, max_items=1)


class CharacterCreate(BaseModel):
    """Schema for creating a new character"""
    identity: CharacterIdentity = Field(..., description="Character identity")
    abilities: AbilityScores = Field(..., description="Ability scores")
    personality: Optional[CharacterPersonality] = Field(None, description="Personality traits")
    
    class Config:
        schema_extra = {
            "example": {
                "identity": {
                    "name": "Bruenor Battlehammer",
                    "race": "Dwarf",
                    "subrace": "Mountain Dwarf",
                    "class": "Fighter",
                    "level": 1,
                    "alignment": "Lawful Good",
                    "background": "Soldier"
                },
                "abilities": {
                    "strength": 16,
                    "dexterity": 12,
                    "constitution": 17,
                    "intelligence": 10,
                    "wisdom": 13,
                    "charisma": 8
                },
                "personality": {
                    "personality_traits": ["I'm always polite and respectful"],
                    "ideals": ["Honor"],
                    "bonds": ["I would die to recover an ancient relic"],
                    "flaws": ["I have a weakness for pretty faces"]
                }
            }
        }


class CharacterComplete(BaseModel):
    """Complete character data"""
    id: str = Field(..., description="Unique character ID")
    identity: CharacterIdentity = Field(..., description="Character identity")
    stats: CharacterStats = Field(..., description="Character statistics")
    personality: CharacterPersonality = Field(..., description="Personality")
    features: List[str] = Field(default_factory=list, description="Character features")
    equipment: List[str] = Field(default_factory=list, description="Equipment")
    created_at: str = Field(..., description="Creation timestamp")
    updated_at: str = Field(..., description="Last update timestamp")


# ============================================================================
# KNOWLEDGE FRAGMENT SCHEMAS
# ============================================================================

class KnowledgeFragment(BaseModel):
    """A fragment of knowledge for RAG"""
    id: str = Field(..., description="Unique fragment ID")
    category: Literal["race", "class", "stat", "alignment", "rule"] = Field(
        ...,
        description="Fragment category"
    )
    content: str = Field(..., min_length=10, description="Fragment content")
    metadata: Dict = Field(default_factory=dict, description="Fragment metadata")
    embedding: Optional[List[float]] = Field(None, description="Vector embedding")
    
    class Config:
        schema_extra = {
            "example": {
                "id": "dwarf_culture_01",
                "category": "race",
                "content": "I am trapu and dense, all muscle and solid bone...",
                "metadata": {
                    "race": "Dwarf Mountain",
                    "section": "Physical Form",
                    "source": "Being_A_Dwarf_Mountain.md"
                }
            }
        }


# ============================================================================
# VALIDATOR FUNCTIONS
# ============================================================================

def validate_character_data(data: Dict) -> CharacterCreate:
    """
    Validate character creation data
    
    Args:
        data: Raw character data dictionary
        
    Returns:
        Validated CharacterCreate object
        
    Raises:
        ValidationError: If data is invalid
    """
    return CharacterCreate(**data)


def validate_race_data(data: Dict) -> RaceSchema:
    """
    Validate race data
    
    Args:
        data: Raw race data dictionary
        
    Returns:
        Validated RaceSchema object
        
    Raises:
        ValidationError: If data is invalid
    """
    return RaceSchema(**data)


def validate_class_data(data: Dict) -> ClassSchema:
    """
    Validate class data
    
    Args:
        data: Raw class data dictionary
        
    Returns:
        Validated ClassSchema object
        
    Raises:
        ValidationError: If data is invalid
    """
    return ClassSchema(**data)


if __name__ == "__main__":
    # Test validators
    print("="*60)
    print("TESTING DATA VALIDATORS")
    print("="*60)
    
    # Test ability scores
    print("\n✅ Testing AbilityScores:")
    abilities = AbilityScores(
        strength=16,
        dexterity=14,
        constitution=15,
        intelligence=10,
        wisdom=12,
        charisma=8
    )
    print(f"   STR modifier: {abilities.get_modifier('strength')}")
    print(f"   Valid: {abilities}")
    
    # Test character creation
    print("\n✅ Testing CharacterCreate:")
    char_data = {
        "identity": {
            "name": "Test Character",
            "race": "Human",
            "class": "Fighter",
            "level": 1,
            "alignment": "Neutral Good"
        },
        "abilities": {
            "strength": 16,
            "dexterity": 14,
            "constitution": 15,
            "intelligence": 10,
            "wisdom": 12,
            "charisma": 8
        }
    }
    
    try:
        char = validate_character_data(char_data)
        print(f"   Character: {char.identity.name}")
        print(f"   Valid: ✓")
    except Exception as e:
        print(f"   Error: {e}")
    
    print("\n✅ All validators ready!")
