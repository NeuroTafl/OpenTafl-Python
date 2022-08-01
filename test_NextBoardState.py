"/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
from Board import Board
from NextBoardState import NextBoardState

"k8-k9"


def test_getNext():
    boardState = NextBoardState(Board("/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"), "t")
    print(boardState.getNext("k8-k9"))
    assert boardState == "yes"

def test_capture():
    boardState = NextBoardState(Board("/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"), "t")
    print(boardState.getNext("k8-k9"))
    assert boardState == "yes"