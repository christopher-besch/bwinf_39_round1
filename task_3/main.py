import random
from IO_Handler import read_skill_levels
from Find_winning_players import find_winning_player_Liga,find_winning_player_KO
from RNG_Simulation import play_RNG_5,play_RNG
from test_of_victory import does_player_win
import sys

def main():
    if(len(sys.argv)<2):
        print("Es werden noch Argumente benötigt :Dateipfad + Wiederholungen")
        return
    skill_levels = read_skill_levels(sys.argv[1])
    players = list(range(len(skill_levels)))
    expected_best_player=max(players)
    count_wins_liga = 0
    count_wins_KO = 0
    count_wins_KO5 = 0
    repetition = int(sys.argv[2])

    while (repetition > 0):
        repetition -= 1
        #Vermische die Spielstärken zufällig
        random.shuffle(skill_levels)

        if (does_player_win( "LIGA", skill_levels)):
            count_wins_liga += 1
        if (does_player_win("KO", skill_levels)):
            count_wins_KO += 1
        if (does_player_win("KO5", skill_levels)):
            count_wins_KO5 += 1

    best_game=""
    if(count_wins_liga>count_wins_KO and count_wins_liga>count_wins_KO5):
        best_game="LIGA"
    elif(count_wins_KO>count_wins_KO5 and count_wins_KO>count_wins_liga):
        best_game="KO"
    else:
        best_game="KO5"
    print(best_game)
if __name__ == '__main__':
    main()

