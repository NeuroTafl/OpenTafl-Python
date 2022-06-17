#!/usr/bin/env python3
#
# Python3 wrapper for OpenTafl
#
# @author Aaron S. Crandall
# @contact crandall@gonzaga.edu
# @copyright 2022
# @license GPL v3
#


import logging
import argparse
from time import sleep
import sys, os
from enum import Enum

# from pprint import pprint


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

        # needs to have this for detecting most recent moves for loops & forced moves
        # if you repeat a series more than x # of moves,
        #  you cannot do a given move to repeat it again
        self.moveHistory = []

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
        message = instruction + " " + options
        self.log.debug(f"Sending to server: {message}")
        print(f"{message}", flush=True)

    def waitForNextMessage(self) -> str:
        message = input().strip()
        return message

    def init(self) -> None:
        self.sendHello()
        self.sendStatus("NeuroTafl Python engine online")

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
        (_, payload) = message.split(" ")
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

        moveChosen = self.moveCallbackHandler(self, sideToPlay)
        self.sendMove(moveChosen)

    def handleMoveMessage(self, message: str) -> None:
        self.log.debug(message)

    def handleOpponentMoveMessage(self, message: str) -> None:
            self.log.debug(message)

    def handleErrorMessage(self, message: str) -> None:
        # no need to make the AI redo the move here because
        # open tafl handles this accordingly and resends a play.
        self.log.debug(f"Received error message: {message}")
        (_, error) = message.split(" ")
        if error== "1":
            self.log.debug("Wrong Side Error")
        elif error == "2":
            self.log.debug("Invalid Move Error")
        elif error == "3":
            self.log.debug("Berserk Mode Wrong Side Error")
        elif error == "4":
            self.log.debug("Berserk Mode Illegal Move")


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
            self.handleErrorMessage(message)


# ****************************************************************************
def parseArguments():
    parser = argparse.ArgumentParser(
        description="OpenTafl-python library for AI agents"
    )

    parser.add_argument(
        "-d", "--debug", action="store_true", help="Set log level to debug"
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Set log level to quiet (errors only)",
    )

    args = parser.parse_args()

    logLevel = logging.INFO
    if args.quiet:
        logLevel = logging.WARNING
    if args.debug:
        logLevel = logging.DEBUG

    # TODO: add a command line option to set this (or make it None)
    logFilename = "/tmp/neurotafl.log"
    if os.name == "nt":  # Tests if you're on windows
        logFilename = r"E:\OpenTafl\OpenTafl Code\neurotafl.log"

    logging.basicConfig(
        filename=logFilename,
        filemode="a",
        format="%(asctime)s,%(msecs)d:%(name)s:%(levelname)s:%(message)s",
        datefmt="%H:%M:%S",
        level=logLevel,
    )

    return args


# ****************************************************************************
# This is where we need to hook in the AI code - whatever it is
def moveDecider(agent: OpenTaflAgent, sideToPlay: str) -> str:
    logging.info(f"Move decider called for: {sideToPlay}")

    if sideToPlay == "defenders":
        return "e3-h3"  # defender opening move
    else:
        return "d1-d2"  # attacker opening move


# ****************************************************************************
if __name__ == "__main__":
    args = parseArguments()

    logging.info("--------------------------------------------------")
    logging.debug(args)
    logging.debug(sys.argv)

    logging.info("Starting NeuroTafl AI agent")

    openTaflConnector = OpenTaflAgent("My agent name")

    # Register callbacks for handling events by AI agent code
    openTaflConnector.registerMoveCallbackHandler(moveDecider)

    openTaflConnector.init()  # Send hello
    openTaflConnector.run()  # Blocks until game end

    logging.info("Agent exiting.")
