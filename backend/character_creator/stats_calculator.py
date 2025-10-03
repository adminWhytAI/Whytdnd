"""
Stats Calculator - D&D 5e ability score generation and management
Implements standard array, point buy, and dice rolling methods
"""
import random
from typing import List, Dict, Tuple, Literal
from dataclasses import dataclass

from backend.utils.logger import logger


@dataclass
class AbilityRoll:
    """Result of a single ability score roll"""
    rolls: List[int]
    dropped: int
    total: int


class DiceRoller:
    """
    Handles dice rolling for ability scores and other mechanics
    """
    
    @staticmethod
    def roll_die(sides: int) -> int:
        """
        Roll a single die
        
        Args:
            sides: Number of sides on the die
            
        Returns:
            Result of the roll
        """
        return random.randint(1, sides)
    
    @staticmethod
    def roll_multiple(num_dice: int, sides: int) -> List[int]:
        """
        Roll multiple dice
        
        Args:
            num_dice: Number of dice to roll
            sides: Number of sides on each die
            
        Returns:
            List of roll results
        """
        return [DiceRoller.roll_die(sides) for _ in range(num_dice)]
    
    @staticmethod
    def roll_4d6_drop_lowest() -> AbilityRoll:
        """
        Roll 4d6 and drop the lowest - standard D&D method
        
        Returns:
            AbilityRoll with details
        """
        rolls = DiceRoller.roll_multiple(4, 6)
        rolls_sorted = sorted(rolls)
        dropped = rolls_sorted[0]
        kept = rolls_sorted[1:]
        total = sum(kept)
        
        return AbilityRoll(
            rolls=rolls,
            dropped=dropped,
            total=total
        )
    
    @staticmethod
    def roll_ability_scores(method: Literal["4d6", "3d6"] = "4d6") -> List[int]:
        """
        Roll a full set of 6 ability scores
        
        Args:
            method: Rolling method (4d6 drop lowest or straight 3d6)
            
        Returns:
            List of 6 ability scores
        """
        scores = []
        
        if method == "4d6":
            for _ in range(6):
                roll = DiceRoller.roll_4d6_drop_lowest()
                scores.append(roll.total)
                logger.debug(f"Rolled {roll.rolls}, dropped {roll.dropped}, total: {roll.total}")
        else:  # 3d6
            for _ in range(6):
                rolls = DiceRoller.roll_multiple(3, 6)
                scores.append(sum(rolls))
        
        return scores


class StatsManager:
    """
    Manages ability score generation and assignment
    """
    
    # Standard array as per D&D 5e
    STANDARD_ARRAY = [15, 14, 13, 12, 10, 8]
    
    # Point buy costs (PHB p.13)
    POINT_BUY_COSTS = {
        8: 0,
        9: 1,
        10: 2,
        11: 3,
        12: 4,
        13: 5,
        14: 7,
        15: 9
    }
    
    POINT_BUY_TOTAL = 27
    
    @staticmethod
    def calculate_modifier(score: int) -> int:
        """
        Calculate ability score modifier
        
        Args:
            score: Ability score value
            
        Returns:
            Modifier value
        """
        return (score - 10) // 2
    
    @staticmethod
    def get_standard_array() -> List[int]:
        """
        Get the standard array
        
        Returns:
            Standard array [15, 14, 13, 12, 10, 8]
        """
        return StatsManager.STANDARD_ARRAY.copy()
    
    @staticmethod
    def validate_point_buy_score(score: int) -> bool:
        """
        Check if a score is valid for point buy
        
        Args:
            score: Score to validate
            
        Returns:
            True if valid
        """
        return score in StatsManager.POINT_BUY_COSTS
    
    @staticmethod
    def calculate_point_buy_cost(scores: List[int]) -> int:
        """
        Calculate total point cost of scores
        
        Args:
            scores: List of ability scores
            
        Returns:
            Total point cost
        """
        total = 0
        for score in scores:
            if score not in StatsManager.POINT_BUY_COSTS:
                raise ValueError(f"Invalid point buy score: {score}")
            total += StatsManager.POINT_BUY_COSTS[score]
        return total
    
    @staticmethod
    def validate_point_buy(scores: List[int]) -> Tuple[bool, str]:
        """
        Validate point buy array
        
        Args:
            scores: List of 6 ability scores
            
        Returns:
            (is_valid, error_message)
        """
        if len(scores) != 6:
            return False, f"Must have exactly 6 scores, got {len(scores)}"
        
        # Check all scores are valid
        for score in scores:
            if not StatsManager.validate_point_buy_score(score):
                return False, f"Invalid score for point buy: {score}"
        
        # Check total cost
        total_cost = StatsManager.calculate_point_buy_cost(scores)
        if total_cost > StatsManager.POINT_BUY_TOTAL:
            return False, f"Point buy cost {total_cost} exceeds maximum {StatsManager.POINT_BUY_TOTAL}"
        
        if total_cost < StatsManager.POINT_BUY_TOTAL:
            return False, f"Point buy cost {total_cost} is less than {StatsManager.POINT_BUY_TOTAL}"
        
        return True, "Valid"
    
    @staticmethod
    def apply_racial_bonuses(
        base_scores: Dict[str, int],
        racial_bonuses: Dict[str, int]
    ) -> Dict[str, int]:
        """
        Apply racial ability score bonuses
        
        Args:
            base_scores: Base ability scores
            racial_bonuses: Racial bonuses to apply
            
        Returns:
            Scores with racial bonuses applied
        """
        result = base_scores.copy()
        
        for ability, bonus in racial_bonuses.items():
            if ability in result:
                result[ability] += bonus
                logger.debug(f"Applied +{bonus} {ability} from race")
        
        return result
    
    @staticmethod
    def assign_scores_to_abilities(
        scores: List[int],
        assignments: Dict[str, int]
    ) -> Dict[str, int]:
        """
        Assign rolled/chosen scores to specific abilities
        
        Args:
            scores: List of scores to assign
            assignments: Dict mapping ability names to indices in scores list
            
        Returns:
            Dict mapping ability names to scores
        """
        abilities = {
            'Strength': 0,
            'Dexterity': 0,
            'Constitution': 0,
            'Intelligence': 0,
            'Wisdom': 0,
            'Charisma': 0
        }
        
        for ability, index in assignments.items():
            if ability in abilities and 0 <= index < len(scores):
                abilities[ability] = scores[index]
        
        return abilities
    
    @staticmethod
    def generate_random_scores(method: Literal["4d6", "3d6", "standard"] = "4d6") -> List[int]:
        """
        Generate ability scores using specified method
        
        Args:
            method: Generation method
            
        Returns:
            List of 6 ability scores
        """
        if method == "standard":
            return StatsManager.get_standard_array()
        else:
            return DiceRoller.roll_ability_scores(method)


def generate_ability_scores_interactive() -> Dict[str, int]:
    """
    Interactive ability score generation (for CLI testing)
    
    Returns:
        Dict of ability scores
    """
    print("\n" + "="*60)
    print("ABILITY SCORE GENERATION")
    print("="*60)
    
    print("\nChoose generation method:")
    print("1. Standard Array [15, 14, 13, 12, 10, 8]")
    print("2. Roll 4d6 (drop lowest)")
    print("3. Point Buy (27 points)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    scores = []
    
    if choice == "1":
        scores = StatsManager.get_standard_array()
        print(f"\nStandard Array: {scores}")
        
    elif choice == "2":
        print("\nRolling 4d6 (drop lowest) 6 times...")
        roller = DiceRoller()
        for i in range(6):
            roll = roller.roll_4d6_drop_lowest()
            scores.append(roll.total)
            print(f"  Roll {i+1}: {roll.rolls} (dropped {roll.dropped}) = {roll.total}")
        
        print(f"\nYour rolls: {scores}")
        
    else:  # Point buy
        print("\nPoint Buy - 27 points total")
        print("Costs: 8(0), 9(1), 10(2), 11(3), 12(4), 13(5), 14(7), 15(9)")
        # For simplicity, use standard array
        scores = StatsManager.get_standard_array()
        print("(Using standard array for demo)")
    
    # Assign to abilities
    abilities = ['Strength', 'Dexterity', 'Constitution', 'Intelligence', 'Wisdom', 'Charisma']
    
    print("\nAssign scores to abilities:")
    assignments = {}
    for i, ability in enumerate(abilities):
        print(f"\n{ability}:")
        for j, score in enumerate(scores):
            print(f"  {j}: {score}")
        
        idx = int(input(f"Choose score for {ability} (0-{len(scores)-1}): "))
        assignments[ability] = scores[idx]
        scores.pop(idx)
    
    return assignments


if __name__ == "__main__":
    # Test the stats calculator
    print("="*60)
    print("TESTING STATS CALCULATOR")
    print("="*60)
    
    # Test modifier calculation
    print("\n✅ Testing Modifiers:")
    test_scores = [8, 10, 12, 14, 16, 18, 20]
    for score in test_scores:
        mod = StatsManager.calculate_modifier(score)
        sign = '+' if mod >= 0 else ''
        print(f"   Score {score:2d} → Modifier {sign}{mod}")
    
    # Test standard array
    print("\n✅ Standard Array:")
    std_array = StatsManager.get_standard_array()
    print(f"   {std_array}")
    
    # Test dice rolling
    print("\n✅ Testing 4d6 drop lowest (5 rolls):")
    roller = DiceRoller()
    for i in range(5):
        roll = roller.roll_4d6_drop_lowest()
        print(f"   Roll {i+1}: {roll.rolls} (dropped {roll.dropped}) = {roll.total}")
    
    # Test point buy validation
    print("\n✅ Testing Point Buy Validation:")
    valid_buy = [15, 14, 13, 12, 10, 8]  # Exactly 27 points
    is_valid, msg = StatsManager.validate_point_buy(valid_buy)
    print(f"   {valid_buy}: {is_valid} - {msg}")
    
    # Test racial bonus application
    print("\n✅ Testing Racial Bonuses:")
    base = {
        'Strength': 15,
        'Dexterity': 14,
        'Constitution': 13,
        'Intelligence': 12,
        'Wisdom': 10,
        'Charisma': 8
    }
    racial = {'Constitution': 2, 'Strength': 2}  # Mountain Dwarf
    
    result = StatsManager.apply_racial_bonuses(base, racial)
    print(f"   Base: STR {base['Strength']}, CON {base['Constitution']}")
    print(f"   Racial: +2 CON, +2 STR (Mountain Dwarf)")
    print(f"   Final: STR {result['Strength']}, CON {result['Constitution']}")
    
    print("\n✅ All tests complete!")
