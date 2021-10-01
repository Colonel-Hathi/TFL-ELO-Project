from elo import *
import numpy as np

s = System()

# TODO: Elo matches between questions?
# TODO: Elo matching + adaptivity

# Add players
playercount = 10
itemcount = 100
for p in range(playercount):
    s.addPlayer(str(p))

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 200, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])


def simulaterandom(n):
    for p in range(playercount):
        for i in range(n):
            item = s.getItem(str(np.random.randint(0, itemcount)))
            player = s.getPlayer(str(p))
            s.game(player.name, item.name)

#print(s.getItemList())
print(s.getRatingList())

simulaterandom(4)

print(s.getRatingList())