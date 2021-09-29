from elo import *

s = System()

s.addPlayer("a")
s.addPlayer("b", rating=900)


def simulate(n):
    for i in range(n):
        s.game("a", "b")
    print("Rating of a:", s.getPlayerRating("a"))
    print("Rating of b:", s.getPlayerRating("b"))


simulate(4)
