from main import smartishBot, build_neighbors, random_bot

neighbors = build_neighbors(5)
sideLength = 5
mines = 0


def test_smartishBot():
    won, time = smartishBot(sideLength, mines, neighbors)
    assert won
    assert time >= 0


def test_randomBot():
    won, time = random_bot(sideLength, mines, neighbors)
    assert won
    assert time >= 0
