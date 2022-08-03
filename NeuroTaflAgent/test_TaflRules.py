from TaflRules import TaflRules


g_copenhagen = "dim:11 sw:w start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_copenhagen_strongShieldwalls = "dim:11 sw:s start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_copenhagen_edgeEscapes = "dim:11 efe:y start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_copenhagen_kingUnarmed = "dim:11 sw:w ka:n start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_copenhagen_kingArmed = "dim:11 sw:w ka:y start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_fetlar = "dim:11 start:/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
g_brandubh_weakKing = "dim:7 ks:n cenhe: cenh: start:/3t3/3t3/3T3/ttTKTtt/3T3/3t3/3t3/"


def test_CopenhagenBasic():
    global g_copenhagen
    taflRules = TaflRules(openTaflRulesString=g_copenhagen)

    expectedBoardDimension = 11
    expectedShieldWallWeak = True
    expectedKingArmed = True
    expectedStartingPositionString = (
        "/3ttttt3/5t5/11/t4T4t/t3TTT3t/tt1TTKTT1tt/t3TTT3t/t4T4t/11/5t5/3ttttt3/"
    )

    assert expectedBoardDimension == taflRules.getBoardDimension()
    assert expectedShieldWallWeak == taflRules.isShieldWallWeak()
    assert expectedKingArmed == taflRules.isKingArmed()
    assert expectedStartingPositionString == taflRules.getStartingPositionString()


def test_Copenhagen_KingUnarmed():
    global g_copenhagen_kingUnarmed
    taflRules = TaflRules(openTaflRulesString=g_copenhagen_kingUnarmed)

    expectedBoardDimension = 11
    expectedShieldWallWeak = True
    expectedKingArmed = False

    assert expectedBoardDimension == taflRules.getBoardDimension()
    assert expectedShieldWallWeak == taflRules.isShieldWallWeak()
    assert expectedKingArmed == taflRules.isKingArmed()


def test_Brandubh_weakKing_attackersFirst_CenterNotHostile():
    global g_brandubh_weakKing
    taflRules = TaflRules(openTaflRulesString=g_brandubh_weakKing)

    expectedBoardDimension = 7
    expectedShieldWallOff = True
    expectedKingArmed = True
    expectedStartingPositionString = "/3t3/3t3/3T3/ttTKTtt/3T3/3t3/3t3/"

    assert expectedBoardDimension == taflRules.getBoardDimension()
    assert expectedShieldWallOff == taflRules.isShieldWallOff()
    assert expectedKingArmed == taflRules.isKingArmed()
    assert expectedStartingPositionString == taflRules.getStartingPositionString()
