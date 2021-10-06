from elo import *
import numpy as np

s = System()

# TODO: Elo matches between questions?
# TODO: Classes for students (different start rating)


# Add players
playercount = 5
# Add items
itemcount = 10
for p in range(playercount):
    s.addPlayer(str(p))

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 200, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])


# Simulation method (# of questions to answer per player, adaptibility range (-1 all random, 0 all adaptive))
def simulate(n, r):
    for p in range(playercount):
        for i in range(n):
            # All random questions
            if r == -1:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                s.game(player.name, item.name)
            # 'Perfect' adaptibility, always choose best question
            elif r == 0:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                for i in range(itemcount):
                    if np.absolute(player.rating - s.getItem(str(i)).rating) < np.absolute(player.rating - item.rating):
                        itemmatch = s.getItem(str(i))
                s.game(player.name, itemmatch.name)
            # r as acceptable elo range for questions
            else:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                while np.absolute(player.rating - item.rating) >= r:
                    item = s.getItem(str(np.random.randint(0, itemcount)))
                s.game(player.name, item.name)

print(s.getRatingList())

simulate(4, -1)

#print(s.getItemList())
print(s.getRatingList())