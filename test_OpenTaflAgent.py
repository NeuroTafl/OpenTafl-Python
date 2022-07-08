# Testing the OpenTafl-python library

import logging

from Board import Board
from MoveDecider import MoveDecider
from OpenTaflAgent import OpenTaflAgent, WinState


# ****************************************************************************
from TensorMoveDecider import TensorMoveDecider


def stubMoveCallback(agent: OpenTaflAgent, sideToPlay: str) -> str:
    print("Move decider stub called")
    moveChosen = "a1-a2"
    return moveChosen


OTM_opponentMove1 = (
    "opponent-move a4-a3 /3ttt3/4t4/t6T1/4T3t/ttTTKTTtt/t3T3t/4T4/1t7/3ttt3/"
)
OTM_Finish0 = "finish 0"  # No winner - qutting
OTM_Finish1 = "finish 1"  # Tie game
OTM_Finish2 = "finish 2"  # Attackers win
OTM_Finish3 = "finish 3"  # Defenders win


# ****************************************************************************
# ****************************************************************************
def test_UnknownErrorMessageFromServer(caplog):
    caplog.set_level(logging.DEBUG)

    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleErrorMessage(OTM_opponentMove1)  # Act

    for record in caplog.records:
        print(record)

    expectedLogString = "Unknown"
    assert expectedLogString in caplog.text


def test_HandleFinish0MessageNoWinner():
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleFinishMessage(OTM_Finish0)  # Act

    expectedWinState = WinState.NONE
    assert agent.getWinState() == expectedWinState


def test_HandleFinish1MessageTieGame():
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleFinishMessage(OTM_Finish1)  # Act

    expectedWinState = WinState.TIE
    assert agent.getWinState() == expectedWinState


def test_HandleFinish2MessageAttackersWin():
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleFinishMessage(OTM_Finish2)  # Act

    expectedWinState = WinState.ATTACKER
    assert agent.getWinState() == expectedWinState


def test_HandleFinish3MessageDefendersWin():
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleFinishMessage(OTM_Finish3)  # Act

    expectedWinState = WinState.DEFENDER
    assert agent.getWinState() == expectedWinState


def test_AgentSendHandshake(capsys):
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.sendHello()
    captured = capsys.readouterr()

    assert "hello\n" in captured.out


def test_moveArray():
    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.sendMove("move /4tt3/3tt4/4T4/t3T3t/ttTTKTTtt/t3T3t/4T4/4t4/3ttt3/")
    assert agent.board == "yes"

def test_moveArray():
    moveDecider = TensorMoveDecider()
    print(moveDecider.decideMove("/4tt3/3tt4/4T4/t3T3t/ttTTKTTtt/t3T3t/4T4/4t4/3ttt3/", "attackers"))
    print(moveDecider.board)

