# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 20:53:29 2018

@author: rjr
"""

# Building a flashcard app with a forgetting curve algo on the backend


import shelve
import random
import datetime



class Card(object):
    """Creates a card with a front/back to be put in a stack
    
        A card holds basic information in a cardHolder list 
        which includes the front of the card, back of the card,
        difficulty rating(based on user input), consecutive correct answers,
        and next due date(datetime object)
    
    Attributes:
        Ctr = initialized/used as a counter for card objects/numbering to make
              it easier for users to add, edit, and delete cards. 
              
    """
    ctr = 1
    
    def __init__(self, name = "", memScore = 0, cardHolder = []):
        self.memScore = memScore
        self.cardHolder = cardHolder
        self.name = name
        
        
    def makeCard(self, deckName):
        """Makes a basic card object
        
           Used to create cards with a front/back and stores additional information
           as needed.  
           
           Args:
               deckName: What the user wants to name the deck
               
           Returns:
               Card: returns a card object
               
           Raises:
               N/A
        """

        # Making the front and back of the card
        # Updating the list with the right values and creating the dict
        userFront = input("What do you want the front of the card to be?")
        userBack = input("What do you want the back of the card to be?")
        self.cardHolder.append(userFront)
        self.cardHolder.append(userBack)
        dictionary = {self.ctr : self.cardHolder}
         
        # Opening the file/db and updating it
        s = shelve.open("testShelf.db", writeback = True)
        s[deckName].update(dictionary)
        Card.ctr += 1
        
        # Writing the changes and clearing the list
        s.close()
        self.cardHolder.clear()
    
    def editCard():
        pass
    
    def deleteCard():
        pass

class Carddeck(object):
    
    def __init__(self, name = ""):
        self.name = name
        
    def createDeck(self, name):
        s = shelve.open("testShelf.db", writeback = True)
        s[name] = {}
        print(name, "created succsessfully!")
        s.close()
    
    def openDeck(self, deckName):
        s = shelve.open("testShelf.db")
        print(s[deckName])
        
    def listDeck(self):
        ctr = 1
        s = shelve.open("testShelf.db")
        for key in s:
            print(ctr, key)
            ctr += 1
        s.close()
    
    def findDeck(self, selection):
        ctr = 1
        s = shelve.open("testShelf.db")
        for key in s:
            if ctr == selection:
                l = Carddeck()
                print(l.openDeck(key))
            print(ctr, key)
            ctr += 1
        
    def deleteDeck(self, selection):
        ctr = 1
        s = shelve.open("testShelf.db")
        for key in s:
            if ctr == selection:
                print("Please type 'delete' to confirm you want to delete deck: ", key)
                userConfirm = input()
                if userConfirm == "delete":
                    del s[key]
                    print(key, "removed!")
                else:
                    print("deck", key, "Not removed!")
                
            ctr += 1
    
    def updateDeck(self, selection):
        # needs to take in user selection in the form of a number
        # match that selection with a key
        # 
        print("This is selection", selection)
        ctr = 1
        cardHolder = []
        s = shelve.open("testShelf.db", writeback = True)
        for key in s:
            if ctr == selection:
                userFront = input("What do you want the front of the card to be?")
                userBack = input("What do you want the back of the card to be?")
                cardHolder.append(userFront)
                cardHolder.append(userBack)
                dictionary = {len(s[key]) + 1: cardHolder}  
                s[key].update(dictionary)
                print(s[key])
                s.close()
                
            ctr += 1
        pass
    
    def sequentialReview(self, selection):
        ctr = 1
        s = shelve.open("testShelf.db")
        for key in s:
            if ctr == selection:
                x = s[key]
                for k, v in x.items():
                    print("Front of card",k,":", v[0], end="")
                    input("Press Enter to continue...")
                    print("**********")
                    print()
                    print()
                    print("Back of card:",k,":", v[1])
                    print()
                    print("**********")
            ctr += 1
    
    def randomReview(self, selection):
        ctr = 1
        s = shelve.open("testShelf.db")
        for key in s:
            if ctr == selection:
                
                x = s[key]
                rand = random.choice(list(x))
                while True:
                    print("Front of card", rand, ":", x[int(rand)][0])
                    input("Press Enter to continue...")
                    print("**********")
                    print()
                    print()
                    print("Back of card", rand, ":", x[int(rand)][1])
                    print()
                    print("**********")
                    rand = random.choice(list(x))
                    userQuit = input("Would you like to quit?(y/n)?")
                    if userQuit == "y":
                        break
            ctr += 1
    
    def worstReview(self, selection):
        pass
        
        
# Step 1: Create a card deck
    # A.  The card deck will be written via shelve to a file
    # B.  The name of the card deck will be the key, the value will be a dict object

# Step 2: Create a card object
    # A.  The card object will have a UUID as the key, and a front/back list as the value
    # B.  Write this complete object when done to the file
    
    # I need something so a user can review multiple cards 
    # I need something so a user can create another card
    
    
    
# Nice to haves
    # Stats for each card deck 
    # Review methods (sequentially, randomly, just the lowest(below X threshold))
    # For forgetting stats, would we need a datetime object(another nice to have), or just X days studied? (I think the later is OK, BUT the datetime object might be more complete/give more data)
"""
x = Carddeck("deck2")
print(x.createDeck())
x.listDeck()
"""

def deckSelection(num):
    deckNum = int(num)
    Carddeck.findDeck(deckNum)

def listDeck():
    Carddeck.listDeck()
    
def reviewDeck():
    pass


   
def options():
    print("1.  Create a card deck")
    print("2.  Review a card deck")
    print("3.  Edit a card deck")
    print("4.  Delete a card deck")
    print("5.  Exit")


userOption = True

# TODO: Refactor everything below this (abandon all hope all ye who enter here)

while userOption == True:
    options()
    userInput = input("What would you like to do: ")
    
    userInput = int(userInput)
    if userInput == 5:
        userOption = False
    elif userInput == 1:
        deckName = input("What would you like to name this deck?")
        x = Carddeck(deckName)
        x.createDeck(deckName)
        print("Creating a new card deck!")
        userBoolean = input("Would you like to add cards to this card deck?(y/n)")
        while userBoolean == "y":
            y = Card(deckName)
            y.makeCard(deckName)
            userBoolean = input("Would you like to add cards to this card deck?(y/n)")
        
    elif userInput == 2:
        l = Carddeck()
        l.listDeck()
        deckNum = input("Ok, which deck would you like to review?")
        userSelection = input("What type of review would you like: \n 1.  Sequential \n 2.  Random \n 3.  Spaced ")
        if userSelection == "1":
            l.sequentialReview(int(deckNum))
        elif userSelection == "2":
            print("Random review!")
            l.randomReview(int(deckNum))
            pass
        elif userSelection == "3":
            print("Spaced review!")
            pass
        
        
        
    elif userInput == 3:
        l = Carddeck()
        l.listDeck()
        deckNum = input("Ok, which deck would you like to edit?")
        userSelection = input("What would you like to do: \n 1.  Add a card \n 2.  Remove a card \n 3.  Update a card ")
        if userSelection == "1":
            print(deckNum)
            l.updateDeck(int(deckNum))
        elif userSelection == "2":
            print("Random review!")
            l.randomReview(int(deckNum))
            pass
        elif userSelection == "3":
            print("Card Update")
            
            
    elif userInput == 4:
        l = Carddeck()
        l.listDeck()
        deckNum = input("Ok, which deck number would you like to remove?")
        l.deleteDeck(int(deckNum))
        
print("Goodbye!")