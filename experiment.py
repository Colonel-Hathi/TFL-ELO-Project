from elo import *
import numpy as np

s = System()

# Add players
s.addPlayer("a")
s.addPlayer("b", rating=900)

# Generate question list (mean, std dev, amount)
itemlist = np.random.normal(1000, 200, 100)

# TODO: Automate random player addition
# TODO: Elo matches between questions?
# TODO: Elo matching + adaptivity

def simulate(n):
    for i in range(n):
        s.game("a", "b")
    print("Rating of a:", s.getPlayerRating("a"))
    print("Rating of b:", s.getPlayerRating("b"))


#simulate(4)
