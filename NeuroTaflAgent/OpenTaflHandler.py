import logging


from .OpenTaflConnector import OpenTaflConnector
from .TaflGame import TaflGame
#from .Move import Move
from .OpenTaflMove import OpenTaflMove
from .WinState import WinState
from .TaflRules import TaflRules


class OpenTaflHandler:
    def __init__(self, taflGame: TaflGame):
        self.taflGame = taflGame
        self.openTaflConnector = None
        self.log = self.log = logging.getLogger(__class__.__name__)
        self.playCallbackHandler = None
        self.taflRules = None
        self.lastMoveSent = OpenTaflMove()

    def setOpenTaflConnector(self, openTaflConnector: OpenTaflConnector):
        self.openTaflConnector = openTaflConnector
        self.openTaflConnector.registerMessageCallbackHandler(self.messageHandler)

    def registerPlayCallbackHandler(self, newHandlerMethod) -> None:
        self.playCallbackHandler = newHandlerMethod

    def sendChosenMove(self, move: OpenTaflMove) -> None:
        message = f"move {move.toChessNotation()}"
        self.lastMoveSent = move
        self.openTaflConnector.sendMessageToServer(message)

    def sendStatus(self, statusMessage: str) -> None:
        self.log.debug(f"Sending status: {statusMessage}")
        message = f"status {statusMessage}"
        self.openTaflConnector.sendMessageToServer(message)

    def messageHandler(self, message: str) -> None:
        self.log.debug(f"Recieved new message: {message}")
        if message.startswith("finish"):
            self.handleFinishMessage(message)
        elif message.startswith("rules"):
            self.handleRulesMessage(message)
        elif message.startswith("play"):
            self.handlePlayMessage(message)
        elif message.startswith("move"):
            self.handleMoveMessage(message)
        elif message.startswith("error"):
            self.handleErrorMessage(message)
        elif message.startswith("opponent-move"):
            self.handleOpponentMoveMessage(message)
        elif message.startswith("goodbye"):
            self.handleGoodbyeMessage(message)

    def handlePlayMessage(self, message: str) -> None:
        (_, sideToPlay) = message.split(" ", 1)
        self.log.debug(f"Play message for team: {sideToPlay}")
        self.playCallbackHandler(self.taflGame, sideToPlay)

    def handleFinishMessage(self, message: str) -> None:
        self.log.debug(f"Received finish message: {message}")
        (_, payload) = message.split(" ", 1)
        newWinState = WinState.NONE
        if payload == "0":
            newWinState = WinState.NONE
        elif payload == "1":
            newWinState = WinState.TIE
        elif payload == "2":
            newWinState = WinState.ATTACKER
        elif payload == "3":
            newWinState = WinState.DEFENDER
        else:
            self.log.error("Invalid win state payload from server")
            return
        self.taflGame.setWinState(newWinState)

    def handleErrorMessage(self, message: str) -> None:
        # no need to make the AI redo the move here because
        # open tafl handles this accordingly and resends a play.
        self.log.debug(f"Received error message: {message}")
        (_, error) = message.split(" ", 1)
        if error == "1":
            self.log.warning("Wrong Side Error")
        elif error == "2":
            self.log.warning("Invalid Move Error")
        elif error == "3":
            self.log.warning("Berserk Mode Wrong Side Error")
        elif error == "4":
            self.log.warning("Berserk Mode Illegal Move")
        else:
            self.log.warning(f"Unknown error message: {message}")

    def handleRulesMessage(self, message: str) -> None:
        (_, payload) = message.split(" ", 1)  # Take off "rules" message tag
        self.log.debug(f"Received rules message: {payload}")
        self.taflRules = TaflRules(openTaflRulesString=payload)

    # /4tt3/3tt4/4T4/t3T3t/ttTTKTTtt/t3T3t/4T4/4t4/3ttt3/
    def handleMoveMessage(self, message: str) -> None:
        (_, positionRecord) = message.split(" ", 1)
        self.log.debug(f"Received move message: {positionRecord}")
        self.taflGame.addNextMove(self.lastMoveSent, positionRecord=positionRecord)

    def handleOpponentMoveMessage(self, message: str) -> None:
        (_, moveStr, positionRecord) = message.split(" ", 2)
        opponentMove = OpenTaflMove(moveString=moveStr)
        self.log.debug(f"Received opponent-move message: {moveStr} {positionRecord}")
        self.taflGame.addNextMove(opponentMove, positionRecord=positionRecord)

