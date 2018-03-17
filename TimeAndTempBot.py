import json
import requests 
import config
import tweepy
import datetime
import time
import random

apiUrlBase = "http://api.openweathermap.org/data/2.5/weather?id="

def getInfo(apiUrlBase, weatherID="2172797"):
    print(weatherID)
    print(list(weatherID))
    print(type(weatherID))
    apiUrl = apiUrlBase + weatherID + "&appid=" + config.weatherApiKey + "&units=imperial"
    print(apiUrl)
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
filename = open('updatedIDs.txt','r')
f = filename.readlines()
filename.close()
