import re

from .Coordinate import Coordinate
from .Move import Move

class OpenTaflMove (Move):
    def loadMoveString(self, moveString: str) -> None:
        self.loadFromOpenTaflNotation(moveString)

    def loadFromOpenTaflNotation(self, openTaflNotation: str) -> None:
        # Move formating and parsing isn't simple.
        # See: https://soapbox.manywords.press/2016/01/27/tafl-opentafl-notation/
        # https://github.com/jslater89/OpenTafl/blob/master/opentafl-notation-spec.txt
        #
        # Basic format for the Open Tafl Move (OTM) spec is:
        # [taflman-symbol]<starting-space><move-type><ending-space>[capture-record][info-symbol]

        openTaflNotation = openTaflNotation.strip()  # kill whitespace, just in case

        # See line 62: https://github.com/jslater89/OpenTafl/blob/master/opentafl-notation-spec.txt
        # If the "move" is just "---" then the "move" was to resign
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


    
