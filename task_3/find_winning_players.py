from typing import List
import itertools
import random
from rng_simulation import play_rng


def get_maximums(items):
    """
    get a list of all maximums in items
    """
    maximum_indices = []
    # currently biggest item
    maximum = None
    for idx, item in enumerate(items):
        # maximum_indices has to be overwritten <- there are bigger items
        if maximum is None or item > maximum:
            maximum = item
            maximum_indices = [idx]
        # add index
        elif item == maximum:
            maximum_indices.append(idx)
    return maximum_indices


def find_winning_player_liga(skill_levels: List[int], play_game=play_rng) -> int:
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
        ranking[winning_player] += 1
    # find the players with most wins and return a random one
    best_player = get_maximums(ranking)
    return random.choice(best_player)


def find_winning_player_ko(start_player: int, end_player: int, skill_levels, expected_best_player, play_game) -> int:
    """
    recursive function
    simulate the game mode "KO" or "KO5" and return the winner
    start_player and end_player define an interval
    start_player is located in the interval and marks the first player on the left
    end_player isn't located in the interval and marks the limit on the right

    return -1 when the best player loses
    """

    if start_player == end_player - 1:
        # base case
        return start_player

    middle_player = (start_player + end_player) // 2

    # search the interval in which the expected best player takes place
    if middle_player <= expected_best_player < end_player:
        # interval on the right
        right_player = find_winning_player_ko(middle_player, end_player, skill_levels, expected_best_player, play_game)
        if right_player != expected_best_player:
            return -1
        left_player = find_winning_player_ko(start_player, middle_player, skill_levels, expected_best_player, play_game)
    elif start_player <= expected_best_player < middle_player:
        # interval on the left
        left_player = find_winning_player_ko(start_player, middle_player, skill_levels, expected_best_player, play_game)
        if left_player != expected_best_player:
            return -1
        right_player = find_winning_player_ko(middle_player, end_player, skill_levels, expected_best_player, play_game)
    else:
        # expected_best_player is not located in any interval
        left_player = find_winning_player_ko(start_player, middle_player, skill_levels, expected_best_player, play_game)
        right_player = find_winning_player_ko(middle_player, end_player, skill_levels, expected_best_player, play_game)
    return play_game(left_player, right_player, skill_levels)
