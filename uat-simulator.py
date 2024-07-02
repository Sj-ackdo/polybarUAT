#!/usr/bin python3

from datetime import datetime, timezone
import os

global epochTime
epochTime = 1704067200 # 01-01-2024 00:00:00
currentTime = int(datetime.now(timezone.utc).timestamp())

def getEpochTime():
    return currentTime - epochTime

def UATsv2():
    uat = getEpochTime()
    return round(uat / pow(42,2.4))     #UAT year equivalent

def calculateUAT():
    oneMinute = 60
    oneHour = 3600
    oneDay = 86400
    oneWeek = oneDay * 7
    oneMonth = oneWeek * 4
    oneMinuteSv2 = oneMinute / pow(42,2.4)
    oneHourSv2 = oneHour / pow(42,2.4)
    oneDaySv2 = oneDay / pow(42,2.4)
    oneWeekSv2 = oneWeek / pow(42,2.4)
    oneMonthSv2 = oneMonth / pow(42,2.4)
    print("UATsv2:\n", "1 minute", round(oneMinuteSv2, 2), "|", "1 hour:", round(oneHourSv2, 1), "paq", "|", "1 day:", round(oneDaySv2), "solz", "|", "1 week:", round(oneWeekSv2), "korsolz", "|", "1 month:", round(oneMonthSv2), "korpaq")

while True:
    calculateUAT()
    os.clear()