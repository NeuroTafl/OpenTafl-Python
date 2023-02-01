#!/usr/bin/env python3


import sys
sys.path.append("..")
import json

from AageNielsenTaflGame import AageNielsenTaflGame

g_AageGameTypeConfigurationFilename = "AageNielsen/AageNielsenData/GameTypeInformation/allGametypes.json"

def loadGameDat(gameJSONFilename: str) -> dict:
    ret = {}
    with open('allGameTypes.json', 'r') as file:
        data = file.read().replace('\n', '')

    ret = json.loads(data)

    aageGameTypeKey = ret["AageGameTypeKey"]

    openTaflRulesStr = lookupOpenTaflRulesStr(aageGameTypeKey, g_AageGameTypeConfigurationFilename)


    return ret

if __name__ == "__main__":
    print("Testing shit")

    testFilename = "AageNielsenData/GameJSONData/CopenhagenGamesJSON/game-16-1-6620.json"

    dat = loadGameDat(testFilename)


    print("Done.")