# Testing the OpenTafl-python library

from NeuroTaflAgent.Coordinate import Coordinate


# ****************************************************************************
# ****************************************************************************
def test_CoordinateXYConstruct():
    x = 3
    y = 4
    coord = Coordinate(x=x, y=y)

    assert coord.x == x
    assert coord.y == y


def test_CoordinateXYChessConstructC5():
    expectedX = 2
    expectedY = 4
    chessNotation = "C5"
    coord = Coordinate(coordinate=chessNotation)

    assert coord.x == expectedX
    assert coord.y == expectedY


def test_CoordinateXYChessConstructK11():
    expectedX = 10
    expectedY = 10
    chessNotation = "K11"
    coord = Coordinate(coordinate=chessNotation)

    assert coord.x == expectedX
    assert coord.y == expectedY


def test_CoordinateXYChessConstructk10():
    expectedX = 10
    expectedY = 9
    chessNotation = "k10"
    coord = Coordinate(coordinate=chessNotation)

    assert coord.x == expectedX
    assert coord.y == expectedY


def test_CoordinateToString():
    chessNotation = "k10"
    coord = Coordinate(coordinate=chessNotation)
    assert str(coord) == chessNotation


def test_CoordinateXYConstruct76():
    expectedX = 7
    expectedY = 6
    coord = Coordinate(x=expectedX, y=expectedY)

    assert coord.getXIndex() == expectedX
    assert coord.getYIndex() == expectedY


def test_EqualsTrue():
    x = 3
    y = 10
    coordA = Coordinate(x=x, y=y)
    coordB = Coordinate(x=x, y=y)

    assert coordA == coordB


def test_EqualsFalse_differentX():
    x = 3
    y = 10
    coordA = Coordinate(x=x, y=y)
    coordB = Coordinate(x=x + 1, y=y)

    assert coordA != coordB


def test_EqualsFalse_differentY():
    x = 3
    y = 10
    coordA = Coordinate(x=x, y=y)
    coordB = Coordinate(x=x, y=y + 1)

    assert coordA != coordB
