from typing import List
import random
import itertools
import numpy as np
from RNG_Simulation import play_RNG

def find_winning_player_Liga(players: List[int],skill_levels:List[int],play_game)->int:
    ranking= [0]*len(players)
    for first_player,secound_player in itertools.combinations(players,2):
        winning_player= play_game(first_player,secound_player,skill_levels)
        ranking[winning_player]=ranking[winning_player]+1
    best_player = max(ranking)
    return best_player


def find_winning_player_KO(start_player:int, end_player:int, skill_levels, expected_best_player,play_game)->int:
    #Play_game muss first_player, secound_player und skillevels als Argumente haben
    #Startplayer und Endplayer definieren ein Intervall
    #Startplayer ist das erste Element von links, Endplayer ist das Element ein weiter rechts als das letzte
    if(start_player==end_player-1):
        return start_player
    middle_player= int((start_player+end_player)/2)

    """in welchem Intervall ist der expected_best_Player"""
    if(expected_best_player>=middle_player and expected_best_player<end_player):
        #Rechte Intervall
        right_player = find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player,play_game)
        if(right_player!=expected_best_player):
            return -1
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player,play_game)
    elif(expected_best_player>=start_player and expected_best_player<middle_player):
        #Linkes Intervall
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player,play_game)
        if(left_player!=expected_best_player):
            return -1
        right_player= find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player,play_game)
    else:
        #Best_Player liegt in keinem Intervall
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player, play_game)
        right_player = find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player, play_game)
    return play_game(left_player,right_player,skill_levels)
