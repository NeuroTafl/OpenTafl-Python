
from WinState import WinState


class TaflGame:
    def __init__(self):
        self.moves = []
        self.rules = ""
        self.dim = 0
        self.winState = WinState.NONE

    def setWinState(self, newWinState: WinState) -> None:
        self.winState = newWinState

    def isGameOver(self) -> bool:
        return self.winState in [WinState.ATTACKER, WinState.DEFENDER, WinState.TIE]

    def isAttackerWin(self) -> bool:
        return self.winState == WinState.ATTACKER

    def isDefenderWin(self) -> bool:
        return self.winState == WinState.DEFENDER

    def isTie(self) -> bool:
        return self.winState == WinState.TIE
