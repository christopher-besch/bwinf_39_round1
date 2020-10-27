import random
from typing import List
def play_RNG(player1: int,player2: int,skill_levels: List[int])-> int:
    skill_level1=skill_levels[player1]
    skill_level2=skill_levels[player2]
    random_murmur=random.randint(0,skill_level1+skill_level2)
    if(random_murmur<skill_level1):
        return player1
    else:
        return player2