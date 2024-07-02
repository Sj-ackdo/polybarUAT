#!/usr/bin python3

from datetime import datetime, timezone
import time
import os

global epochTime
epochTime = 1704067200 # 01-01-2024 00:00:00
currentTime = int(datetime.now(timezone.utc).timestamp())

def getEpochTime():
    return currentTime - epochTime

def UATsv2():
    uat = getEpochTime()
    return round(uat / pow(42,2.4))     #UAT year equivalent

print("UATsv1:", getEpochTime(), "|", "UATsv2:", UATsv2())

