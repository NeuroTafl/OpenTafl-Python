import logging
import pytest
import sys
from time import sleep
from io import StringIO

from OpenTaflConnector import OpenTaflConnector
from OpenTaflHandler import OpenTaflHandler
from TaflGame import TaflGame
from Move import Move

g_message = ""
openTaflMessage_finish0 = "finish 0\n"  # No end game state
openTaflMessage_finish1 = "finish 1\n"  # Tie game
openTaflMessage_finish2 = "finish 2\n"  # Attackers win
openTaflMessage_finish3 = "finish 3\n"  # Defenders game


def messageHandler(message: str) -> None:
    global g_message
    g_message = message


logging.basicConfig(level=logging.DEBUG)

#*************************************************************************
def test_BasicSetup():
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    assert True

def test_StatusMessage(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    message = "test UI message"
    handler.sendStatus(message)

    out, err = capsys.readouterr()
    print(out)
    assert "status" in out
    assert "test UI message"

def test_MoveMessage(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    moveOpenTaflNotation = "a5-j5"

    move = Move(openTaflNotation=moveOpenTaflNotation)
    handler.sendChosenMove(move)

    out, err = capsys.readouterr()
    print(out)
    assert "move" in out
    assert moveOpenTaflNotation in out

def test_HandleMessage_Finish0_NONE(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish0
    sys.stdin = StringIO(openTaflMessage_finish0)   # "Send" message to connector from OpenTafl server
    connector.run() # Start connector -- should push callback to handler
    sleep(0.1)

    assert not taflGame.isGameOver()

def test_HandleMessage_Finish1_TieGameOver(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish1
    sys.stdin = StringIO(openTaflMessage_finish1)   # "Send" message to connector from OpenTafl server
    connector.run() # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isTie()

def test_HandleMessage_Finish2_AttackersWin(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish2
    sys.stdin = StringIO(openTaflMessage_finish2)   # "Send" message to connector from OpenTafl server
    connector.run() # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isAttackerWin()

def test_HandleMessage_Finish3_DefendersWin(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish3
    sys.stdin = StringIO(openTaflMessage_finish3)   # "Send" message to connector from OpenTafl server
    connector.run() # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isDefenderWin()


