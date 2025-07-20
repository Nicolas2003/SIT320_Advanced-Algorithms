import pytest
import tic_tac_toe
import math

from tic_tac_toe import print_board


# board = {"human": [False, False, False, False, False, False, False, False, False],
#          "bot": [False, False, False, False, False, False, False, False]}
def test_empty():
    assert tic_tac_toe.is_winner([False, False, False, False, False, False, False, False, False]) == False

def test_first_row():
    assert tic_tac_toe.is_winner([True, False, False, True, False, False, True, False, False]) == True
    assert tic_tac_toe.is_winner([True, True, False, True, False, False, True, False, False]) == True

def test_verify_empty_spaces():
    hum = [False, True,  False, True,  False, False, True, False, False]
    bot = [True,  False, False, False, False, False, True, False, False]
    assert tic_tac_toe.empty_spaces(hum, bot) == [2, 4, 5, 7, 8]

def test_full_board():
    bot = [True,  False, True,  True,  False, True,  False, True,  False]
    hum = [False, True,  False, False, True,  False, True,  False, True]
    assert tic_tac_toe.empty_spaces(hum, bot) == []
    assert tic_tac_toe.occupied_spaces(hum, bot) == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_empty_board():
    bot = [False, False, False, False, False, False, False, False, False]
    hum = [False, False, False, False, False, False, False, False, False]
    assert tic_tac_toe.empty_spaces(hum, bot) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
    assert tic_tac_toe.occupied_spaces(hum, bot) == []

def test_verify_occupied_spaces():
    assert tic_tac_toe.occupied_spaces([True, False, False, True, False, False, True, False, False], [True, False, False, False, False, False, True, False, False]) == [0, 3, 6]

def test_minimax_human_win_base_case():
    # Example: human wins
    human = [False, False, False, True, True, True, False, False, False]
    bot = [False, False, False, False, False, False, False, False, False]

    assert tic_tac_toe.minimax(human, bot, 0, False) == (-10, None)  # human wins

def test_minimax_best_move():
    human = [False, False, False, False, True, False, False, True, False]
    bot = [True, True, False, False, False, False, False, False, False]

    # It's bot's turn
    score, move = tic_tac_toe.minimax(human, bot, 0, True)

    assert move == 2
    assert score == 9  # Because bot wins

def test_minimax():
    human = [False, True, False, True, False, False, True, False, True]
    bot =   [True, False, True, False, True, False, False, True, False]

    score, move = tic_tac_toe.minimax(human, bot, 0, False)

    assert move == 5

