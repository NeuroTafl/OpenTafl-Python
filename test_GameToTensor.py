

import numpy

from GameToTensor import GameToTensor
from NeuroTaflAgent.TaflGame import TaflGame

g_rules_copenhagen = "dim:11 name:Copenhagen atkf:y tfr:w sw:s efe:y start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"


# ****************************************************************************
def test_basic():
    global g_rules_copenhagen
    OTRules = g_rules_copenhagen
    taflGame = TaflGame(openTaflRulesString=OTRules)
    whoseTurn = "attackers"

    tensor = GameToTensor.generateCopenhagenTensor(taflGame, whoseTurn)

    print(tensor)

    assert True
