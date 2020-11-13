from typing import List
import random
import itertools
import numpy as np
from rng_simulation import play_RNG


def find_winning_player_liga(skill_levels: List[int], play_game = play_RNG) -> int:
    """
    simulate the game mode "LIGA" and return the winner
    """

    # the number of players equals to the length of existing skill levels
    players = list(range(len(skill_levels)))
    # declare a list of integers that represents the ranks, every player starts with a score of zero
    ranking = [0] * len(skill_levels)
    # in the following for-loop, the list of players will shape to an two dimensional list
    # every element in players presents a pair of two
    for first_player, second_player in itertools.combinations(players, 2):
        # first_player and second_player play against each other
        # save the winner
        winning_player = play_game(first_player, second_player, skill_levels)
        # counts the wins of the winner
        ranking[winning_player] = ranking[winning_player] + 1
    # find the player with most wins and return his number
    best_player = max(ranking)
    return best_player


def find_winning_player_KO(start_player: int, end_player: int, skill_levels, expected_best_player, play_game) -> int:
    """
    recursive function
    simulate the game mode "KO" or "KO5" and return the winner
    start_player and end_player define an interval
    start_player is located in the interval and marks the first player on the left
    end_player isn't located in the interval and marks the limit on the right

    """

    if start_player == end_player - 1:
        # base case
        return start_player

    middle_player = int((start_player + end_player) / 2)

    # search the interval in which the expected best player takes place
    if middle_player <= expected_best_player < end_player:
        # interval on the right
        right_player = find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player, play_game)
        if right_player != expected_best_player:
            return -1
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player, play_game)
    elif start_player <= expected_best_player < middle_player:
        # interval on the left
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player, play_game)
        if left_player != expected_best_player:
            return -1
        right_player = find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player, play_game)
    else:
        # expected_best_player is not located in any interval
        left_player = find_winning_player_KO(start_player, middle_player, skill_levels, expected_best_player, play_game)
        right_player = find_winning_player_KO(middle_player, end_player, skill_levels, expected_best_player, play_game)
    return play_game(left_player, right_player, skill_levels)
