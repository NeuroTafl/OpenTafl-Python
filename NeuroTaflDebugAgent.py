#!/usr/bin/env python3
# Simple "hello" agent to verify we can standup and work with OT server

import logging
import sys
import argparse
from time import sleep

from NeuroTaflAgent.NeuroTaflAgent import NeuroTaflAgent

from NeuroTaflAgent.Move import Move
from NeuroTaflAgent.Coordinate import Coordinate
from NeuroTaflAgent.TaflGame import TaflGame


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
    parser.add_argument("--log_file", help="Set log file location")

    args = parser.parse_args()

    logLevel = logging.INFO
    if args.quiet:
        logLevel = logging.WARNING
    if args.debug:
        logLevel = logging.DEBUG

    # TODO: add a command line option to set this (or make it None)
    logFilename = "/tmp/neurotafl.log"
    if args.log_file:
        logFilename = args.log_file

    logging.basicConfig(
        filename=logFilename,
        filemode="a",
        format="%(asctime)s,%(msecs)d:%(name)s:%(levelname)s:%(message)s",
        datefmt="%H:%M:%S",
        level=logLevel,
    )

    return args


class NeuroTaflDebugAgent(NeuroTaflAgent):
    def __init__(self, name="NT Debug Agent"):
        super().__init__(name=name)
        self.log.debug("Starting Debug Agent class")
        self.turn = 0

    def playCallbackHandler(self, taflGame: TaflGame, sideToPlay: str):
        sleep(3)
        startCoordinate = Coordinate(coordinate="d1")
        endCoordinate = Coordinate(coordinate="d2")

        if self.turn % 2 == 0:
            move = Move(startingCoordinate=startCoordinate, endingCoordinate=endCoordinate)
        else:
            move = Move(startingCoordinate=endCoordinate, endingCoordinate=startCoordinate)
        self.turn += 1

        self.openTaflHandler.sendChosenMove(move)


# ****************************************************************************
if __name__ == "__main__":
    args = parseArguments()

    logging.info("--------------------------------------------------")
    logging.debug(args)
    logging.debug(sys.argv)

    logging.info("Starting NeuroTafl Hello Debug AI agent")

    #neuroTaflHelloAgent = NeuroTaflAgent(name="Hello Only Agent")
    neuroTaflHelloAgent = NeuroTaflDebugAgent(name="Debug NT Agent")
    neuroTaflHelloAgent.setup()
    neuroTaflHelloAgent.run()

    try:
        while neuroTaflHelloAgent.isAlive():
            sleep(1)
    except Exception as e:
        logging.error(f"Main run errored out with: {e}")
    finally:
        neuroTaflHelloAgent.teardown()

    logging.info("Agent exiting.")
