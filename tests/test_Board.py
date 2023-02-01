# import pytest

from copy import copy

from NeuroTaflAgent.Coordinate import Coordinate
from NeuroTaflAgent.Board import Board


g_copenhagen_BoardPosition_Start = (
    "/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
)
g_brandubh_BoardPosition_Start = "/3t3/3t3/3T3/ttTKTtt/3T3/3t3/3t3/"


def test_checkPositions_copenhagen():
    global g_copenhagen_BoardPosition_Start

    board = Board(g_copenhagen_BoardPosition_Start)

    coordA1 = Coordinate(coordinate="a1")
    coordD1 = Coordinate(coordinate="d1")
    coordF4 = Coordinate(coordinate="f4")
    coordK8 = Coordinate(coordinate="k8")

    expectedEmpty = True
    expectedBlocked = False

    assert expectedEmpty == board.checkCoord(coordA1)
    assert expectedBlocked == board.checkCoord(coordD1)
    assert expectedBlocked == board.checkCoord(coordF4)
    assert expectedBlocked == board.checkCoord(coordK8)


def test_MaxBoardDimensions_copenhagen():
    global g_copenhagen_BoardPosition_Start

    board = Board(g_copenhagen_BoardPosition_Start)
    expectedMaxY = 11
    expectedMaxX = 11

    assert expectedMaxY == board.getMaxY()
    assert expectedMaxX == board.getMaxX()


def test_MaxBoardDimensions_Brandubh():
    global g_brandubh_BoardPosition_Start

    board = Board(g_brandubh_BoardPosition_Start)
    expectedMaxY = 7
    expectedMaxX = 7

    assert expectedMaxY == board.getMaxY()
    assert expectedMaxX == board.getMaxX()


def test_getNewRowListFromRowString():
    rowStr1 = "ttKtt"
    expectedRowStr1List = ["t", "t", "K", "t", "t"]

    rowStr2 = "3"
    expectedRowStr2List = ["e", "e", "e"]

    rowStr3 = "5t5"
    expectedRowStr3List = ["e", "e", "e", "e", "e", "t", "e", "e", "e", "e", "e"]

    rowStr4 = "1K3t5"
    expectedRowStr4List = ["e", "K", "e", "e", "e", "t", "e", "e", "e", "e", "e"]

    rowStr5 = "10t"
    expectedRowStr5List = ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "t"]

    rowStr6 = "11"
    expectedRowStr6List = ["e", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]

    rowStr7 = "K10"
    expectedRowStr7List = ["K", "e", "e", "e", "e", "e", "e", "e", "e", "e", "e"]

    board = Board(rowStr1)

    assert expectedRowStr1List == board.getRowListFromRowString(rowStr1)
    assert expectedRowStr2List == board.getRowListFromRowString(rowStr2)
    assert expectedRowStr3List == board.getRowListFromRowString(rowStr3)
    assert expectedRowStr4List == board.getRowListFromRowString(rowStr4)
    assert expectedRowStr5List == board.getRowListFromRowString(rowStr5)
    assert expectedRowStr6List == board.getRowListFromRowString(rowStr6)
    assert expectedRowStr7List == board.getRowListFromRowString(rowStr7)


def test_toStr_output_copenhagen():
    global g_copenhagen_BoardPosition_Start
    board = Board(g_copenhagen_BoardPosition_Start)
    expectedStr = g_copenhagen_BoardPosition_Start
    assert expectedStr == str(board)


def test_toStr_output_brandubh():
    global g_brandubh_BoardPosition_Start
    board = Board(g_brandubh_BoardPosition_Start)
    expectedStr = g_brandubh_BoardPosition_Start
    assert expectedStr == str(board)


# Verifies that our board can be copied without a shallow (reference) copy happening
def test_copyBoard():
    global g_copenhagen_BoardPosition_Start
    global g_brandubh_BoardPosition_Start
    boardA = Board(g_brandubh_BoardPosition_Start)
    boardB = copy(boardA)

    boardB.setBoard(g_copenhagen_BoardPosition_Start)

    assert str(boardA) != str(boardB)


def test_boardIterator():
    global g_brandubh_BoardPosition_Start
    boardA = Board(g_brandubh_BoardPosition_Start)

    expectedPieceString = "eeeteeeeeeteeeeeeTeeettTKTtteeeTeeeeeeteeeeeeteee"
    foundPieceString = ""
    for boardPiece in boardA:
        foundPieceString += boardPiece

    assert expectedPieceString == foundPieceString


def test_getTerminalString_Copenhagen():
    global g_copenhagen_BoardPosition_Start
    board = Board(g_copenhagen_BoardPosition_Start)
    print(board.getTerminalStr())
    assert True


def test_getTerminalString_Brandubh():
    global g_brandubh_BoardPosition_Start
    board = Board(g_brandubh_BoardPosition_Start)
    print(board.getTerminalStr())
    assert True


def test_getTensor():
    global g_copenhagen_BoardPosition_Start
    board = Board(g_copenhagen_BoardPosition_Start)
    print(board.getTensor())
    assert True

