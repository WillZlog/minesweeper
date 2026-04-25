import random

from main import (
    MINE,
    apply_reveal,
    build_board,
    build_neighbors,
    flood_fill,
    random_bot,
    reveal_square,
    smartishBot,
)


def test_build_neighbors_corner():
    neighbors = build_neighbors(3)
    assert set(neighbors[0]) == {1, 3, 4}


def test_build_neighbors_center():
    neighbors = build_neighbors(3)
    assert set(neighbors[4]) == {0, 1, 2, 3, 5, 6, 7, 8}


def test_build_board_correct_number_of_mines():
    random.seed(0)
    side = 5
    neighbors = build_neighbors(side)
    board = build_board(side, 4, neighbors)
    assert board.count(MINE) == 4


def test_reveal_square_mine_loses_game():
    board = [MINE]
    hidden = [True]
    state = {"game_over": False, "won": False, "safe_left": 0}

    result = reveal_square(0, board, hidden, state, 1)

    assert result is False
    assert state["game_over"] is True
    assert state["won"] is False
    assert hidden[0] is False


def test_reveal_square_safe_tile_returns_value():
    board = [0]
    hidden = [True]
    state = {"game_over": False, "won": False, "safe_left": 1}

    result = reveal_square(0, board, hidden, state, 0)

    assert result is True
    assert state["game_over"] is True
    assert state["won"] is True
    assert hidden[0] is False


def test_reveal_square_already_revealed_returns_none():
    board = [0]
    hidden = [False]
    state = {"game_over": False, "won": False, "safe_left": 1}

    result = reveal_square(0, board, hidden, state, 0)

    assert result is None


def test_flood_fill_reveals_connected_zero_region():
    side = 3
    neighbors = build_neighbors(side)

    board = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    hidden = [True] * 9
    state = {"game_over": False, "won": False, "safe_left": 9}
    clues = {}

    flood_fill(0, board, hidden, state, neighbors, 0, clues)

    assert all(h is False for h in hidden)
    assert state["won"] is True
    assert state["game_over"] is True


def test_flood_fill_records_number_clues():
    side = 3
    neighbors = build_neighbors(side)

    board = [
        0,
        1,
        MINE,
        0,
        1,
        1,
        0,
        0,
        0,
    ]
    hidden = [True] * 9
    state = {"game_over": False, "won": False, "safe_left": 8}
    clues = {}

    flood_fill(0, board, hidden, state, neighbors, 1, clues)

    assert 1 in clues
    assert clues[1] == 1


def test_apply_reveal_stores_clue():
    side = 2
    neighbors = build_neighbors(side)

    board = [1, MINE, 1, 1]
    hidden = [True] * 4
    state = {"game_over": False, "won": False, "safe_left": 3}
    clues = {}

    result = apply_reveal(0, board, hidden, state, 1, clues, neighbors)

    assert result == 1
    assert clues[0] == 1


def test_apply_reveal_zero_mine_board_finishes_game():
    side = 5
    neighbors = build_neighbors(side)
    board = [0] * (side * side)
    hidden = [True] * (side * side)
    state = {"game_over": False, "won": False, "safe_left": side * side}
    clues = {}

    result = apply_reveal(0, board, hidden, state, 0, clues, neighbors)

    assert state["game_over"] is True
    assert state["won"] is True
    assert result == "break" or result == 0


def test_random_bot_returns_bool_and_nonnegative_time():
    neighbors = build_neighbors(5)
    won, elapsed = random_bot(5, 3, neighbors)

    assert isinstance(won, bool)
    assert elapsed >= 0


def test_smartishBot_returns_bool_and_nonnegative_time():
    neighbors = build_neighbors(5)
    won, elapsed = smartishBot(5, 3, neighbors)

    assert isinstance(won, bool)
    assert elapsed >= 0


def test_smartishBot_zero_mines_always_wins():
    neighbors = build_neighbors(5)
    won, elapsed = smartishBot(5, 0, neighbors)

    assert won is True
    assert elapsed >= 0
