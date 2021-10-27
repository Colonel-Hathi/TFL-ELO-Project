# Base implementation from: Elopy Copyright (c) 2017 HankMD under MIT license
import random

# Defines System implementation
class System:
    g = 0
    # Initialize class, base rating of 1000
    def __init__(self, base_rating=1000):
        self.base_rating = base_rating
        self.players = []
        self.items = []
        self.classes = []

    # Return list of all players by name
    def __getPlayerList(self):
        return self.players

    def __getItemList(self):
        return self.items

    def __getClassList(self):
        return self.classes

    # Return a specific player by name
    def getPlayer(self, name):
        for p in self.__getPlayerList():
            if p.name == name:
                return p
        return None

    # Add a player (rating optional)
    def addPlayer(self, name, classname, rating=None):
        if rating == None:
            rating = self.base_rating
        self.players.append(_Player(name, classname, rating, []))

    # Remove a player
    def removePlayer(self, name):
        self.__getPlayerList().remove(self.getPlayer(name))

    def addClass(self, name, startrating):
        self.classes.append(_Class(name, startrating))

    def getClass(self, name):
        for c in self.__getClassList():
            if c.name == name:
                return c

    def getClasses(self):
        return self.classes

    def addToClass(self, classname, playername):
        c = self.getClass(classname)
        for p in self.__getPlayerList():
            if p.name == playername:
                c.addPlayerToClass(p)

    # Return a specific player by name
    def getItem(self, name):
        for i in self.__getItemList():
            if i.name == name:
                return i
        return None

    # Add an item
    def addItem(self, name, rating=None):
        if rating == None:
            rating = self.base_rating
        self.items.append(_Item(name, rating))

    # Remove an item
    def removeItem(self, name):
        self.__getItemList().remove(self.getItem(name))

    def game(self, player, item, winner=None):
        player = self.getPlayer(player)
        item = self.getItem(item)

        expected1 = player.compareRating(player, item)
        expected2 = item.compareRating(item, player)

        #print("Expected probabilities P1:", expected1, "P2:", expected2)

        k = 40

        rating1 = player.rating
        rating2 = item.rating
        if random.random() <= expected1:
            score1 = 1.0
            score2 = 0.0
        else:
            score1 = 0.0
            score2 = 1.0

        newRating1 = rating1 + k * (score1 - expected1)
        newRating2 = rating2 + k * (score2 - expected2)

        if newRating1 < 0:
            newRating1 = 0
            newRating2 = rating2 - rating1

        elif newRating2 < 0:
            newRating2 = 0
            newRating1 = rating1 - rating2

        player.rating = newRating1
        item.rating = newRating2

    def getPlayerRating(self, name):
        """
        Returns the rating of the player with the given name.
        @param name - name of the player.
        @return - the rating of the player with the given name.
        """
        player = self.getPlayer(name)
        return player.rating


    def getRatingList(self):
        """
        Returns a list of tuples in the form of ({name},{rating})
        @return - the list of tuples
        """
        lst = []
        for player in self.__getPlayerList():
            lst.append((player.name, player.classname, player.rating))
        return lst

    def getItemList(self):
        """
        Returns a list of tuples in the form of ({item},{rating})
        @return - the list of tuples
        """
        lst = []
        for item in self.__getItemList():
            lst.append((item.name, item.rating))
        return lst

# Object class for the player
class _Player:

    def __init__(self, name, classname, rating, itemsdone):
        self.name = name
        self.classname = classname
        self.rating = rating

    # Method to compare player ratings and return expected score
    def compareRating(self, name, opponent):
        return ( 1+10**( ( opponent.rating-self.rating )/400.0 ) ) ** -1


# Object class for question items
class _Item:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    # Method to compare player ratings and return expected score
    def compareRating(self, name, opponent):
        return ( 1+10**( ( opponent.rating-self.rating )/400.0 ) ) ** -1

class _Class:

    def __init__(self, name, startrating):
        self.name = name
        self.startrating = startrating
        self.classplayers = []

    # Method to add players
    def addPlayerToClass(self, player):
        self.classplayers.append(player)

    # Get players in class
    def getPlayersInClass(self, name):
        return self.classplayers