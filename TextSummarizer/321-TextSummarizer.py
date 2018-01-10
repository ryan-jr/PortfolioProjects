# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 16:44:10 2017

@author: rjr

https://www.reddit.com/r/dailyprogrammer/comments/683w4s/20170428_challenge_312_hard_text_summarizer/?st=jbuzvkww&sh=6b3755be



"""

from collections import Counter
import statistics
import re
from collections import OrderedDict
from operator import itemgetter

def findAll(c, string):
  """Finds all indicies/instances of a character in a string 
  
     Given a string and a character c,  the method finds all instances/indicies 
     of the character and returns a list with the indicies of where the character 
     occurs.  
     
     Args:
     c: The character passed in that the method will find 
     string: The string to iterate over and find the character in 
     
     Returns:
     returns a list findList that contains the indicies of where the character occurs 
     
     Raises:
     N/A
  
  """
  
  findList = []
  ctr = 0
  stringList = list(string)
  for char in stringList:
    if c == char:
      findList.append(ctr)
      ctr += 1
    else:
      ctr += 1 
    
  return findList



def sentenceOrder(s, sentenceList):
    """Arranges sentences in a chronological order
    
        Takes in a mean value and a dictionary of sentence keys that have
        rankings/scores associated with them as values.  From this we filter out
        all of the sentneces below the mean, and arrange the sentences in a chronological
        order
    
    Args:
        mean: A mean value calculated from all of the sentence scores
        sentenceScoreDict: A dictionary with sentence/score key/value pairs
    
    Returns:
        N/A
        
    Raises:
        N/A
        
        
    """
    # TODO: What do I do if the highest score is the last item in dicitonary???
    # I think I would fail over into printing the first 3 keys
    
    return sentenceList.index(s)
    
        
    

def paraScore(paraString, stopWords):
    """Takes in a string of text and removes the stopwords
    
    We take in the string and remove the stopwords in order to get a unique count
    of all the words in the sentence
    
    Args:
        paraString:
        stopWords:
    
    Returns:
        Returns a dict with the number of times each unique word occurs in the paragraph
        
    Raises:
        N/A
        
        
    """
    # Going through and capitalizing stopwords to potentially remove them later
    capitalizedStopWords = []
    ctr = 0
    for i in stopWords:
        capitalizedStopWords.append(stopWords[ctr].capitalize())
        ctr += 1

    
    paraString = paraString.split(" ")

    # Looping through and removing the stopwords 
    for word in stopWords:
        if word in paraString:
            indexList = findAll(word, paraString)
            for i in indexList:
                paraString[i] = ""
    
    for word in capitalizedStopWords:
       if word in paraString:
            indexList = findAll(word, paraString)
            for i in indexList:
                paraString[i] = ""
      
    # Using filter to get rid of uneccessary spaces
    paraString = list(filter(None, paraString))

    
    # Finding the most interesting/most used words in the list to score
    data = Counter(paraString)
    commonWordList = data.most_common()
    
    # This section of the code is constructed to find a good value to 
    # establish what is "interesting/relevant" in the text provided
    # To do this we calculate both the median and the mode to try and get tendencies of both
    ctr = 0
    median = 0
    medianList = []
    
    
    
    for i in commonWordList:
        val = i[1]
        medianList.append(val)
        
    # Getting the median and mode for comparative values
    median = statistics.median(medianList)
    mode = statistics.mode(medianList)

    # Filtering out the mode to prevent an akward distribution
    medianList = list(filter(lambda x: x > mode, medianList))
    median = statistics.median(medianList)   
    
    
    for i in commonWordList:
        if commonWordList[ctr][1] < median:
            commonWordList[ctr] = ""
        ctr += 1

    commonWordList = list(filter(None, commonWordList))
    
    
    commonWords = []
    for i in commonWordList:
        commonWords.append(i[0])
        
    
    
    return commonWords

def stripText(paraString):
    """Takes in a string of text and removes what we don't want/need
    
    Args:
        paraString: A paragraph brought in as a string of text
        
    Returns:
        paraString: The original paramater modified to exclude what we don't want
        
    Raises:
        N/A   
    
    """

    
    excludeList = ["(", ")", "[", "]", "U.", "S.", "U.S."]
    
    if "(" in paraString:
        x = paraString.find(excludeList[0])
        
        y = paraString.find(excludeList[1])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
        
    if "[" in paraString:
        x = paraString.find(excludeList[2])
        
        y = paraString.find(excludeList[3])
        
        paraString = paraString[0:x] + "" + paraString[y + 1:-1]
        
    if "U.S." in paraString:
        x = paraString.find(excludeList[4])
        y = paraString.find(excludeList[5])
        
        paraString = paraString[0:x] + "US" + paraString[y + 2: -1]
    
    return paraString
       
    
 
def sentenceScore(interestingWords, sentenceList):
    """Scores each sentece based upon how many interesting words it has
    
    Arguments:
        interestingWords: A list of words that has been determined to be interesting
        sentenceList: A list of sentences contained in the text that was originally
                      passed in
                      
    Returns:
        Returns a summary of the text based on the score of sentences
        
    Raises:
        N/A
    """
    score = 0
    sentences = []
    scores = []

    
    for sentence in sentenceList:
        sentences.append(sentence.split(" "))
        
    for lists in sentences:
        score = 0
        for words in lists:
            if words in interestingWords:
                score += 1
        scores.append(score)

    # Taking care of anything that is a zero score in both the index and the sentence list
    scoreIndex = []
    ctr = 0
    for i in scores:
        if i == 0:
            scoreIndex.append(ctr)
        ctr += 1

    
    
    for i in scoreIndex:
        sentenceList[i] = ""
        
    sentenceList = list(filter(None, sentenceList))
    scores = list(filter(lambda x: x > 0, scores))

    
    sentenceScore = list(zip(sentenceList, scores))    
    
    print("Unique/interesting words from the provided text:", ", ".join(interestingWords))
    print()
    
    sentenceScore = dict(sentenceScore)
    sortedScores = OrderedDict(sorted(sentenceScore.items(), key = itemgetter(1), reverse = True))
    
    chronoList = []
    for i, k in enumerate(sortedScores):
        if i < 3:
            x = sentenceOrder(k, sentenceList)
            chronoList.append(x)

    chronoList = sorted(chronoList)
    for i in chronoList:
        print(sentenceList[i])



### Begin main()
    
# Reading stopwords, putting them into a list
f = open("stopWords.txt", "r")
stopList = f.readlines()
stopList = list(map(lambda s: s.strip(), stopList))



paraString = ""

with open("dataIn.txt", "r", encoding="utf8") as dataFile:
    paraString = dataFile.read().replace("\n", " ")
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
  
paraString = stripText(paraString)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
interestingWordList = paraScore(paraString, stopList)
paraString = re.sub("[?!]", ".", paraString)
sentenceList = paraString.split(". ")
sentenceScore(interestingWordList, sentenceList)
