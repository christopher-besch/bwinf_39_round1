from typing import List
from Find_winning_players import find_winning_player_KO,find_winning_player_Liga
from RNG_Simulation import play_RNG,play_RNG_5



def does_player_win(gamename : str,skill_levels:List[int]) -> bool:
    expected_best_player= max(skill_levels)
    if(gamename=="LIGA"):
        winning_player=find_winning_player_Liga(skill_levels,play_RNG)
    elif(gamename=="KO"):
        winning_player=find_winning_player_KO(0,len(skill_levels),skill_levels,expected_best_player,play_RNG)
    elif(gamename=="KO5"):
        winning_player=find_winning_player_KO(0,len(skill_levels),skill_levels,expected_best_player,play_RNG_5)

    return winning_player==expected_best_player














