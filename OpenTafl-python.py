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
from pprint import pprint
from time import sleep, time
import sys, os


def parseArguments():
    parser = argparse.ArgumentParser(description='OpenTafl-python library for AI agents')

    parser.add_argument('-d', '--debug', action='store_true',
                    help='Set log level to debug')
    parser.add_argument('-q', '--quiet', action='store_true',
                    help='Set log level to quiet (errors only)')

    args = parser.parse_args()

    logLevel = logging.INFO
    if(args.quiet):
        logLevel = logging.WARNING
    if(args.debug):
        logLevel = logging.DEBUG

    logFilename = "/tmp/neurotafl.log"
    if os.name == 'nt':     # Tests if you're on windows
        logFilename = "c:\temp\neurotafl.log"

    logging.basicConfig(filename=logFilename,
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logLevel)

    return args


class OpenTaflAgent:
    def __init__(self, name: str):
        self.name = name
        self.log = logging.getLogger(__class__.__name__)

    def sendHello(self) -> None:
        self.log.debug("Sending hello handshake")
        sleep(0.1)        # If you hello too fast, OpenTafl crashes
        print("hello", flush=True)

    def sendStatus(self, message: str) -> None:
        self.log.debug(f"Sending status: {message}")
        print(f"status {message}", flush=True)

    def sendMove(self, message: str) -> None:
        self.log.info(f"Sending move: {message}")
        self.sendStatus(f"{self.name} Moving: {message}")
        print(f"move {message}", flush=True)

    def waitForNextMessage(self):
        message = input()
        return message


if __name__ == "__main__":
    done = False
    args = parseArguments()

    logging.info('--------------------------------------------------')
    logging.debug(args)
    logging.debug(sys.argv)

    logging.info('Starting NeuroTafl AI agent')

    agent = OpenTaflAgent("My agent name")
    agent.sendHello()
    agent.sendStatus('NeuroTafl Python engine online')
    agent.sendMove("d1-d2")

    while not done:
        message = agent.waitForNextMessage()
        logging.debug(message)

    sleep(30)

