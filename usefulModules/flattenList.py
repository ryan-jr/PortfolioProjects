# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 22:05:28 2018

@author: rjr
"""

def flattenList(nestedList):
  """Takes in a nested list and returns a flattened list 
  
  Args: 
    nestedList: The nested list in question 
  
  Returns:
    flatList: A flattned list 
    
  Raises:
    N/A 
  """
  flatList = []
  for sublist in nestedList:
    for item in sublist:
      flatList.append(item)
      
  return flatList