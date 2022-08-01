from pprint import pprint
import re

from Coordinate import Coordinate


class Move:
    def __init__(
        self,
        startingCoordinate: Coordinate = None,
        endingCoordinate: Coordinate = None,
        taflNotation: str = None,
        openTaflNotation: str = None,
    ):
        self.startingCoordinate = startingCoordinate
        self.endingCoordinate = endingCoordinate

        self.taflmanSymbol = ""
        self.startSpace = ""
        self.endSpace = ""
        self.moveCaptures = []
        self.infoSymbol = ""

        if taflNotation:
            self.loadChessNotation(taflNotation)

        if openTaflNotation:
            self.loadFromOpenTaflNotation(openTaflNotation)

    def loadChessNotation(self, chessNotation: str) -> None:
        # "Chess" notation only handles chess-style stop/stop coordinates
        # Use Open Tafl Notation for full OpenTafl move notation/strings
        (startCoordinate, endCoordinate) = chessNotation.split("-", 1)
        self.startingCoordinate = Coordinate(coordinate=startCoordinate)
        self.endingCoordinate = Coordinate(coordinate=endCoordinate)

    def loadFromOpenTaflNotation(self, openTaflNotation: str) -> None:
        # Move formating and parsing isn't simple.
        # See: https://soapbox.manywords.press/2016/01/27/tafl-opentafl-notation/
        # https://github.com/jslater89/OpenTafl/blob/master/opentafl-notation-spec.txt
        #
        # Basic format for the Open Tafl Move (OTM) spec is:
        # [taflman-symbol]<starting-space><move-type><ending-space>[capture-record][info-symbol]

        openTaflNotation = openTaflNotation.strip()  # kill whitespace, just in case

        # See line 62: https://github.com/jslater89/OpenTafl/blob/master/opentafl-notation-spec.txt
        # If the "move" is just "---" then it's a resignation by the next moving player
        if openTaflNotation == "---":
            self.infoSymbol = "---"
            return

        # If this regular expression doesn't look like magic, I need to retire
        regexString = r"^\s*(K)?(\S\d+)-(\S\d+)x?(\S\d+)?/?(\S\d+)?/?(\S\d+)?/?(\S\d+)?(-{1,2}|\+{1,2})?"
        taflmanTypeIndex = 1
        startSpaceIndex = 2
        endSpaceIndex = 3
        captureSetStartIndex = 4
        captureSetEndIndex = 7
        infoSymbolIndex = 8

        reMatch = re.search(regexString, openTaflNotation)

        if reMatch:
            # handle taflman type character (if there's one)
            if reMatch.group(taflmanTypeIndex) != None:
                self.taflmanSymbol = reMatch.group(taflmanTypeIndex)

            # handle the move start and end
            self.startingCoordinate = Coordinate(
                coordinate=reMatch.group(startSpaceIndex)
            )
            self.endingCoordinate = Coordinate(coordinate=reMatch.group(endSpaceIndex))

            # handle possible captures
            for groupNum in range(captureSetStartIndex, captureSetEndIndex + 1):
                currCaptureSpace = reMatch.group(groupNum)
                if currCaptureSpace:
                    self.moveCaptures.append(Coordinate(coordinate=currCaptureSpace))

            # handle info symbols (king threatened, escaped, captured, resigned)
            if reMatch.group(infoSymbolIndex):
                self.infoSymbol = reMatch.group(infoSymbolIndex)

        else:
            raise Exception(
                f"Move parse error: No regex match on input: {openTaflNotation}"
            )

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
