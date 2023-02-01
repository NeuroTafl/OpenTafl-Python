# Stores all data about a given Tafl Game

import logging

from .WinState import WinState
from .Move import Move
from .Ply import Ply
from .TaflRules import TaflRules
from .Board import Board
from .Side import Side


class TaflGame:
    def __init__(self, taflRules: TaflRules):

    #def __init__(self, openTaflRulesString=""):
        self.log = logging.getLogger(__class__.__name__)
        self.rules: TaflRules = taflRules

        # Game default values
        self.winState: WinState = WinState.NONE
        self.attackerPlayerName: str = "attackerName"
        self.defenderPlayerName: str = "defenderName"
        self.plys: list = []

        # Create starting board
        self.startingBoard: Board = Board(self.rules.getStartingPositionString())

        # Setup ply 0
        self.initializeGame()

    def initializeGame(self):
        self.addNextMove(None)

    def setAttackerPlayerName(self, newPlayerName: str) -> None:
        self.attackerPlayerName = newPlayerName

    def setDefenderPlayerName(self, newPlayerName: str) -> None:
        self.defenderPlayerName = newPlayerName

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

    def addNextMove(self, newMove: Move, whoMoved: Side = None) -> None:
        self.log.debug(f"Adding move {newMove}")
        nextPlyNumber = len(self.plys)
        newPly = Ply(number=nextPlyNumber, whoMoved=whoMoved, move=newMove)
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
        ret += f" Attacker: {self.attackerPlayerName} vs. Defender: {self.defenderPlayerName}\n"
        ret += f" Game over? {self.isGameOver()}\n"
        ret += f" OpenTafl rules string: {self.openTaflRulesString}\n"
        ret += "\n"
        ret += "Plys: \n"

        for ply in self.plys:
            ret += f"\t{ply}\n"

        return ret
