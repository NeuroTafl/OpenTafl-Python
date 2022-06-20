# Testing the OpenTafl-python library

import logging

from OpenTaflAgent import OpenTaflAgent


# ****************************************************************************
def stubMoveCallback(agent: OpenTaflAgent, sideToPlay: str) -> str:
    print("Move decider stub called")
    moveChosen = "a1-a2"
    return moveChosen


openTaflMessage_opponentMove1 = "opponent-move a4-a3 /3ttt3/4t4/t6T1/4T3t/ttTTKTTtt/t3T3t/4T4/1t7/3ttt3/"

# ****************************************************************************
# ****************************************************************************
def test_UnknownErrorMessageFromServer(caplog):
    caplog.set_level(logging.DEBUG)

    agent = OpenTaflAgent("Test Agent")
    agent.registerMoveCallbackHandler(stubMoveCallback)

    agent.handleErrorMessage(openTaflMessage_opponentMove1) # Act

    for record in caplog.records:
        print(record)

    expectedLogString = "Unknown"
    assert expectedLogString in caplog.text
