#
#
# Move notation documentation:
#  https://github.com/jslater89/OpenTafl/blob/master/opentafl-notation-spec.txt
#
# This is the standard OTN move record:
#  [taflman-symbol]<starting-space><move-type><ending-space>[capture-record][info-symbol]
#
# Alternative (unsupported so far for OpenTafl-Python) - Damian Walker's notation:
#  <starting-space><"-"><ending-space>[capture-record][info-symbol]
#


from NeuroTaflAgent.Coordinate import Coordinate
from NeuroTaflAgent.AageNielsenMove import AageNielsenMove

# Aage Nielsen's notation system for move notation
# No extra characters on moves like piece type or end of game states
# Resigned is just the string 'resigned'
# This *really* should be a subclassed Move type
# Berserk games use a very odd notation: i4e4 . e4c4 . c4c5 (3 moves?) - no capture info too
t_aageMove_simple_a5b5 = "a5-b5"
t_aageMove_singleCapture = "i4-c4xb4"
t_aageMove_doubleDigit_e10d10 = "e10-d10"
t_aageMove_doubleCapture = "k10-d10xc10xd11"
t_aageMove_resigned = "resigned"
t_aageMove_noHyphenCases_e1a1 = "e1a1"


# ** *************************************************************************
# **  Aage Neilsen Move types - http://aagenielsen.dk/
# ** *************************************************************************
def test_AageMoveToString():
    moveString = t_aageMove_simple_a5b5
    move = AageNielsenMove(moveString=moveString)
    assert str(move) == moveString


def test_AageMoveToString_doubleDigitIndicies():
    moveString = t_aageMove_doubleDigit_e10d10
    move = AageNielsenMove(moveString=moveString)
    assert str(move) == moveString

def test_aageMoveTestIndicies():
    moveString = t_aageMove_doubleDigit_e10d10 # e10-d10
    move = AageNielsenMove(moveString=moveString)
    startXindex = 4
    startYindex = 9
    endXindex = 3
    endYindex = 9

    assert move.startingCoordinate.getXIndex() == startXindex
    assert move.startingCoordinate.getYIndex() == startYindex
    assert move.endingCoordinate.getXIndex() == endXindex
    assert move.endingCoordinate.getYIndex() == endYindex

def test_Aage_Capture1():
    moveString = t_aageMove_singleCapture   # i4-c4xb4
    expectedCaptures = [Coordinate(coordinate="b4")]

    move = AageNielsenMove(moveString=moveString)
    captures = move.getCaptures()

    assert move.hasCaptures()
    assert len(expectedCaptures) == len(captures)
    assert expectedCaptures == captures

def test_Aage_Capture2():
    moveString = t_aageMove_doubleCapture # "k10-d10xc10xd11"
    expectedCaptures = [Coordinate(coordinate="c10"), Coordinate(coordinate="d11")]

    move = AageNielsenMove(moveString=moveString)
    captures = move.getCaptures()

    assert move.hasCaptures()
    assert len(expectedCaptures) == len(captures)
    assert expectedCaptures == captures

def test_Aage_PlayerResigns():
    moveString = t_aageMove_resigned
    move = AageNielsenMove(moveString=moveString)
    expectedHasPlayerResigned = True

    assert expectedHasPlayerResigned == move.hasPlayerResigned()

def test_Aage_NoHypensMoveNotation():
    moveString = t_aageMove_noHyphenCases_e1a1
    move = AageNielsenMove(moveString=moveString)

    expectedMoveStr = "e1-a1"

    assert expectedMoveStr == str(move)

