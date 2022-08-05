# Stores all data about a given Tafl Game

import logging

from .WinState import WinState
from .Move import Move
from .Ply import Ply
from .TaflRules import TaflRules


class TaflGame:
    def __init__(self, openTaflRulesString=""):
        self.log = logging.getLogger(__class__.__name__)
        self.openTaflRulesString = openTaflRulesString
        self.rules = None
        self.winState = WinState.NONE
        self.plys = []

        if self.openTaflRulesString:
            self.setOpenTaflRules(self.openTaflRulesString)
            self.addNextMove(None, positionRecord=self.rules.getStartingPositionString())

    def setOpenTaflRules(self, openTaflRulesString):
            self.rules = TaflRules(openTaflRulesString)

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

    def addNextMove(self, newMove: Move, positionRecord: str = None) -> None:
        self.log.debug(f"Adding move {newMove} -- {positionRecord}")
        nextPlyNumber = len(self.plys)
        newPly = Ply(plyNumber=nextPlyNumber, plyMove=newMove, positionRecord=positionRecord)
        self.plys.append(newPly)

        self.log.debug(str(self))

    def getCurrentPly(self):
        if len(self.plys) == 0:
            raise Exception(
                "Attempted to get a ply with empty set of plays in TaflGame"
            )
        return self.plys[-1]

    def __str__(self):
        ret = ""
        ret += f"Tafl Game ----------------------------\n"
        ret += f" Game over? {self.isGameOver()}\n"
        ret += "\n"
        ret += "Plys: \n"

        for ply in self.plys:
            ret += f"\t{ply}\n"

        return ret
