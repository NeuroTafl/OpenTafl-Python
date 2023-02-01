
import re
from .Coordinate import Coordinate
from .Move import Move

class AageNielsenMove (Move):
    def loadMoveString(self, moveString: str) -> None:
        self.loadFromAageNielsenTaflNotation(moveString)

    def loadFromAageNielsenTaflNotation(self, aageNielsenNotation: str) -> None:
        aageNielsenNotation = aageNielsenNotation.strip()

        # Aage uses the full word 'resigned' instead of '---'
        if aageNielsenNotation.lower() == "resigned":
            self.infoSymbol = "---"
            return

        regexString = r"^\s*(\S\d+)-?(\S\d+)"

        reMatch = re.search(regexString, aageNielsenNotation)
        startSpaceIndex = 1
        endSpaceIndex = 2

        if reMatch:
            # handle the move start and end
            self.startingCoordinate = Coordinate(
                coordinate=reMatch.group(startSpaceIndex)
            )
            self.endingCoordinate = Coordinate(coordinate=reMatch.group(endSpaceIndex))
        else:
            raise Exception(
                f"Move parse error: No regex match on input: {aageNielsenNotation}"
            )

        reSearchCaptures = r"(x\S\d+)"
        foundCaptures = re.findall(reSearchCaptures, aageNielsenNotation)

        for currCaptureStr in foundCaptures:
            currCaptureStr = currCaptureStr[1:] # Take the 'x' off the front
            self.moveCaptures.append(Coordinate(coordinate=currCaptureStr))
