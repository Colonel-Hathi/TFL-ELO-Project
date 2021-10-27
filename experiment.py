from elo import *
import numpy as np

s = System()

# TODO: Elo matches between questions?


# Add players
playercount = 30
# Add items
itemcount = 4000

# Add Classes
s.addClass("a", 1000)
s.addClass("b", 1000)

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
        print("Still going! At:", p, "%")
        #notdone = True
        for i in range(n):
            # All random questions
            if r == -1:
                item = s.getItem(str(np.random.randint(0, itemcount)))
                player = s.getPlayer(str(p))
                s.game(player.name, item.name)
                check = True
            # 'Perfect' adaptability, always choose best question
            elif r == 0:
                player = s.getPlayer(str(p))
                check = False
                for i in range(itemcount):
                    chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 1)
                    if chance == 0.5:
                    #if np.absolute(player.rating - s.getItem(str(i)).rating) < np.absolute(player.rating - itemmatch.rating):
                        itemmatch = s.getItem(str(i))
                        s.game(player.name, itemmatch.name)
                        check = True
                        break
                    else:
                        continue
                if not check:
                    break
            # r as acceptable elo range for questions
            else:
                player = s.getPlayer(str(p))
                chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 2)
                for i in range(itemcount):
                    item = s.getItem(str(i))
                    if chance > 0.15 and chance < 0.85:
                        s.game(player.name, item.name)
                        break
                    else:
                        continue

print(s.getRatingList())
simulate(5, 300)
print(s.getRatingList())