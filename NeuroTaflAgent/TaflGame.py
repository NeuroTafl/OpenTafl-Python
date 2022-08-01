
from WinState import WinState
from Move import Move
from Ply import Ply


class TaflGame:
    def __init__(self):
        self.rules = ""
        self.winState = WinState.NONE
        self.plys = []

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

    def addNextMove(self, newMove: Move, positionRecord: str=None) -> None:
        nextPlyNumber = len(self.plys)
        newPly = Ply(nextPlyNumber, plyMove=newMove, positionRecord=positionRecord)
        self.plys.append(newPly)

    def getCurrentPly(self):
        if len(self.plys) == 0:
            raise Exception("Attempted to get a ply with empty set of plays in TaflGame")
        return self.plys[-1]

