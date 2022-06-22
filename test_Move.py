from Move import Move
# from Coordinate import Coordinate


# ****************************************************************************
# ****************************************************************************
def test_MoveToString():
    moveString = "b2-c2"
    move = Move(taflNotation=moveString)
    assert str(move) == moveString


def test_MoveTestIndicies():
    moveString = "j5-j9"
    move = Move(taflNotation=moveString)

    startXindex = 9
    startYindex = 4
    endXindex = 9
    endYindex = 8

    assert move.startingCoordinate.getXIndex() == startXindex
    assert move.startingCoordinate.getYIndex() == startYindex
    assert move.endingCoordinate.getXIndex() == endXindex
    assert move.endingCoordinate.getYIndex() == endYindex
