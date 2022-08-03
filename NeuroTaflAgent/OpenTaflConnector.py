import logging
from time import sleep
from threading import Thread


class OpenTaflConnector:
    def __init__(self, name):
        self.name = name
        self.done = False
        self.mainStdinWaitThread = Thread(target=self.mainStdinWait, daemon=True)
        self.log = logging.getLogger(__class__.__name__)

        self.messageCallbackHandler = None

    def registerMessageCallbackHandler(self, newHandlerMethod) -> None:
        self.messageCallbackHandler = newHandlerMethod

    def sendHello(self) -> None:
        self.log.debug("Sending hello handshake")
        sleep(0.1)  # If you hello too fast, OpenTafl crashes
        self.sendMessageToServer("hello")

    def sendMessageToServer(self, message) -> None:
        self.log.debug(f"Sending to server: {message}")
        print(f"{message}\n", end="", flush=True)

    def waitForNextMessage(self) -> str:
        message = input().strip()
        return message

    def init(self) -> None:
        self.sendHello()
        self.sendMessageToServer(f"status {self.name} -- online")

    def mainStdinWait(self) -> None:
        self.log.debug("Starting connector main wait method")
        while not self.done:
            try:
                message = self.waitForNextMessage()
                self.log.debug(message)
                self.handleServerMessage(message)
            except EOFError:
                self.done = True
        self.log.debug("Exiting connector main wait method ")

    def run(self) -> None:
        if not self.messageCallbackHandler:
            self.log.error("Run started with no registered callback handler")
            raise Exception("Run started with no registered callback handler")

        if not self.mainStdinWaitThread.is_alive():
            self.mainStdinWaitThread.start()
        else:
            raise Exception("Attempted to double-start connector thread")

        self.log.debug("Exiting main agent wait thread")

    # NOTE: This only kills the thread once a \n comes through the input()
    # Generating a true non-blocking killable thread will take more work
    def stop(self) -> None:
        self.done = True

    def handleServerMessage(self, message: str) -> None:
        self.messageCallbackHandler(message)
