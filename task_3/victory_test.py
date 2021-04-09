from typing import List
from find_winning_players import find_winning_player_ko, find_winning_player_liga
from rng_simulation import play_rng, play_rng_5


def does_player_win(game_name: str, skill_levels: List[int]) -> bool:
    """
    find out if the expected best player wins and return a boolean
    """
    # determine the player with the best skill level
    expected_best_player = skill_levels.index(max(skill_levels))
    # determine the winner of the given play mode
    if game_name == "LIGA":
        winning_player = find_winning_player_liga(skill_levels)
    elif game_name == "KO":
        winning_player = find_winning_player_ko(0, len(skill_levels), skill_levels, expected_best_player, play_rng)
    elif game_name == "KO5":
        winning_player = find_winning_player_ko(0, len(skill_levels), skill_levels, expected_best_player, play_rng_5)
    else:
        raise ValueError("unsupported game_name used.")
    # compare the winner with expected best player
    return winning_player == expected_best_player
