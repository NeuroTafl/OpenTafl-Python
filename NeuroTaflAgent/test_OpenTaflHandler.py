import logging
import pytest
import sys
from time import sleep
from io import StringIO

from .OpenTaflConnector import OpenTaflConnector
from .OpenTaflHandler import OpenTaflHandler
from .TaflGame import TaflGame
from .Move import Move

g_message = ""
openTaflMessage_finish0 = "finish 0\n"  # No end game state
openTaflMessage_finish1 = "finish 1\n"  # Tie game
openTaflMessage_finish2 = "finish 2\n"  # Attackers win
openTaflMessage_finish3 = "finish 3\n"  # Defenders game

openTaflMessage_error1 = "error 1\n"  # Wrong side error
openTaflMessage_error2 = "error 2\n"  # Invalid move error
openTaflMessage_error3 = "error 3\n"  # Berserk Mode Wrong Side Error
openTaflMessage_error4 = "error 4\n"  # Berserk Mode Illegal Move
openTaflMessage_errorUnk = "error 89\n"  # Unknown error type

openTaflMessage_rulesCopenhagen = "rules dim:11 sw:w start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"


def messageHandler(message: str) -> None:
    global g_message
    g_message = message


logging.basicConfig(level=logging.DEBUG)

# *************************************************************************
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
    sys.stdin = StringIO(
        openTaflMessage_finish0
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert not taflGame.isGameOver()


def test_HandleMessage_Finish1_TieGameOver(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish1
    sys.stdin = StringIO(
        openTaflMessage_finish1
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isTie()


def test_HandleMessage_Finish2_AttackersWin(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish2
    sys.stdin = StringIO(
        openTaflMessage_finish2
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isAttackerWin()


def test_HandleMessage_Finish3_DefendersWin(capsys):
    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_finish3
    sys.stdin = StringIO(
        openTaflMessage_finish3
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert taflGame.isGameOver()
    assert taflGame.isDefenderWin()


def test_OTS_ErrorMessage1(caplog):
    expectedMessage = "Wrong Side Error"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_error1
    sys.stdin = StringIO(
        openTaflMessage_error1
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert expectedMessage in caplog.text


def test_OTS_ErrorMessage2(caplog):
    expectedMessage = "Invalid Move Error"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_error2
    sys.stdin = StringIO(
        openTaflMessage_error2
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert expectedMessage in caplog.text


def test_OTS_ErrorMessage3(caplog):
    expectedMessage = "Berserk Mode Wrong Side Error"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_error3
    sys.stdin = StringIO(
        openTaflMessage_error3
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert expectedMessage in caplog.text


def test_OTS_ErrorMessage4(caplog):
    expectedMessage = "Berserk Mode Illegal Move"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_error4
    sys.stdin = StringIO(
        openTaflMessage_error4
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert expectedMessage in caplog.text


def test_OTS_ErrorMessageUnk(caplog):
    expectedMessage = "Unknown error message"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_errorUnk
    sys.stdin = StringIO(
        openTaflMessage_errorUnk
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    assert expectedMessage in caplog.text


def test_OTS_Rules_Copenhagen(caplog):
    expectedMessage = "Wrong Side Error"

    taflGame = TaflGame()
    connector = OpenTaflConnector("Test Connector")
    handler = OpenTaflHandler(taflGame)
    handler.setOpenTaflConnector(connector)

    global openTaflMessage_rulesCopenhagen
    sys.stdin = StringIO(
        openTaflMessage_rulesCopenhagen
    )  # "Send" message to connector from OpenTafl server
    connector.run()  # Start connector -- should push callback to handler
    sleep(0.1)

    taflRules = handler.taflRules

    # "dim:11 sw:w start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"

    expectedDimension = 11
    expectedStartPosition = (
        "/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
    )

    assert expectedDimension == taflRules.getBoardDimension()
    assert expectedStartPosition == taflRules.getStartingPositionString()
