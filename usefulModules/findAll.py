# Creating a findAll method 

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


s = ""

print(findAll("l", s))
