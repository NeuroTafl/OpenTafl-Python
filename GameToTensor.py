
import numpy
from NeuroTaflAgent.TaflGame import TaflGame
from NeuroTaflAgent.Board import Board

class GameToTensor:
    def __init__(self):
        pass

    def pieceToNumpyArray(pieceString: str):
        if pieceString == 'e':
            return numpy.array([0,0,0])
        elif pieceString == 't':
            return numpy.array([1,0,0])
        elif pieceString == 'T':
            return numpy.array([0,1,0])
        elif pieceString == 'K':
            return numpy.array([0,0,1])

    def whoseTurnToNumpyArray(whoseTurn: str) -> numpy.array:
        if whoseTurn == "attackers":
            return numpy.array([1,0])
        elif whoseTurn == "defenders":
            return numpy.array([0,1])
        else:
            raise Exception(f"Invalid turn for building array: {whoseTurn}")

    def generateCopenhagenTensor(taflGame: TaflGame, whoseTurn: str):
        #numpyTensor = numpy.empty([1])
        currPly = taflGame.getCurrentPly()
        currBoard = currPly.getBoard()

        print("Adding whose turn")
        numpyTensor = GameToTensor.whoseTurnToNumpyArray(whoseTurn)
        #numpyTensor = numpy.append(numpyTensor, GameToTensor.whoseTurnToNumpyArray(whoseTurn))

        print(numpyTensor)

        print("Adding current board as one-hot")
        for pieceString in currBoard:
            numpyTensor = numpy.append(numpyTensor, GameToTensor.pieceToNumpyArray(pieceString))

        print(numpyTensor)



