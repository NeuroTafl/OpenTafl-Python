#!/usr/bin/env python3
# Base class for all NeuroTafl Agents
# Should be inherited and methods overriden
# Should call __super__() in subclass __init__()


import logging
from time import sleep

from .OpenTaflConnector import OpenTaflConnector
from .OpenTaflHandler import OpenTaflHandler
from .TaflGame import TaflGame

from .Move import Move
from .Coordinate import Coordinate


class NeuroTaflAgent:
    def __init__(self, name:str = "Base NT Agent"):
        self.log = logging.getLogger(__class__.__name__)
        self.name = name
        self.taflGame = None
        self.openTaflConnector = None
        self.openTaflHandler = None

        self.log.debug(f"NeuroTafl agent base class init: {self.name}")

    def setup(self):
        self.taflGame = TaflGame()
        self.openTaflConnector = OpenTaflConnector(self.name)
        self.openTaflHandler = OpenTaflHandler(self.taflGame)
        self.openTaflHandler.setOpenTaflConnector(self.openTaflConnector)
        self.openTaflHandler.registerPlayCallbackHandler(self.playCallbackHandler)

    def run(self):
        self.openTaflConnector.init()
        self.openTaflConnector.run()

    def playCallbackHandler(self, taflGame: TaflGame, sideToPlay: str):
        self.log.debug(f"Play callback handler called for turn by: {sideToPlay}")
        raise NotImplementedError("Should override this by child class")

    def isAlive(self) -> bool:
        return self.openTaflConnector.isConnected()

    def teardown(self) -> None:
        self.log.debug("Tearing down NT agent -- Does nothing in base class")


