"/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
from Board import Board
from MoveDecider import MoveDecider
from NextBoardState import NextBoardState
from TensorMoveDecider import TensorMoveDecider

"k8-k9"


def test_getNext():
    boardState = NextBoardState(Board("/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"), "t")
    print(boardState.getNext("k8-k9"))
    assert boardState == "yes"

def test_allMoves():
    boardState = NextBoardState(Board("/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"), "t")
    descision = MoveDecider()
    descision.board = boardState.cur_board
    list = descision.generateAllPossible("attackers")
    for move in list:
        print(boardState.getNext(move))

    assert boardState == "yes"

def test_capture():
    boardState = NextBoardState(Board("/3ttttt3/5t5/3tT6/t4t4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"), "t")
    next = boardState.getNext("f4-f3")
    print(next)
    assert next == "/3ttttt3/5t5/3t1t5/t3t4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"