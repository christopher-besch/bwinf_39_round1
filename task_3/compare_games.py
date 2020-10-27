from typing import List
import random
import itertools
import numpy as np
from Find_winning_players import find_winning_player_KO,find_winning_player_Liga
from RNG_Simulation import play_RNG



def does_player_win(expected_best_player: int,gamename : str, players : List[int],skill_levels) -> bool:
    if(gamename=="LIGA"):
        winning_player=find_winning_player_Liga(players,skill_levels)
    elif(gamename=="KO"):
        winning_player=find_winning_player_KO(0,len(players),skill_levels,expected_best_player,play_RNG)

    return winning_player==expected_best_player

def get_average(wins:int,number_of_games:int)->int:
    average = wins/number_of_games
    return average













