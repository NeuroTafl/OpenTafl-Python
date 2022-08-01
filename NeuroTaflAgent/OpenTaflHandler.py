
import logging
from OpenTaflConnector import OpenTaflConnector
from TaflGame import TaflGame
from Move import Move
from WinState import WinState

class OpenTaflHandler:
    def __init__(self, taflGame: TaflGame):
        self.taflGame = taflGame
        self.openTaflConnector = None
        self.log = self.log = logging.getLogger(__class__.__name__)
        self.playCallbackHandler = None

    def setOpenTaflConnector(self, openTaflConnector: OpenTaflConnector):
        self.openTaflConnector = openTaflConnector
        self.openTaflConnector.registerMessageCallbackHandler(self.messageHandler)

    def registerPlayCallbackHandler(self, newHandlerMethod) -> None:
        self.playCallbackHandler = newHandlerMethod

    def sendChosenMove(self, move: Move) -> None:
        message = f"move {move.toChessNotation()}"
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

    def handlePlayMessage(self, message: str) -> None:
        (_, sideToPlay) = message.split(" ", 1)
        self.playCallbackHandler(self, self.taflGame, sideToPlay)

    def sendStatus(self, statusMessage: str) -> None:
        self.log.debug(f"Sending status: {statusMessage}")
        message = f"status {statusMessage}"
        self.openTaflConnector.sendMessageToServer(message)

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

    def handleRulesMessage(self, message: str) -> None:
        (_, payload) = message.split(" ", 1)
        self.log.debug(f"Received rules message: {payload}")
        (_, rules) = payload.split("start:", 1)
        self.currentBoardState = rules
        self.log.debug(f"Received rules message with rules: {rules}")
        # TODO: Need to parse & store up the rules message info
        # See the full spec file, but we don't need all of it
        # Primary one is the king armed flag
        raise Exception("Cannot handle rules yet!")

