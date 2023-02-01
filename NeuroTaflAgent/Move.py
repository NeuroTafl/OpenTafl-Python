
from .Coordinate import Coordinate

# ** *************************************************************************
class Move:
    def __init__(
        self,
        startingCoordinate: Coordinate = None,
        endingCoordinate: Coordinate = None,
        moveString: str = None
    ):
        self.startingCoordinate = startingCoordinate
        self.endingCoordinate = endingCoordinate

        self.taflmanSymbol = ""
        self.startSpace = ""
        self.endSpace = ""
        self.moveCaptures = []
        self.infoSymbol = ""
        self.moveString = moveString

        if moveString:
            self.loadMoveString(self.moveString)

    def loadMoveString(self, moveString: str) -> None:
        # Specific move types need to implement this - we have many move type notations now!
        raise NotImplementedError("Need to implment this in a subclass Move Type")

    def isKing(self) -> bool:
        return self.taflmanSymbol == "K"

    def hasCaptures(self) -> bool:
        return len(self.moveCaptures) > 0

    def getCaptures(self) -> list:
        return self.moveCaptures

    def isKingVulnerableToCapture(self) -> bool:
        return self.infoSymbol == "+"

    def kingHasEscapeRoute(self) -> bool:
        return self.infoSymbol == "-"

    def isKingCaptured(self) -> bool:
        return self.infoSymbol == "++"

    def isKingEscaped(self) -> bool:
        return self.infoSymbol == "--"

    def hasPlayerResigned(self) -> bool:
        return self.infoSymbol == "---"

    # Two moves are defined as being "equal" if their start and ending coordinates are the same
    # This leaves out whether it's a king or basic taflman moving, or if there's any captures
    # Not sure if we need to handle captures and piece types, but I don't think so (so far)
    def __eq__(self, otherMove) -> bool:
        return (
            self.startingCoordinate == otherMove.startingCoordinate
            and self.endingCoordinate == otherMove.endingCoordinate
        )

    def toChessNotation(self) -> str:
        return f"{self.startingCoordinate}-{self.endingCoordinate}"

    def __str__(self) -> str:
        ret = ""

        if self.hasPlayerResigned():
            ret += self.infoSymbol
        else:
            ret += self.taflmanSymbol
            ret += str(self.startingCoordinate)
            ret += "-"
            ret += str(self.endingCoordinate)
            ret += self.convertCapturesToOTMSpec()
            ret += str(self.infoSymbol)
        return ret

    def convertCapturesToOTMSpec(self) -> str:
        ret = ""
        if not self.hasCaptures():
            return ret
        else:
            ret += "x"
            coordinates = [str(x) for x in self.moveCaptures]
            ret += "/".join(coordinates)
            return ret
