import logging

# <board-size> [lots of possible options] <positionRecordString>
# dim:\d{1,2}
# start:/..../


class TaflRules:
    def __init__(self, openTaflRulesString=None):
        self.openTaflRules = openTaflRulesString
        self.log = self.log = logging.getLogger(__class__.__name__)

        self.startingPosition = ""
        self.boardDimension = 1
        self.kingArmed = "y"  # 'n', 'a' - anvil, 'h' - hammer
        self.kingMode = (
            "s"
        )  # string, "c" - strong by throne, "m" - middleweight, "w" - weak everywhere
        self.shieldwallMode = (
            "n"  # 'w' weak (no corners) - 's' strong can do corners too
        )

        # Unimplemented so far
        self.whoMovesFirst = "attackers"  # "defenders"
        self.escapeLocation = "corner"  # "edge"

        if self.openTaflRules:
            self.parseOpenTaflRulesString(self.openTaflRules)

    def parseOpenTaflRulesString(self, openTaflRulesString: str):
        ruleStrings = openTaflRulesString.split()
        for ruleString in ruleStrings:
            self.handleRuleString(ruleString)

    def handleRuleString(self, ruleString: str):
        if ruleString.startswith("dim:"):
            self.parseDimensionString(ruleString)
        elif ruleString.startswith("sw:"):
            self.parseShieldWallModeString(ruleString)
        elif ruleString.startswith("ka:"):
            self.parseKingArmedString(ruleString)
        elif ruleString.startswith("start:"):
            self.parseStartPositionString(ruleString)
        else:
            self.log.warning(f"Did not handle OT Rules String: {ruleString}")

    def parseStartPositionString(self, ruleString: str):
        (_, positionString) = ruleString.split(":", 1)
        self.startingPosition = positionString

    def parseKingArmedString(self, ruleString: str):
        (_, kingArmedMode) = ruleString.split(":", 1)
        self.kingArmed = kingArmedMode

    def parseShieldWallModeString(self, ruleString: str):
        (_, shieldwallMode) = ruleString.split(":", 1)
        self.shieldwallMode = shieldwallMode

    def parseDimensionString(self, ruleString: str):
        (_, size) = ruleString.split(":", 1)
        self.boardDimension = int(size)

    def getBoardDimension(self):
        return self.boardDimension

    def isShieldWallOff(self):
        return self.shieldwallMode == "n"

    def isShieldWallWeak(self):
        return self.shieldwallMode == "w"

    def isShieldWallStrong(self):
        return self.shieldwallMode == "s"

    def isKingArmed(self):
        return self.kingArmed == "y"

    def isKingUnarmed(self):
        return self.kingArmed == "n"

    def isKingHammer(self):
        return self.kingArmed == "h"

    def isKingAnvil(self):
        return self.kingArmed == "a"

    def getStartingPositionString(self):
        return self.startingPosition
