from typing import List


def read_skill_levels(filepath) -> List[int]:
    """
    read the skill levels and return a list of every skill level
    """
    with open(filepath, "r")as data:
        skill_levels = []
        for skill_level in data:
            # every line in our open data presents a skill level
            # add the current skill level to our list of skill levels
            skill_levels.append(int(skill_level))

    return skill_levels
