from elo import *
import numpy as np
import csv

s = System()

# Add players
playercount = 100
# Add items
itemcount = 4000

# Add Classes
s.addClass("a", 1000)
s.addClass("b", 1000)

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
def simulate(r):
    print("scenario: " + str(r))
    print("playercount: " + str(playercount))
    print("itemcount: " + str(itemcount))
    for p in range(playercount):
        print("-----" + str(p) + "------")
        if r == -1:
            no_adaptivity(p)
        elif r == 0:
            perfect_adaptivity(p)
        else:
            range_adaptivity(p)

def no_adaptivity(p):
    item = s.getItem(str(np.random.randint(0, itemcount)))
    player = s.getPlayer(str(p))
    s.game(player.name, item.name)

def perfect_adaptivity(p):
    player = s.getPlayer(str(p))
    for i in range(itemcount):
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), s.getItem(str(i))), 1)
        if chance == 0.5:
            # if np.absolute(player.rating - s.getItem(str(i)).rating) < np.absolute(player.rating - itemmatch.rating):
            itemmatch = s.getItem(str(i))
            s.game(player.name, itemmatch.name)

def range_adaptivity(p):
    player = s.getPlayer(str(p))
    for i in range(itemcount):
        item = s.getItem(str(i))
        chance = np.round(s.getPlayer(str(p)).compareRating(s.getPlayer(str(p)), item), 2)
        if chance > 0.15 and chance < 0.85:
            s.game(player.name, item.name)


simulate(-1)

ratings = []
ratinglist = s.getRatingList()

for i in range(len(ratinglist)):
    ratings.append(ratinglist[i][2])

print(ratinglist)

with open("result", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(ratings)