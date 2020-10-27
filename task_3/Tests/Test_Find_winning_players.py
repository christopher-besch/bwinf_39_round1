from Find_winning_players import find_winning_player_Liga,find_winning_player_KO
import unittest


def test_best_player_wins(player1, player2, skill_levels):
    skill_level1=skill_levels[player1]
    skill_level2= skill_levels[player2]
    if(skill_level1>skill_level2):
        return player1
    return player2
def test_best_player_fails(player1,player2, skill_levels):
    skill_level1=skill_levels[player1]
    skill_level2=skill_levels[player2]
    if(skill_level1>skill_level2):
        return player2
    return player1

class Test_find_winning_player_Liga(unittest.TestCase):
    def test_find_winning_player(self):
        players = list(range(4))
        skill_levels=[1,2,3,4]
        winning_player=find_winning_player_Liga(players, skill_levels, test_best_player_wins)
        self.assertAlmostEqual(winning_player,3)

class Test_find_winning_player_KO(unittest.TestCase):
    def test_1(self):
        #Best_Player hat Glück!
        players= list(range(8))
        skill_levels=[1,3,8,7,4,5,2,6]
        #übergebe die Interavalle : startplayer 0-Endplayer 8
        winning_player = find_winning_player_KO(0, len(players), skill_levels, 2, test_best_player_wins)
        self.assertAlmostEqual(winning_player,2)

    def test_2(self):
        #Best_Player hat Unglück!
        players= list(range(8))
        skill_levels=[1,3,8,7,4,5,2,6]
        winning_player=find_winning_player_KO(0,len(players),skill_levels,2,test_best_player_fails)
        self.assertAlmostEqual(winning_player,-1)
    def test_3(self):
        #falscher Übergabe des expected_players
        players=list(range(8))
        skill_levels=[1,3,8,7,4,5,2,6]
        winning_player= find_winning_player_KO(0,len(players),skill_levels,3,test_best_player_wins)
        self.assertAlmostEqual(winning_player,-1)
    def test_4(self):
        #list index out of range
        players= list(range(8))
        skill_levels=[1,3,8,7,4,5,2]
        with self.assertRaises(IndexError):
            winning_player = find_winning_player_KO(0, len(players), skill_levels, 2, test_best_player_wins)

