# For coordinate notation see:
# http://tafl.cyningstan.com/page/174/game-notation


class Coordinate:
    def __init__(self, x=None, y=None, coordinate=None):
        self.x = 0
        self.y = 0

        if x:
            self.x = x
        if y:
            self.y = y
        if coordinate:
            self.loadFromCoordinate(coordinate)

    def getXIndex(self) -> int:
        return self.x

    def getYIndex(self) -> int:
        return self.y

    def __str__(self):
        return f"{self.getTaflNotationX()}{self.getTaflNotationY()}"

    def getTaflNotationX(self) -> str:
        return chr(self.x + ord("a"))

    def getTaflNotationY(self) -> str:
        return str(self.y + 1)

    def loadFromCoordinate(self, coordinate: str) -> None:
        coordinate = coordinate.lower()
        xChr = ord(coordinate[0])
        xIndex = xChr - ord("a")

        yChr = int(coordinate[1:])
        yIndex = yChr - 1

        self.x = xIndex
        self.y = yIndex

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
