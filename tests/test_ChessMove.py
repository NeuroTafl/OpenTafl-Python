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
from NeuroTaflAgent.ChessMove import ChessMove

# Chess moves only have a simple start-end coordination notation
# It has no way to handle captures or resignations so far
t_simpleMove_b2c2 = "b2-c2"  # Taflman moves from b2 to c2
t_simpleMove_j5j9 = "j5-j9"  # Taflman moves from j5 to j9
t_simpleMove_c10d10 = "c10-d10"  # Taflman moves from c10 to d10

# ****************************************************************************
# ****************************************************************************
def test_ChessMove_b2c2():
    moveString = t_simpleMove_b2c2
    move = ChessMove(moveString=moveString)
    assert str(move) == moveString

def test_ChessMove_j5j9():
    moveString = t_simpleMove_j5j9
    move = ChessMove(moveString=moveString)
    assert str(move) == moveString

def test_ChessMove_doubleDigitIndicies():
    moveString = t_simpleMove_c10d10
    move = ChessMove(moveString=moveString)

    startCoordinate = Coordinate(coordinate="c10")
    endCoordinate = Coordinate(coordinate="d10")

    assert str(move) == moveString
    assert move.startingCoordinate == startCoordinate
    assert move.endingCoordinate == endCoordinate
