import json
import requests 
import config
import tweepy
import datetime
import time
import random
from dateutil import tz

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
filename = open('updatedIDs.txt','r')
f = filename.readlines()
filename.close()


# Loops through the file constantly to get the data and update the Twitter account
while True:
    cityID = random.choice(f)
    cityID = cityID.strip()
    weatherData = getInfo(apiUrlBase, str(cityID))
    cityName = weatherData["name"]
    cityTemp = weatherData["main"]["temp"]
    timeData = str(datetime.datetime.utcnow())
    currUTCTime = timeData[11:19]

    indicator = ["AM", "PM"]
    meridiem = ""
    
    if int(currUTCTime[:2]) < 12:
        meridiem = indicator[0]
    else:
        meridiem = indicator[1]

    timeString = "The current time is " + currUTCTime + meridiem + " " + "UTC,"
    timeString = str(timeString)
    
    # Appending to the list that will be later joined for the final tweet
    tweetList = []
    tweetList.append("Hey there")
    tweetList.append(str(cityName) + ".  ")
    tweetList.append("\n" + timeString)
    tweetList.append("and the temprature is")
    tweetList.append(str(cityTemp))
    tweetList.append("degrees farenheit.")
     
    tweet = ""
    tweet = " ".join(tweetList)

    api = getApi() 
    status = api.update_status(status = tweet)    

    tweetList = []
    time.sleep(900)

   
