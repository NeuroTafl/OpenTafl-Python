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


from Move import Move

t_simpleMove_b2c2 = "b2-c2" # Taflman moves from b2 to c2
t_simpleMove_j5j9 = "j5-j9" # Taflman moves from j5 to j9
t_kingMove_h6b6 = "Kh6-b6"  # King moves from h6 to b6


# ****************************************************************************
# ****************************************************************************
def test_MoveToString():
    moveString = t_simpleMove_b2c2
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
    #move = Move(openTaflNotation=moveString)


