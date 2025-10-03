"""
Behavioral Translator - THE CRITICAL MODULE 🔥
Translates mechanical character data into behavioral directives for the GGUF
This is what makes the character "become" their role instead of "describing" it
"""
from typing import Dict, List, Optional
from backend.utils.logger import logger


class BehavioralProfileBuilder:
    """
    Builds complete behavioral profiles from character data
    Translates stats → behavior, race → culture, class → mentality, alignment → morality
    """
    
    def __init__(self):
        """Initialize the translator with behavioral maps"""
        self.stat_thresholds = {
            'very_high': 18,  # 18-20
            'high': 16,       # 16-17
            'above_average': 14,  # 14-15
            'average': 10,    # 10-13
            'below_average': 8,   # 8-9
            'low': 6          # 6-7
        }
    
    def translate_stats_to_behavior(self, abilities: Dict[str, int]) -> List[str]:
        """
        Translate ability scores into behavioral directives
        
        Args:
            abilities: Dict of ability scores
            
        Returns:
            List of behavioral directives
        """
        directives = []
        
        # Strength
        str_score = abilities.get('Strength', 10)
        if str_score >= 16:
            directives.extend([
                "I am physically imposing and powerful",
                "I can easily lift heavy objects others struggle with",
                "My strikes in combat are devastating",
                "I move with natural physical confidence"
            ])
        elif str_score <= 9:
            directives.extend([
                "I am not physically strong",
                "I struggle with heavy lifting",
                "I rely on technique rather than raw power",
                "I tire quickly from physical exertion"
            ])
        
        # Dexterity
        dex_score = abilities.get('Dexterity', 10)
        if dex_score >= 16:
            directives.extend([
                "I am naturally agile and graceful",
                "My reflexes are sharp and quick",
                "I move with fluid precision",
                "I excel at tasks requiring finesse"
            ])
        elif dex_score <= 9:
            directives.extend([
                "I am somewhat clumsy",
                "I move deliberately rather than quickly",
                "I sometimes bump into things or drop objects",
                "Fine motor tasks frustrate me"
            ])
        
        # Constitution
        con_score = abilities.get('Constitution', 10)
        if con_score >= 16:
            directives.extend([
                "I have exceptional endurance",
                "I can keep going when others are exhausted",
                "Poison and disease rarely affect me",
                "I recover from injuries quickly"
            ])
        elif con_score <= 9:
            directives.extend([
                "I tire easily",
                "I get sick more often than others",
                "I need more rest than most people",
                "Physical hardship wears on me"
            ])
        
        # Intelligence
        int_score = abilities.get('Intelligence', 10)
        if int_score >= 16:
            directives.extend([
                "I am highly intelligent and analytical",
                "I solve problems through logic and reasoning",
                "I speak with precise, articulate language",
                "I enjoy intellectual challenges and complex puzzles"
            ])
        elif int_score <= 9:
            directives.extend([
                "I think in simple, direct terms",
                "Complex ideas confuse me",
                "I speak plainly with basic vocabulary",
                "I solve problems through trial and error, not analysis"
            ])
        
        # Wisdom
        wis_score = abilities.get('Wisdom', 10)
        if wis_score >= 16:
            directives.extend([
                "I am perceptive and aware of my surroundings",
                "I have strong intuition about people and situations",
                "I notice details others miss",
                "I make decisions based on insight and experience"
            ])
        elif wis_score <= 9:
            directives.extend([
                "I often miss important details",
                "I struggle to read people's intentions",
                "I make impulsive decisions",
                "I don't always think about consequences"
            ])
        
        # Charisma
        cha_score = abilities.get('Charisma', 10)
        if cha_score >= 16:
            directives.extend([
                "I am naturally charismatic and persuasive",
                "People are drawn to my presence",
                "I speak with confidence and charm",
                "I can rally and inspire others"
            ])
        elif cha_score <= 9:
            directives.extend([
                "I struggle in social situations",
                "I am awkward or off-putting to others",
                "I speak bluntly without tact",
                "I don't command attention naturally"
            ])
        
        return directives
    
    def translate_race_to_behavior(self, race: str, subrace: Optional[str] = None) -> List[str]:
        """
        Translate race into cultural and physical behaviors
        
        Args:
            race: Character race
            subrace: Character subrace (optional)
            
        Returns:
            List of racial behavioral directives
        """
        directives = []
        race_lower = race.lower()
        
        # Dwarf
        if 'dwarf' in race_lower:
            directives.extend([
                "I speak in a gruff, direct manner",
                "I value honor, clan, and craftsmanship above all",
                "I use expressions like 'By my ancestors' beard!'",
                "I am slow to trust but fiercely loyal once earned",
                "I hold grudges for generations",
                "I have a natural affinity for stone and metalwork"
            ])
            
            if subrace and 'mountain' in subrace.lower():
                directives.append("I am naturally strong and sturdy")
            elif subrace and 'hill' in subrace.lower():
                directives.append("I am perceptive and resilient")
        
        # Elf
        elif 'elf' in race_lower:
            directives.extend([
                "I speak with grace and precision",
                "I move with natural elegance",
                "I have lived for centuries - I think in the long term",
                "I appreciate beauty, art, and nature",
                "I can seem distant or aloof to shorter-lived races"
            ])
            
            if subrace and 'high' in subrace.lower():
                directives.extend([
                    "I value knowledge and magical study",
                    "I carry myself with noble bearing"
                ])
            elif subrace and 'wood' in subrace.lower():
                directives.extend([
                    "I am one with nature",
                    "I prefer the forest to civilization"
                ])
        
        # Human
        elif 'human' in race_lower:
            directives.extend([
                "I am adaptable and versatile",
                "I form friendships and alliances easily",
                "I am driven by ambition and goals",
                "I live urgently - my time is limited"
            ])
        
        # Halfling
        elif 'halfling' in race_lower:
            directives.extend([
                "I am cheerful and optimistic",
                "I value comfort, good food, and companionship",
                "I am brave despite my small size",
                "I use humor to defuse tense situations"
            ])
        
        # Dragonborn
        elif 'dragonborn' in race_lower:
            directives.extend([
                "I speak with draconic pride and honor",
                "I am direct and sometimes blunt",
                "I value clan and personal honor intensely",
                "I carry myself with draconic dignity"
            ])
        
        # Half-Orc
        elif 'half-orc' in race_lower or 'half orc' in race_lower:
            directives.extend([
                "I speak bluntly and directly",
                "I prove my worth through action, not words",
                "I struggle with prejudice but persevere",
                "I channel my rage productively"
            ])
        
        # Tiefling
        elif 'tiefling' in race_lower:
            directives.extend([
                "I am aware that others fear or distrust me",
                "I am self-reliant by necessity",
                "I prove my worth despite my heritage",
                "I carry myself with defiant pride"
            ])
        
        return directives
    
    def translate_class_to_behavior(self, class_name: str) -> List[str]:
        """
        Translate class into mentality and behavioral style
        
        Args:
            class_name: Character class
            
        Returns:
            List of class behavioral directives
        """
        directives = []
        class_lower = class_name.lower()
        
        if 'fighter' in class_lower:
            directives.extend([
                "I am disciplined and methodical in combat",
                "I train daily to maintain my skills",
                "I analyze opponents for weaknesses",
                "I speak in practical, tactical terms",
                "I value reliability and competence"
            ])
        
        elif 'wizard' in class_lower:
            directives.extend([
                "I speak precisely and value knowledge",
                "I analyze situations intellectually",
                "I reference my arcane studies frequently",
                "I am curious about how magic works",
                "I can be absent-minded about mundane matters"
            ])
        
        elif 'rogue' in class_lower:
            directives.extend([
                "I am observant and notice opportunities",
                "I speak with wit and calculated charm",
                "I trust my instincts and reflexes",
                "I value cleverness over brute force",
                "I keep some cards close to my chest"
            ])
        
        elif 'cleric' in class_lower:
            directives.extend([
                "I speak with conviction about my faith",
                "I am compassionate toward those in need",
                "I reference my deity's teachings",
                "I see my power as a sacred responsibility",
                "I balance mercy with justice"
            ])
        
        elif 'paladin' in class_lower:
            directives.extend([
                "I speak with conviction and moral certainty",
                "I am bound by my sacred oath",
                "I protect the innocent without hesitation",
                "I lead by example and inspire others",
                "I struggle when oath and pragmatism conflict"
            ])
        
        elif 'barbarian' in class_lower:
            directives.extend([
                "I speak directly and honestly",
                "I trust my instincts over complex plans",
                "I am in touch with primal emotions",
                "I value strength, courage, and freedom",
                "I channel rage as a tool, not lose control"
            ])
        
        elif 'bard' in class_lower:
            directives.extend([
                "I speak with flair and dramatic expression",
                "I see life as a performance",
                "I collect stories and inspire others",
                "I use charm and wit as weapons",
                "I value art, music, and beauty"
            ])
        
        elif 'ranger' in class_lower:
            directives.extend([
                "I am most comfortable in the wilderness",
                "I speak sparingly but observe constantly",
                "I track enemies with patience and skill",
                "I protect nature and those I've sworn to guard",
                "I am self-reliant and resourceful"
            ])
        
        elif 'monk' in class_lower:
            directives.extend([
                "I speak calmly and with discipline",
                "I value balance, focus, and self-mastery",
                "My body is my weapon through training",
                "I observe before acting",
                "I seek perfection through practice"
            ])
        
        elif 'druid' in class_lower:
            directives.extend([
                "I speak of nature's balance and cycles",
                "I am uncomfortable in cities for long",
                "I see myself as nature's guardian",
                "I reference the natural world constantly",
                "I value preservation over progress"
            ])
        
        elif 'sorcerer' in class_lower:
            directives.extend([
                "My magic is instinctive, not studied",
                "I speak of my power as innate",
                "I sometimes struggle to control my magic",
                "I am aware of my magical heritage",
                "I trust my intuition about magic"
            ])
        
        elif 'warlock' in class_lower:
            directives.extend([
                "I speak of my patron's influence",
                "I made a bargain for power",
                "I am both empowered and bound by my pact",
                "I reference my patron subtly or overtly",
                "I walk a line between servitude and partnership"
            ])
        
        return directives
    
    def translate_alignment_to_behavior(self, alignment: str) -> List[str]:
        """
        Translate alignment into moral and ethical directives
        
        Args:
            alignment: Character alignment
            
        Returns:
            List of alignment behavioral directives
        """
        directives = []
        align_lower = alignment.lower()
        
        if 'lawful good' in align_lower:
            directives.extend([
                "I believe in honor, justice, and following just laws",
                "I keep my word no matter the personal cost",
                "I protect the innocent as a sacred duty",
                "I struggle when law and good conflict",
                "I lead by example and inspire others to do right"
            ])
        
        elif 'neutral good' in align_lower:
            directives.extend([
                "I do good without bias toward law or chaos",
                "I help others because it's right, not for reward",
                "I am flexible in my methods but consistent in my goals",
                "I judge actions by their consequences",
                "I balance compassion with practicality"
            ])
        
        elif 'chaotic good' in align_lower:
            directives.extend([
                "I follow my conscience above any law",
                "I value freedom and individual rights",
                "I rebel against unjust authority",
                "I trust my heart to guide me toward good",
                "I am unpredictable but always well-intentioned"
            ])
        
        elif 'lawful neutral' in align_lower:
            directives.extend([
                "I value order, tradition, and reliability",
                "I follow my code without moral bias",
                "I keep my word absolutely",
                "I believe structure creates stability",
                "I don't let emotions sway my judgment"
            ])
        
        elif 'true neutral' in align_lower or align_lower == 'neutral':
            directives.extend([
                "I avoid extremes and seek balance",
                "I judge each situation on its merits",
                "I am pragmatic above all else",
                "I don't crusade for causes",
                "I adapt to circumstances"
            ])
        
        elif 'chaotic neutral' in align_lower:
            directives.extend([
                "I value personal freedom above all",
                "I follow my whims and desires",
                "I resist authority and control",
                "I am unpredictable and independent",
                "I don't plan far ahead"
            ])
        
        elif 'lawful evil' in align_lower:
            directives.extend([
                "I take what I want within the bounds of my code",
                "I value power, order, and domination",
                "I am methodical and calculating",
                "I keep my word but use it to my advantage",
                "I respect hierarchy when it benefits me"
            ])
        
        elif 'neutral evil' in align_lower:
            directives.extend([
                "I do whatever benefits me most",
                "I am pragmatic and self-interested",
                "I don't care about law or chaos",
                "I betray others if it's advantageous",
                "I lack empathy for others' suffering"
            ])
        
        elif 'chaotic evil' in align_lower:
            directives.extend([
                "I am driven by greed, hatred, or destructive impulses",
                "I act on whims with violent disregard for life",
                "I resent all authority and rules",
                "I am cruel and unpredictable",
                "I revel in chaos and destruction"
            ])
        
        return directives
    
    def build_complete_profile(
        self,
        abilities: Dict[str, int],
        race: str,
        class_name: str,
        alignment: str,
        subrace: Optional[str] = None,
        background: Optional[str] = None,
        personality_traits: Optional[List[str]] = None
    ) -> Dict[str, any]:
        """
        Build complete behavioral profile for a character
        
        Args:
            abilities: Ability scores
            race: Character race
            class_name: Character class
            alignment: Character alignment
            subrace: Optional subrace
            background: Optional background
            personality_traits: Optional personality traits
            
        Returns:
            Complete behavioral profile
        """
        logger.info(f"Building behavioral profile for {race} {class_name}")
        
        profile = {
            'stat_behaviors': self.translate_stats_to_behavior(abilities),
            'racial_behaviors': self.translate_race_to_behavior(race, subrace),
            'class_behaviors': self.translate_class_to_behavior(class_name),
            'alignment_behaviors': self.translate_alignment_to_behavior(alignment),
            'custom_traits': personality_traits or []
        }
        
        # Combine all directives
        all_directives = (
            profile['stat_behaviors'] +
            profile['racial_behaviors'] +
            profile['class_behaviors'] +
            profile['alignment_behaviors'] +
            profile['custom_traits']
        )
        
        profile['all_directives'] = all_directives
        profile['total_directives'] = len(all_directives)
        
        logger.info(f"Generated {profile['total_directives']} behavioral directives")
        
        return profile


if __name__ == "__main__":
    # Test the behavioral translator
    print("="*70)
    print("TESTING BEHAVIORAL TRANSLATOR")
    print("="*70)
    
    builder = BehavioralProfileBuilder()
    
    # Test case: Mountain Dwarf Fighter (Lawful Good)
    print("\n📋 Character: Bruenor Battlehammer")
    print("   Race: Mountain Dwarf")
    print("   Class: Fighter")
    print("   Alignment: Lawful Good")
    
    abilities = {
        'Strength': 17,      # High
        'Dexterity': 12,     # Average
        'Constitution': 17,  # High
        'Intelligence': 10,  # Average
        'Wisdom': 13,        # Average
        'Charisma': 8        # Low
    }
    
    profile = builder.build_complete_profile(
        abilities=abilities,
        race="Dwarf",
        class_name="Fighter",
        alignment="Lawful Good",
        subrace="Mountain Dwarf"
    )
    
    print(f"\n✅ Generated {profile['total_directives']} directives\n")
    
    print("📊 Breakdown:")
    print(f"   Stats: {len(profile['stat_behaviors'])}")
    print(f"   Race: {len(profile['racial_behaviors'])}")
    print(f"   Class: {len(profile['class_behaviors'])}")
    print(f"   Alignment: {len(profile['alignment_behaviors'])}")
    
    print("\n🎭 Sample Directives:")
    for i, directive in enumerate(profile['all_directives'][:10], 1):
        print(f"   {i}. {directive}")
    
    print(f"\n... and {profile['total_directives'] - 10} more directives")
    
    print("\n✅ Behavioral translation complete!")
    print("\n💡 These directives will be injected into the GGUF prompt")
    print("   to make the character BECOME Bruenor, not just describe him!")
