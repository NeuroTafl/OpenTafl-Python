

from NeuroTaflAgent.Ply import Ply
from NeuroTaflAgent.Board import Board
from NeuroTaflAgent.Move import Move

g_copenhagen_BoardPosition_Start = (
    "/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
)

# ****************************************************
def test_PlayTerminalOutput():
    global g_copenhagen_BoardPosition_Start
    move = Move(openTaflNotation="c5-k5")
    board = Board(g_copenhagen_BoardPosition_Start)
    whoMoved = "attackers"

    ply = Ply(plyNumber=3, plyMove=move, plyBoard=board, positionRecord=board.getBoardPositionString(), whoMoved=whoMoved)

    print(ply)
    print()
    print(ply.getTerminalStr())

    # assert False
