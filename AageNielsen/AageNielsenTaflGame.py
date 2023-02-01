

from NeuroTaflAgent.TaflGame import TaflGame


class AageNielsenTaflGame(TaflGame):
    def __init__(self, aageNielsenGameDict: dict):
        self.openTaflRulesString = aageNielsenGameDict["openTaflRulesString"]

        super().__init__(
            openTaflRulesString=self.openTaflRulesString
        )



