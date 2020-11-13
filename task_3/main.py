import random
from io_handler import read_skill_levels
from find_winning_players import find_winning_player_liga, find_winning_player_KO
from rng_simulation import play_RNG_5, play_RNG
from victory_test import does_player_win
import sys

def get_input():
    if len(sys.argv) < 2:
        # will return main method if arguments are missing
        print("Es werden noch Argumente benötigt :Dateipfad + Wiederholungen")
        return
    # first sys argument is needed for the filepath of the skill levels
    skill_levels = read_skill_levels(sys.argv[1])
    # second sys argument is needed for the number of repetitions
    n= int(sys.argv[2])
    players = list(range(len(skill_levels)))
    # declare counters for every win in game
    count_wins_liga = 0
    count_wins_KO = 0
    count_wins_KO5 = 0
    repetition =n
    while repetition > 0:
        repetition -= 1
        # mix the skill levels randomly
        random.shuffle(skill_levels)
        # If the best player wins, the specific counter will count
        if does_player_win("LIGA", skill_levels):
            count_wins_liga += 1
        if does_player_win("KO", skill_levels):
            count_wins_KO += 1
        if does_player_win("KO5", skill_levels):
            count_wins_KO5 += 1
    # the string best_game saves the game with most wins
    best_game = ""
    # compare the value of counters
    print("Wie oft hat der spielstärkste Spieler im Durschnitt gewonnen: ")
    print("LIGA :",count_wins_liga/n)
    print("KO   :",count_wins_KO/n)
    print("KO5  :",count_wins_KO5/n)
    if count_wins_liga > count_wins_KO and count_wins_liga > count_wins_KO5:
        best_game = "LIGA"
    elif count_wins_KO > count_wins_KO5 and count_wins_KO > count_wins_liga:
        best_game = "KO"
    else:
        best_game = "KO5"
    # print the best game mode
    print("Beste Spielvariante: " + best_game)


if __name__ == '__main__':
    main()
