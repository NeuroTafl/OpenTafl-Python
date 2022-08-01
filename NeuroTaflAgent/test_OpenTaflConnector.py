import pytest
import sys
from io import StringIO
import logging
from time import sleep

from OpenTaflConnector import OpenTaflConnector

g_message = ""


def messageHandler(message: str) -> None:
    global g_message
    g_message = message


logging.basicConfig(level=logging.DEBUG)

# **************************************************************************#
def test_BasicMessageHandlingWorking():
    global g_message
    expectedMessage = "abc"
    sys.stdin = StringIO(expectedMessage)

    connector = OpenTaflConnector("Test Connector")
    connector.registerMessageCallbackHandler(messageHandler)
    connector.run()
    sleep(0.1)  # Must wait for connector thread to handle I/O

    assert g_message == expectedMessage


def test_HelloText(capsys):
    connector = OpenTaflConnector("Test Connector")
    connector.sendHello()
    out, err = capsys.readouterr()
    assert "hello" in out


def test_InitText(capsys):
    connector = OpenTaflConnector("Test Connector")
    connector.init()
    out, err = capsys.readouterr()
    assert "hello" in out
    assert "status" in out
    assert "Test Connector" in out
