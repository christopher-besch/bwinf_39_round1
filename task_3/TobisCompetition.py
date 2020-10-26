from typing import List
import random
import itertools
"""
skill_levels=read_skill_levels(File)
players= range(0,len(skill_levels))
best_player = max(players)
simulation_count = 50
Liga_wins=0
KO_wins=0
KO5_wins=0

for simulationer_counter in range(0,simulation_count)
    bester_spieler_Liga=playLiga()
    best_player_KO=playKO(,1)
    best_player_KO=playKO5(,5)
comparegames()
"""

def read_skill_levels(Filepath)-> list[int]:
    with open(Filepath,"r")as data :
        skill_levels=[]
        for skill_level in data:
                skill_levels.append(int(skill_level))

    return skill_levels

def play_RNG(player1: int,player2: int,skill_levels: list[int])-> int:
    skill_level1=skill_levels.get(player1)
    skill_level2=skill_levels.get(player2)
    murmurs = [skill_level1+skill_level2]
    for murmur in murmurs:
        murmurs.append(random.randint(1,2))
    winning_murmur = murmurs.get(random.randint(0,len(murmurs)))
    if(winning_murmur==1):
        return player1
    else:
        return player2



def does_player_win(playeridx: int,gamename : str, players : List[int]) -> bool:





def play_Liga(players: list(int),skill_levels:list(int))->int:
    ranking= [len(players)]
    for first_player,secound_player in itertools.combinations(players,2):
        winning_player= play_RNG(first_player,secound_player,skill_levels)
        ranking[winning_player]=ranking.get(winning_player)+1
    best_player = max(ranking)
    return best_player





def play_KO(players:list(int),rounds:int)->int:
    """Rekusiv?"""

    return best_player
