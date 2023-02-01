
from .Coordinate import Coordinate
from .Move import Move

class ChessMove (Move):
    def loadMoveString(self, moveString: str) -> None:
        self.loadChessNotation(moveString)

    def loadChessNotation(self, chessNotation: str) -> None:
        # "Chess" notation only handles chess-style stop/stop coordinates
        # Use Open Tafl Notation for full OpenTafl move notation/strings
        (startCoordinate, endCoordinate) = chessNotation.split("-", 1)
        self.startingCoordinate = Coordinate(coordinate=startCoordinate)
        self.endingCoordinate = Coordinate(coordinate=endCoordinate)
