#!/usr/bin/env python3
#
# Simple agent that only makes one move and then gets stuck
#
# @author Aaron S. Crandall
# @contact crandall@gonzaga.edu
# @copyright 2022
#


import tensorflow as tf
from tensorflow import keras
import logging
import argparse
import sys
import os


from TensorMoveDecider import TensorMoveDecider
from OpenTaflAgent import OpenTaflAgent


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
    parser.add_argument("--log_file", help="Set log file location")

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


# ****************************************************************************
# This is where we need to hook in the AI code - whatever it is
def moveDecider(agent: OpenTaflAgent, sideToPlay: str, board) -> str:
    logging.info(f"Move decider called for: {sideToPlay}")
    logging.info("decider created " + board + " " + sideToPlay)
    decider = TensorMoveDecider()
    move = decider.decideMove(board, sideToPlay)
    logging.info(move)
    return move

# ****************************************************************************
if __name__ == "__main__":
    args = parseArguments()

    logging.info("--------------------------------------------------")
    logging.debug(args)
    logging.debug(sys.argv)

    logging.info("Starting One Move AI agent")

    openTaflConnector = OpenTaflAgent("One Move Dummy AI Agent")

    # Register callbacks for handling events by AI agent code
    openTaflConnector.registerMoveCallbackHandler(moveDecider)

    openTaflConnector.init()  # Send hello

    try:
        openTaflConnector.run()  # Blocks until game end
    except Exception as e:
        logging.error(f"Main run errored out with: {e}")

    logging.info("One Move Agent exiting.")
