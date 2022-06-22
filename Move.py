from Coordinate import Coordinate


class Move:
    def __init__(
        self,
        startingCoordinate: Coordinate = None,
        endingCoordinate: Coordinate = None,
        chessNotation: str = None,
    ):
        self.startingCoordinate = startingCoordinate
        self.endingCoordinate = endingCoordinate

        if chessNotation:
            self.loadChessNotation(chessNotation)

    def loadChessNotation(self, chessNotation: str) -> None:
        # TODO: This notation parsing is *way* too simple
        # Needs to handle kings, wins/loss, check, captures
        # See: https://soapbox.manywords.press/2016/01/27/tafl-opentafl-notation/
        (startCoordinate, endCoordinate) = chessNotation.split("-", 1)
        self.startingCoordinate = Coordinate(coordinate=startCoordinate)
        self.endingCoordinate = Coordinate(coordinate=endCoordinate)

    def __str__(self) -> str:
        return f"{str(self.startingCoordinate)}-{str(self.endingCoordinate)}"
