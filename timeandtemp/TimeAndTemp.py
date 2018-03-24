# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:13:47 2018

@author: rjr


dataArr = []

with open("CityID.txt", "r") as file:
    x = file.readlines()
    for line in x:
        dataArr.append(line)
        

cityID = list(map(lambda cID: cID[0:6], dataArr))

# Enumerate in order to keep  track of the index that you're replacing
#message ellie resume
for ID in cityID:
    for chars in ID:
        if chars == '\t':
            print("1")
            chars = map(lambda x: chars.replace(x, "\t", ""), cityID)
        elif chars == "\t":
            print("2")
            chars.replace("t", " ")
        else:
            continue
        
with open("IDs.txt", "w") as IDFile:
    for i in cityID:
        IDFile.write(i)
        IDFile.write("\n")
        
    
"""
"""

ID.replace(ID, ID[0:5])
"""

import json
import requests 
import config
import tweepy
import datetime
import time


apiUrlBase = "http://api.openweathermap.org/data/2.5/weather?id="

def getInfo(apiUrlBase, weatherID="2172797"):
    apiUrl = apiUrlBase + weatherID + "&appid=" + config.weatherApiKey + "&units=imperial"
    response = requests.get(apiUrl)
    
    
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None


def getApi():
    auth = tweepy.OAuthHandler(config.twitterApiKey, config.twitterSecret)
    auth.set_access_token(config.twitterToken, config.twitterTokenSecret)
    return tweepy.API(auth)

#File the bot will tweet from
filename = open('IDs.txt','r')
f = filename.readlines()
filename.close()


# Loops through the file constantly to get the data and update the Twitter account

while True:
    for count, data in enumerate(f):
        # Setting the variables we want
        helloString = "Hey there "
        a = datetime.datetime.now()
        timeData = ("The time is: %02d:%02d" % (a.hour, a.minute))
        indicator = ["AM", "PM"]
        meridiem = ""
        if a.hour < 12:
            meridiem = indicator[0]
        else:
            meridiem = indicator[1]
        
        # Getting the information
        weatherData = getInfo(apiUrlBase, str(data[:7]))
        weatherInfo = weatherData["main"]["temp"]
        
        # Formatting the string and sending out the tweet
        tweet = helloString + str(data[8:-1])  + ".\n" + str(timeData) + meridiem + " ,and the temperature is", str(weatherInfo), "degrees fahrenheit."
        print(" ".join(tweet))
        #api = getApi() 
        #status = api.update_status(status = " ".join(tweet))
        time.sleep(10)