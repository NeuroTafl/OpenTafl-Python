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


from Coordinate import Coordinate
from Move import Move

t_simpleMove_b2c2 = "b2-c2"  # Taflman moves from b2 to c2
t_simpleMove_j5j9 = "j5-j9"  # Taflman moves from j5 to j9
t_simpleMove_c10d10 = "c10-d10"  # Taflman moves from c10 to d10
t_kingMove_h6b6 = "Kh6-b6"  # King moves from h6 to b6

t_taflmanMoveCap1 = "d3-d7xd8"  # Moves d3-d7, captures one @d8
t_taflmanMoveCap2 = "d3-d7xd8/e7"  # Moves d3-d7, captures @d8 & @e7
t_taflmanMoveCap3 = "d3-d7xd8/e7/c7"  # Moves d3-d7, captures @d8 & @e7 & @c7

t_taflmanMoveKingVulnerable = "f2-f3+"  # move threatens king
t_kingHasEscapeRoute = "Kk7-k2-"  # king moves to space with escape route (1 move win)
t_taflmanCapturesKing = "i9-i3++"  # king is captured by taflman
t_kingHasEscaped = "Ka8-a1--"  # king moves to space with escape route (1 move win)

t_resignationSymbol = "---"  # player resigns

# ****************************************************************************
# ****************************************************************************
def test_MoveToString():
    moveString = t_simpleMove_b2c2
    move = Move(openTaflNotation=moveString)
    assert str(move) == moveString


def test_MoveToString_doubleDigitIndicies():
    moveString = t_simpleMove_c10d10
    move = Move(openTaflNotation=moveString)
    assert str(move) == moveString


def test_MoveTestIndicies():
    moveString = t_simpleMove_j5j9
    move = Move(openTaflNotation=moveString)

    startXindex = 9
    startYindex = 4
    endXindex = 9
    endYindex = 8

    assert move.startingCoordinate.getXIndex() == startXindex
    assert move.startingCoordinate.getYIndex() == startYindex
    assert move.endingCoordinate.getXIndex() == endXindex
    assert move.endingCoordinate.getYIndex() == endYindex


def test_MoveKingSimple_h6b6():
    moveString = t_kingMove_h6b6
    move = Move(openTaflNotation=moveString)
    assert move.isKing()


def test_MoveNOTKingSimple():
    moveString = t_simpleMove_b2c2

    move = Move(openTaflNotation=moveString)
    assert not move.isKing()


def test_NoCaptures():
    moveString = t_simpleMove_c10d10
    move = Move(openTaflNotation=moveString)
    assert not move.hasCaptures()


def test_Capture1():
    moveString = t_taflmanMoveCap1
    expectedCaptures = [Coordinate(coordinate="d8")]

    move = Move(openTaflNotation=moveString)
    captures = move.getCaptures()

    assert move.hasCaptures()
    assert len(expectedCaptures) == len(captures)
    assert expectedCaptures == captures


def test_Capture2():
    moveString = t_taflmanMoveCap2
    expectedCaptures = [Coordinate(coordinate="d8"), Coordinate(coordinate="e7")]

    move = Move(openTaflNotation=moveString)
    captures = move.getCaptures()

    assert move.hasCaptures()
    assert len(expectedCaptures) == len(captures)
    assert expectedCaptures == captures


def test_Capture3():
    moveString = t_taflmanMoveCap3
    expectedCaptures = [
        Coordinate(coordinate="d8"),
        Coordinate(coordinate="e7"),
        Coordinate(coordinate="c7"),
    ]

    move = Move(openTaflNotation=moveString)
    captures = move.getCaptures()

    assert move.hasCaptures()
    assert len(expectedCaptures) == len(captures)
    assert expectedCaptures == captures


def test_KingVulnerable():
    moveString = t_taflmanMoveKingVulnerable
    move = Move(openTaflNotation=moveString)
    expectedIsVulnerable = True

    assert expectedIsVulnerable == move.isKingVulnerableToCapture()


def test_KingNOTVulnerable():
    moveString = t_simpleMove_b2c2
    move = Move(openTaflNotation=moveString)
    expectedIsVulnerable = False

    assert expectedIsVulnerable == move.isKingVulnerableToCapture()


def test_KingHasEscapeRoute():
    moveString = t_kingHasEscapeRoute
    move = Move(openTaflNotation=moveString)
    expectedKingHasEscapeRoute = True

    assert expectedKingHasEscapeRoute == move.kingHasEscapeRoute()


def test_KingHasNOEscapeRoute():
    moveString = t_kingMove_h6b6
    move = Move(openTaflNotation=moveString)
    expectedKingHasEscapeRoute = False

    assert expectedKingHasEscapeRoute == move.kingHasEscapeRoute()


def test_KingIsCaptured():
    moveString = t_taflmanCapturesKing
    move = Move(openTaflNotation=moveString)
    expectedKingIsCaptured = True

    assert expectedKingIsCaptured == move.isKingCaptured()


def test_KingIsNOTCaptured():
    moveString = t_simpleMove_c10d10
    move = Move(openTaflNotation=moveString)
    expectedKingIsCaptured = False

    assert expectedKingIsCaptured == move.isKingCaptured()


def test_KingIsEscaped():
    moveString = t_kingHasEscaped
    move = Move(openTaflNotation=moveString)
    expectedIsKingEscaped = True

    assert expectedIsKingEscaped == move.isKingEscaped()


def test_KingIsNOTEscaped():
    moveString = t_simpleMove_j5j9
    move = Move(openTaflNotation=moveString)
    expectedIsKingEscaped = False

    assert expectedIsKingEscaped == move.isKingEscaped()


def test_KingIsNOTEscaped2():
    moveString = t_kingMove_h6b6
    move = Move(openTaflNotation=moveString)
    expectedIsKingEscaped = False

    assert expectedIsKingEscaped == move.isKingEscaped()


def test_PlayerResigns():
    moveString = t_resignationSymbol
    move = Move(openTaflNotation=moveString)
    expectedHasPlayerResigned = True

    assert expectedHasPlayerResigned == move.hasPlayerResigned()


def test_PlayerNOTResigns():
    moveString = t_taflmanMoveCap2
    move = Move(openTaflNotation=moveString)
    expectedHasPlayerResigned = False

    assert expectedHasPlayerResigned == move.hasPlayerResigned()


def test_movesAreSame1():
    moveString = t_simpleMove_b2c2
    moveA = Move(openTaflNotation=moveString)
    moveB = Move(openTaflNotation=moveString)

    assert moveA == moveB


def test_movesAreSameKing():
    moveString = t_kingMove_h6b6
    moveA = Move(openTaflNotation=moveString)
    moveB = Move(openTaflNotation=moveString)

    assert moveA == moveB


def test_movesAreNOTSame1():
    moveStringA = t_simpleMove_b2c2
    moveStringB = t_simpleMove_j5j9
    moveA = Move(openTaflNotation=moveStringA)
    moveB = Move(openTaflNotation=moveStringB)

    assert moveA != moveB


def test_MoveToStrSimple():
    moveString = t_simpleMove_b2c2
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrKingSimple():
    moveString = t_kingMove_h6b6
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrCap1():
    moveString = t_taflmanMoveCap1
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrCap3():
    moveString = t_taflmanMoveCap3
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrKingVulnerable():
    moveString = t_taflmanMoveKingVulnerable
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrKingEscapeOpen():
    moveString = t_kingHasEscapeRoute
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrKingCaptured():
    moveString = t_taflmanCapturesKing
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrKingEscaped():
    moveString = t_kingHasEscaped
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToStrPlayerResigned():
    moveString = t_resignationSymbol
    move = Move(openTaflNotation=moveString)

    assert moveString == str(move)


def test_MoveToChessNotationStrCap3_d3_d7():
    moveString = t_taflmanMoveCap3
    expectedString = "d3-d7"
    move = Move(openTaflNotation=moveString)

    assert expectedString == move.toChessNotation()


def test_MoveToChessNotationStrCap3_k7_k2():
    moveString = t_kingHasEscapeRoute
    expectedString = "k7-k2"
    move = Move(openTaflNotation=moveString)

    assert expectedString == move.toChessNotation()
