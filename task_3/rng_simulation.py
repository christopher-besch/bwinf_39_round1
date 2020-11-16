import random
from typing import List


def play_RNG(player1: int, player2: int, skill_levels: List[int]) -> int:
    """
    player1 and player2 play RNG against each other
    the skill level of a player determines the number of murmurs in the urn
    return the winner

    """
    skill_level1 = skill_levels[player1]
    skill_level2 = skill_levels[player2]
    # determine a random murmur
    random_murmur = random.randint(1, skill_level1 + skill_level2)
    # the owner of the drawn murmur wins
    if random_murmur <= skill_level1:
        return player1
    else:
        return player2


def play_RNG_5(player1: int, player2: int, skill_levels: List[int]) -> int:
    """
    play RNG with 5 repetitions
    """
    count_wins_player1 = 0
    count_wins_player2 = 0
    skill_level1 = skill_levels[player1]
    skill_level2 = skill_levels[player2]
    counter = 5
    while counter > 0:
        # counter counts down
        counter -= 1
        random_murmur = random.randint(1, skill_level1 + skill_level2)
        if random_murmur <= skill_level1:
            count_wins_player1 += 1
        else:
            count_wins_player2 += 1
    if count_wins_player2 < count_wins_player1:
        return player1
    else:
        return player2
