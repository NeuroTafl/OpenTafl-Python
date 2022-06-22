# Python3 wrapper for OpenTafl as an Agent
#
# @author Aaron S. Crandall
# @contact crandall@gonzaga.edu
# @copyright 2022
# @license GPL v3
#


import logging
from time import sleep
from enum import Enum


# ****************************************************************************
class WinState(Enum):
    NONE = 0
    TIE = 1
    ATTACKER = 2
    DEFENDER = 3


# ****************************************************************************
class OpenTaflAgent:
    def __init__(self, name: str):
        self.name = name
        self.log = logging.getLogger(__class__.__name__)

        self.winState = WinState.NONE
        self.moveCallbackHandler = None

        # TODO: unused data fields - but we'll need something for them
        # board state comes from these messages: rules, opponent-move, move
        self.currentBoardState = ""

        # an array of the current board
        self.board = None

        # needs to have this for detecting most recent moves for loops & forced moves
        # if you repeat a series more than x # of moves,
        #  you cannot do a given move to repeat it again
        self.moveHistory = []

    def getWinState(self) -> WinState:
        return self.winState

    def registerMoveCallbackHandler(self, newHandlerMethod) -> None:
        self.moveCallbackHandler = newHandlerMethod

    def sendHello(self) -> None:
        self.log.debug("Sending hello handshake")
        sleep(0.1)  # If you hello too fast, OpenTafl crashes
        self.sendMessageToServer("hello", "")

    def sendStatus(self, statusMessage: str) -> None:
        self.log.debug(f"Sending status: {statusMessage}")
        instruction = "status"
        self.sendMessageToServer(instruction, statusMessage)

    def sendMove(self, moveString: str) -> None:
        instruction = "move"
        self.sendStatus(f"{self.name} Moving: {moveString}")
        self.sendMessageToServer(instruction, moveString)

    def sendMessageToServer(self, instruction: str, options: str) -> None:
        message = instruction
        if options:
            message = instruction + " " + options
        self.log.debug(f"Sending to server: {message}")
        print(f"{message}\n", end="", flush=True)

    def waitForNextMessage(self) -> str:
        message = input().strip()
        return message

    def init(self) -> None:
        self.sendHello()
        self.sendStatus(f"{self.name} -- online")

    def run(self) -> None:
        if not self.moveCallbackHandler:
            self.log.error("Run started with move callback handler")
            raise Exception("Run started with move callback handler")

        done = False
        self.log.debug("Running main agent wait loop")

        while not done:
            message = self.waitForNextMessage()
            logging.debug(message)
            self.handleServerMessage(message)

            if message == "goodbye":
                done = True

        self.log.debug("Exiting main agent wait loop")

    def handleFinishMessage(self, message: str) -> None:
        self.log.debug(f"Received finish message: {message}")
        (_, payload) = message.split(" ", 1)
        if payload == "0":
            self.winState = WinState.NONE
        elif payload == "1":
            self.winState = WinState.TIE
        elif payload == "2":
            self.winState = WinState.ATTACKER
        elif payload == "3":
            self.winState = WinState.DEFENDER
        else:
            self.log.error("Invalid win state payload from server")

    def handleRulesMessage(self, message: str) -> None:
        (_, payload) = message.split(" ", 1)
        self.log.debug(f"Received rules message: {payload}")
        # TODO: Need to parse & store up the rules message info
        # See the full spec file, but we don't need all of it
        # Primary one is the king armed flag

    def handlePlayMessage(self, message: str) -> None:
        (_, sideToPlay) = message.split(" ", 1)

        moveChosen = self.moveCallbackHandler(self, sideToPlay, self.board)
        self.sendMove(moveChosen)

    # /4tt3/3tt4/4T4/t3T3t/ttTTKTTtt/t3T3t/4T4/4t4/3ttt3/
    def handleMoveMessage(self, message: str) -> None:
        (_, payload) = message.split(" ", 1)
        self.log.debug(f"Received move message: {payload}")
        self.currentBoardState = payload
        self.updateBoard()

    def handleOpponentMoveMessage(self, message: str) -> None:
        (_, payload) = message.split(" ", 1)
        (_, boardstate) = payload.split(" ", 1)
        self.log.debug(f"Received opponent-move message: {payload}")
        self.currentBoardState = boardstate
        self.updateBoard()

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

    def handleServerMessage(self, message: str) -> None:
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

    def updateBoard(self) -> None:
        rows = self.currentBoardState.split(sep="/")
        array = []
        for row in rows:
            new_row = []
            for piece in row:
                self.log.debug(piece)
                if piece.__contains__("t"):
                    new_row.append("t")
                elif piece.__contains__("T"):
                    new_row.append("T")
                elif piece.__contains__("K"):
                    new_row.append("K")
                else:
                    spaces = int(piece)
                    for x in range(spaces):
                        new_row.append("e")
            if len(new_row) > 0:
                array.append(new_row)
        array.reverse()
        self.board = array
        self.log.debug(array)
