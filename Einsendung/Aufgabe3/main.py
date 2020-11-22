import random
from io_handler import read_skill_levels
from victory_test import does_player_win
import sys


def main():
    if len(sys.argv) < 3:
        # will return if arguments are missing
        print("Es werden noch Argumente benötigt :Dateipfad + Wiederholungen")
        return
    # second sys argument is needed for the filepath of the skill levels
    skill_levels = read_skill_levels(sys.argv[1])
    # third sys argument is needed for the number of repetitions
    n = int(sys.argv[2])
    # declare counters for every win in game
    count_wins_liga = 0
    count_wins_ko = 0
    count_wins_ko5 = 0
    for _ in range(n):
        # mix the skill levels randomly
        random.shuffle(skill_levels)
        # If the best player wins, the specific counter will be increased
        if does_player_win("LIGA", skill_levels):
            count_wins_liga += 1
        if does_player_win("KO", skill_levels):
            count_wins_ko += 1
        if does_player_win("KO5", skill_levels):
            count_wins_ko5 += 1

    # compare the values of counters
    print("Wie oft hat der spielstärkste Spieler im Durschnitt gewonnen: ")
    print(f"LIGA:\t{count_wins_liga / n}")
    print(f"KO:\t{count_wins_ko / n}")
    print(f"KO5:\t{count_wins_ko5 / n}")
    games = {
        count_wins_liga: "LIGA",
        count_wins_ko: "KO",
        count_wins_ko5: "K05"
    }
    # print the best game mode
    print(f"Beste Spielvariante: {games[max(games)]}")


if __name__ == '__main__':
    main()
