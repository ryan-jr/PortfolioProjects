# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 23:13:47 2018

@author: rjr
"""

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
        
            
print(cityID)
    

"""

ID.replace(ID, ID[0:5])
"""