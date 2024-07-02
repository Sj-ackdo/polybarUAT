#!/usr/bin python3

from datetime import datetime, timezone
import time
import os

global epochTime
epochTime = 1704067200 # 01-01-2024 00:00:00
currentTime = int(datetime.now(timezone.utc).timestamp())

def getEpochTime():
    return currentTime - epochTime

print(getEpochTime())
