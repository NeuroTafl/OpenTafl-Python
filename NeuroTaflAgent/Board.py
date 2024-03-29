# Stores a single Tafl board's piece state

from .Coordinate import Coordinate


class Board:
    def __init__(self, boardStatePositionString):
        self.board = []
        self.board.append([])  # Ensures a 2D board for indexing

        self.boardStatePositionString = boardStatePositionString
        self.setBoard(self.boardStatePositionString)

    def setBoard(self, newBoardPositionString: str) -> None:
        self.board = self.generateBoardArray(newBoardPositionString)

    def generateBoardArray(self, newBoardPositionString: str) -> list:
        newBoardList = []
        newBoardPositionString = newBoardPositionString.strip()
        rowPositionStrings = newBoardPositionString.split("/")
        for rowPositionString in rowPositionStrings:
            if (
                len(rowPositionString) < 1
            ):  # the split("/") generates an empty strings at front and back
                continue
            newRowList = self.getRowListFromRowString(rowPositionString)
            newBoardList.append(newRowList)
        return newBoardList

    def getRowListFromRowString(self, rowPositionString: str) -> list:
        newRowList = []
        currCharIndex = 0
        while currCharIndex < len(rowPositionString):
            if rowPositionString[currCharIndex].isdigit():
                emptyBucketCount = int(rowPositionString[currCharIndex])
                if (
                    currCharIndex < len(rowPositionString) - 1
                    and rowPositionString[currCharIndex + 1].isdigit()
                ):
                    emptyBucketCount = int(
                        rowPositionString[currCharIndex : currCharIndex + 2]
                    )
                    currCharIndex += 1  # skip second digit in main loop
                for _ in range(emptyBucketCount):
                    newRowList.append("e")
            else:
                newRowList.append(rowPositionString[currCharIndex])
            currCharIndex += 1
        return newRowList

    def getMaxY(self):
        return len(self.board)

    def getMaxX(self):
        return len(self.board[0])

    def getRowPositionString(self, rowList: list) -> str:
        rowString = ""
        currEmptyCount = 0
        for piece in rowList:
            if piece != "e":
                if currEmptyCount != 0:
                    rowString += str(currEmptyCount)
                    currEmptyCount = 0
                rowString += piece
            else:
                currEmptyCount += 1
        if currEmptyCount != 0:
            rowString += str(currEmptyCount)
        return rowString

    def getBoardPositionString(self) -> str:
        positionString = "/"
        for row in self.board:
            currRowString = self.getRowPositionString(row)
            positionString += f"{currRowString}/"
        return positionString

    def __str__(self):
        return self.getBoardPositionString()

    def checkCoord(self, coord: Coordinate) -> bool:
        if coord.y >= self.getMaxY() or coord.y < 0:
            return False
        if coord.x >= self.getMaxX() or coord.x < 0:
            return False

        if self.board[coord.y][coord.x] == "e":
            return True
        return False

    def removePieceAtCoord(self, coord: Coordinate) -> None:
        self.board[coord.getYIndex()][coord.getXIndex()] = "e"

    def setPieceAtCoord(self, coord: Coordinate, piece: str) -> None:
        self.board[coord.getYIndex()][coord.getXIndex()] = piece

    def getPieceAtCoord(self, coord: Coordinate) -> str:
        return self.board[coord.getYIndex()][coord.getXIndex()]

    def __iter__(self):
        return BoardIterator(self)

    def getTerminalStr(self):
        ret = ""

        ret += "   "
        for currX in range(self.getMaxX()):
            char = chr(currX+97)
            ret += f"{char} "
        ret += "\n"
        ret += "-" * ((self.getMaxX() + 1) * 2 + 1) + "\n"
        for currY in range(self.getMaxY()):
            ret += f"{currY+1:02}|"
            for currX in range(self.getMaxX()):
                ret += self.board[currY][currX]
                ret += "|"
            ret += "\n"
        ret += "-" * ((self.getMaxX() + 1) * 2 + 1)

        return ret


    def getTensor(self) -> str:
        # attacker,defender,king
        tensor = ""
        for row in self.board:
            for pos in row:
                if pos == "T":
                    tensor += "0,1,0,"
                elif pos == "t":
                    tensor += "1,0,0,"
                elif pos == "K":
                    tensor += "0,0,1,"
                else:
                    tensor += "0,0,0,"
        return tensor


# ****************************************************************************
class BoardIterator:
    def __init__(self, board: Board):
        self._board = board
        self._index = 0
        self._maxIndex = self._board.getMaxX() * self._board.getMaxY()


    def __next__(self):
        if self._index < self._maxIndex:
            result = ""
            currX = self._index % self._board.getMaxX()
            currY = int(self._index / self._board.getMaxX())

            result = self._board.board[currY][currX]

            self._index += 1
            return result
        else:
            raise StopIteration
