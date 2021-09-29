# Base implementation from: Elopy Copyright (c) 2017 HankMD under MIT license
import random

# Defines System implementation
class System:
    # Initialize class, base rating of 1000
    def __init__(self, base_rating=1000):
        self.base_rating = base_rating
        self.players = []

    # Return list of all players by name
    def __getPlayerList(self):
        return self.players

    # Return a specific player by name
    def getPlayer(self, name):
        for p in self.__getPlayerList():
            if p.name == name:
                return p
        return None

    # Add a player (rating optional)
    def addPlayer(self, name, rating=None):
        if rating == None:
            rating = self.base_rating
        self.players.append(_Player(name, rating))

    # Remove a player
    def removePlayer(self, name):
        self.__getPlayerList().remove(self.getPlayer(name))

    def game(self, player1, player2, winner=None):
        player1 = self.getPlayer(player1)
        player2 = self.getPlayer(player2)

        expected1 = player1.compareRating(player1, player2)
        expected2 = player2.compareRating(player2, player1)

        print("Expected probabilities P1:", expected1, "P2:", expected2)

        k = 20

        rating1 = player1.rating
        rating2 = player2.rating

        if random.random() <= expected1:
            print("1 wins")
            score1 = 1.0
            score2 = 0.0
        else:
            print("2 wins")
            score1 = 0.0
            score2 = 1.0

        if winner == player1.name:
            score1 = 1.0
            score2 = 0.0
        elif winner == player2.name:
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

        player1.rating = newRating1
        player2.rating = newRating2


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
            lst.append((player.name, player.rating))
        return lst

# Object class for the player
class _Player:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    # Method to compare player ratings and return expected score
    def compareRating(self, name, opponent):
        return ( 1+10**( ( opponent.rating-self.rating )/400.0 ) ) ** -1
