from elo import *
import numpy as np

s = System()

# TODO: Elo matches between questions?
# TODO: Implement dynamic classes (maybe?)


# Add players
playercount = 100
# Add items
itemcount = 400

# Add Classes
s.addClass("a", 1000)
s.addClass("b", 900)

#print(s.getClass("b").startrating)

# Add players for each class
for p in range(playercount):
    if p < playercount / 2:
        s.addPlayer(str(p), "a", s.getClass("a").startrating)
        #s.addToClass("a", str(p))
    else:
        s.addPlayer(str(p), "b", s.getClass("b").startrating)
        #s.addToClass("b", str(p))

# Generate question list (mean, std dev, amount)
itemdist = np.random.normal(1000, 200, itemcount)
for i in range(itemcount):
    s.addItem(str(i), rating=itemdist[i])


# Simulation method (# of questions to answer per player, adaptability range (-1 all random, 0 all adaptive))
def simulate(n, r):
    for p in range(playercount):
        for i in range(n):
            # All random questions
            if r == -1:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                s.game(player.name, item.name)
            # 'Perfect' adaptability, always choose best question
            elif r == 0:
                itemmatch = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                for i in range(itemcount):
                    if np.absolute(player.rating - s.getItem(str(i)).rating) < np.absolute(player.rating - itemmatch.rating):
                        itemmatch = s.getItem(str(i))
                s.game(player.name, itemmatch.name)
            # r as acceptable elo range for questions
            else:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                while np.absolute(player.rating - item.rating) <= r:
                    item = s.getItem(str(np.random.randint(0, itemcount)))
                s.game(player.name, item.name)

print(s.getRatingList())

simulate(100, 0)

#print(s.getItemList())
print(s.getRatingList())